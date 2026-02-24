# ClaudeForge Design Document

**Date:** February 24, 2026
**Status:** Approved
**Author:** ThamJiaHe

---

## 1. Overview

ClaudeForge is a free, open-source web application that transforms plain English descriptions into production-ready Claude prompts. Users select their target Claude model, choose from 9 output formats, configure advanced parameters, and receive structured prompts with relevant skill/plugin suggestions.

### Vision

Turn the Claude Prompt Engineering Guide repository into a living, interactive product that anyone can use without reading 50+ pages of documentation.

### Differentiators

1. **Model-Aware Generation** -- prompts are tailored to each model's capabilities
2. **9 Output Formats** -- generate once, copy in XML, TOON, Harness, or 6 other formats
3. **Skill & Plugin Suggestions** -- maps user intent to 200+ Claude Code skills
4. **Full Parameter Control** -- thinking, effort, max tokens with model-specific constraints
5. **Prompt History** -- searchable, filterable personal prompt library

---

## 2. Technical Architecture

### Approach

Monolithic Next.js 15 application with Edge Runtime on the prompt generation route for streaming. Single repo, single Vercel deployment.

### Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 15 (App Router) |
| UI | React 19 + shadcn/ui (Radix + Tailwind) |
| Styling | Tailwind CSS v4 |
| Animation | Framer Motion |
| Icons | Lucide React |
| Code Display | Shiki |
| Theme | next-themes (light/dark/system) |
| State | Zustand |
| Forms | React Hook Form + Zod |
| Database | Supabase (PostgreSQL + Auth) |
| Hosting | Vercel |
| Auth | Supabase Auth (GitHub + Google OAuth) |

### Design Style

Clean minimal, Apple-like aesthetic. Light + dark mode, generous whitespace, subtle shadows instead of borders, intentional animations that communicate meaning.

---

## 3. Core User Flow

```
1. LAND     User arrives at ClaudeForge. Sees clean hero with input box.
2. CONFIGURE Select model (Opus 4.6, Sonnet 4.6, Haiku 4.5), format, parameters.
3. DESCRIBE  Type plain English: "I need a code reviewer for security issues."
4. GENERATE  Click Generate (or Cmd+Enter). Claude API streams the response.
5. REVIEW    See structured prompt + suggested skills + parameter tips.
6. COPY      One-click copy. Optionally save to history.
```

### Access Model

- Free and open source
- BYOK (Bring Your Own Key) -- users provide their own Anthropic API key
- No signup required to generate prompts
- Optional Supabase auth for persistent history across devices

---

## 4. Page Routes

| Route | Purpose |
|---|---|
| `/` | Hero + Prompt Generator (main experience) |
| `/history` | Saved prompts -- searchable, filterable, favorites |
| `/docs` | How-to guide, format explanations, tips |
| `/settings` | API key management, theme preferences |

---

## 5. Prompt Generation Engine

### How It Works

The API route builds a dynamic **meta-prompt** sent to the Claude API:

1. **System prompt** -- "You are ClaudeForge, an expert prompt engineer..." with format-specific instructions
2. **Model context injection** -- Model-specific capabilities (e.g., Opus 4.6 supports adaptive thinking and max effort; Haiku does not support extended thinking)
3. **Format template** -- Structural rules for the selected format
4. **Skill matching instructions** -- Analyzes task and suggests relevant skills from a curated registry

### Data Flow

```
User Input + Model + Format + Params
        |
        v
  [Meta-Prompt Builder]  (server-side, builds the system prompt)
        |
        v
  [Claude API Call]  (Edge Runtime, streaming)
        |
        v
  [Response Parser]  (extracts prompt, skills, tips)
        |
        v
  [Format Converter]  (client-side, enables format switching)
        |
        v
  Output Panel (syntax highlighted, copyable)
```

### The 9 Output Formats

| Format | Description |
|---|---|
| XML (Anthropic Official) | `<system_prompt>`, `<task>`, `<rules>` tags |
| TOON | `[ROLE]`, `[TASK]`, `[OUTPUT]` blocks |
| Harness Style | YAML-like structured prompts with metadata |
| Markdown | Headers + bullet points, human-readable |
| Plain Text | No formatting, raw prompt |
| JSON Structured | Machine-readable JSON schema |
| YAML Config | Key-value config-file style |
| Claude.md | `.claude/` project rules format |
| System+User Split | Separate system and user message blocks |

### Format Switching

After generation, users can switch between formats **without regenerating**. The initial Claude API call returns structured data; format conversion happens client-side via a converter module.

### Skill/Plugin Matching

A curated JSON registry of 200+ skills (sourced from the prompt engineering guide repo) is embedded in the app. The engine analyzes user intent and maps it to relevant skills:

- "review my PR" --> `pr-review-toolkit:review-pr`, `code-review:code-review`
- "debug this error" --> `superpowers:systematic-debugging`, `error-debugging:debugger`
- "build a REST API" --> `backend-development:feature-development`, `api-scaffolding:fastapi-templates`

---

## 6. Data Model (Supabase)

### Tables

```sql
-- User profiles (extends Supabase Auth)
CREATE TABLE profiles (
  id              UUID PRIMARY KEY REFERENCES auth.users,
  display_name    TEXT,
  preferred_model TEXT DEFAULT 'claude-sonnet-4-6',
  preferred_format TEXT DEFAULT 'xml',
  theme           TEXT DEFAULT 'system',
  created_at      TIMESTAMPTZ DEFAULT now(),
  updated_at      TIMESTAMPTZ DEFAULT now()
);

-- Prompt history
CREATE TABLE prompt_history (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID REFERENCES profiles(id),
  title           TEXT,
  input_text      TEXT NOT NULL,
  output_prompt   TEXT NOT NULL,
  model           TEXT NOT NULL,
  format          TEXT NOT NULL,
  parameters      JSONB DEFAULT '{}',
  suggested_skills TEXT[] DEFAULT '{}',
  is_favorite     BOOLEAN DEFAULT false,
  created_at      TIMESTAMPTZ DEFAULT now(),
  updated_at      TIMESTAMPTZ DEFAULT now()
);

-- Encrypted API keys (optional)
CREATE TABLE api_keys (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID REFERENCES profiles(id) NOT NULL,
  encrypted_key   TEXT NOT NULL,
  key_prefix      TEXT NOT NULL,
  last_used_at    TIMESTAMPTZ,
  created_at      TIMESTAMPTZ DEFAULT now()
);
```

### Security

- Row Level Security (RLS) on all tables -- users access only their own data
- API keys encrypted with AES-256 + per-user salt
- Anonymous users: history stored in localStorage only (no DB writes without auth)

### API Key Handling

- **Default (Client-Side Only):** Key stored in localStorage, API calls made directly from browser to Claude API. Key never touches the server.
- **Opt-in (Server-Side Encrypted):** Key encrypted and stored in Supabase, decrypted only during generation, API calls proxied through Next.js API route.

---

## 7. API Routes

```
/app/api/
  generate/
    route.ts          POST  Prompt generation (Edge Runtime, streaming)
                      Input:  { text, model, format, params, apiKey }
                      Output: SSE stream -> { prompt, skills, tips }

  formats/convert/
    route.ts          POST  Client-side format conversion
                      Input:  { structuredPrompt, targetFormat }
                      Output: { convertedPrompt }

  history/
    route.ts          GET (list), POST (create)
    [id]/
      route.ts        GET (single), PATCH (update), DELETE (remove)

  auth/callback/
    route.ts          Supabase auth callback handler
```

---

## 8. UI Component Architecture

### Component Tree (Main Page)

```
<HomePage>
  <Header>
    Logo + "ClaudeForge"
    <ThemeToggle>
    <NavLinks>             History | Docs
    <AuthButton>           Sign In / Avatar

  <HeroSection>
    <Headline>             "Craft perfect Claude prompts"
    <Subheadline>          "Plain English to Production-ready"

  <PromptWorkspace>
    <ConfigBar>
      <ModelSelector>      Dropdown: Opus 4.6, Sonnet 4.6, Haiku 4.5
      <FormatSelector>     Dropdown: XML, TOON, Harness, etc.
      <ThinkingToggle>     Switch: Extended Thinking ON/OFF
      <EffortSlider>       Segmented: low | medium | high | max
      <MaxTokensInput>     Number input with smart defaults

    <InputPanel>
      <PromptTextarea>     Auto-resize, placeholder examples
      <GenerateButton>     "Generate Prompt" + Cmd+Enter hint

    <OutputPanel>
      <FormatTabs>         Switch formats without regenerating
      <CodeBlock>          Syntax-highlighted output (Shiki)
      <CopyButton>         One-click copy with toast
      <SkillSuggestions>   Pill badges with skill names
      <ParameterTips>      Contextual advice
      <SaveButton>         Save to history (requires auth)

  <Footer>
    "Open Source on GitHub"
    Version + Links
```

### Responsive Layout

| Breakpoint | Layout |
|---|---|
| Desktop (1024px+) | Side-by-side: Input left, Output right |
| Tablet (768-1023px) | Stacked: Input top, Output bottom |
| Mobile (<768px) | Full-width stacked, collapsible config |

---

## 9. Deployment

| Component | Platform | Cost |
|---|---|---|
| Next.js App | Vercel (Hobby/Pro) | Free tier |
| Database | Supabase Free Tier | 500MB, 50K auth users |
| Domain | claudeforge.dev (or similar) | ~$12/year |
| Monitoring | Vercel Analytics | Free |

### Environment Variables

```
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
API_KEY_ENCRYPTION_SECRET=
```

---

## 10. Out of Scope (v1)

- Chat interface (this is a prompt generator, not a chat app)
- Prompt marketplace / sharing
- Multi-LLM support (Claude-only is the differentiator)
- Team/organization features
- Prompt testing/evaluation
- Chrome extension
- Mobile native app

These are potential v2 features.

---

## 11. Success Criteria

- User can go from landing to copied prompt in under 30 seconds
- All 9 output formats produce valid, copy-pasteable prompts
- Model-specific features (adaptive thinking, effort max) are correctly gated
- Skill suggestions are relevant to the user's described task
- History persists across sessions for authenticated users
- Lighthouse score above 90 on all metrics
- Works on latest Chrome, Firefox, Safari, Edge

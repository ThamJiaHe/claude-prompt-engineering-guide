# ClaudeForge Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build ClaudeForge, a free open-source web app that transforms plain English into production-ready Claude prompts with model-aware generation, 9 output formats, and skill suggestions.

**Architecture:** Monolithic Next.js 15 (App Router) with Edge Runtime on the generation route. Supabase for auth + history. Zustand for client state. shadcn/ui + Tailwind v4 for the Apple-clean UI.

**Tech Stack:** Next.js 15, React 19, TypeScript, Tailwind CSS v4, shadcn/ui, Framer Motion, Zustand, Zod, Shiki, Supabase, Vercel

**Design Doc:** `docs/plans/2026-02-24-claudeforge-design.md`

---

## Phase 1: Project Scaffolding (Tasks 1-3)

### Task 1: Initialize Next.js 15 Project

**Files:**
- Create: `claudeforge/` (new repo root)
- Create: `claudeforge/package.json`
- Create: `claudeforge/.gitignore`
- Create: `claudeforge/tsconfig.json`

**Step 1: Create the project**

```bash
cd ~/Documents
npx create-next-app@latest claudeforge --typescript --tailwind --eslint --app --src-dir --import-alias "@/*" --turbopack
cd claudeforge
```

**Step 2: Verify it runs**

```bash
npm run dev
```
Expected: App running on http://localhost:3000 with default Next.js page.

**Step 3: Initialize git**

```bash
git init
git add .
git commit -m "chore: initialize Next.js 15 project with TypeScript and Tailwind"
```

---

### Task 2: Install Core Dependencies

**Files:**
- Modify: `claudeforge/package.json`

**Step 1: Install UI and state dependencies**

```bash
npm install @supabase/supabase-js @supabase/ssr zustand framer-motion lucide-react next-themes zod react-hook-form @hookform/resolvers shiki @anthropic-ai/sdk
```

**Step 2: Install shadcn/ui CLI and initialize**

```bash
npx shadcn@latest init -d
```

When prompted:
- Style: Default
- Base color: Neutral
- CSS variables: Yes

**Step 3: Add needed shadcn/ui components**

```bash
npx shadcn@latest add button input textarea select dropdown-menu dialog tabs toast badge separator card switch slider label popover command avatar sheet scroll-area tooltip
```

**Step 4: Verify build**

```bash
npm run build
```
Expected: Build succeeds with no errors.

**Step 5: Commit**

```bash
git add .
git commit -m "chore: add core dependencies (supabase, zustand, shadcn, framer-motion, shiki)"
```

---

### Task 3: Project Structure & Config Files

**Files:**
- Create: `src/lib/constants.ts`
- Create: `src/lib/types.ts`
- Create: `src/lib/utils.ts` (shadcn creates this, extend it)
- Create: `.env.local.example`

**Step 1: Create the environment example file**

Create `.env.local.example`:
```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Encryption (for server-side API key storage)
API_KEY_ENCRYPTION_SECRET=generate-a-32-byte-hex-string
```

**Step 2: Create types file**

Create `src/lib/types.ts`:
```typescript
// ─── Model Types ────────────────────────────────────────
export type ClaudeModel = 'claude-opus-4-6' | 'claude-sonnet-4-6' | 'claude-haiku-4-5';

export interface ModelInfo {
  id: ClaudeModel;
  apiString: string;
  displayName: string;
  description: string;
  supportsThinking: boolean;
  supportsAdaptiveThinking: boolean;
  supportsEffortMax: boolean;
  maxOutputTokens: number;
  contextWindow: number;
  inputPricePer1M: number;
  outputPricePer1M: number;
}

// ─── Format Types ───────────────────────────────────────
export type PromptFormat =
  | 'xml'
  | 'toon'
  | 'harness'
  | 'markdown'
  | 'plaintext'
  | 'json'
  | 'yaml'
  | 'claudemd'
  | 'system-user-split';

export interface FormatInfo {
  id: PromptFormat;
  displayName: string;
  description: string;
  fileExtension: string;
  syntaxLanguage: string; // for Shiki highlighting
}

// ─── Parameter Types ────────────────────────────────────
export type EffortLevel = 'low' | 'medium' | 'high' | 'max';

export interface GenerationParams {
  model: ClaudeModel;
  format: PromptFormat;
  enableThinking: boolean;
  effort: EffortLevel;
  maxTokens: number;
}

// ─── Generation Types ───────────────────────────────────
export interface GenerationRequest {
  text: string;
  params: GenerationParams;
  apiKey: string;
}

export interface GenerationResult {
  prompt: string;
  structuredData: Record<string, string>; // for format conversion
  suggestedSkills: SkillSuggestion[];
  parameterTips: string[];
  model: ClaudeModel;
  format: PromptFormat;
}

// ─── Skill Types ────────────────────────────────────────
export interface SkillSuggestion {
  id: string;           // e.g. "superpowers:systematic-debugging"
  name: string;         // e.g. "Systematic Debugging"
  category: string;     // e.g. "debugging"
  description: string;  // short explanation
  relevance: number;    // 0-1 confidence score
}

export interface SkillRegistryEntry {
  id: string;
  name: string;
  category: string;
  description: string;
  keywords: string[];   // for matching
}

// ─── History Types ──────────────────────────────────────
export interface PromptHistoryEntry {
  id: string;
  title: string;
  inputText: string;
  outputPrompt: string;
  model: ClaudeModel;
  format: PromptFormat;
  parameters: GenerationParams;
  suggestedSkills: string[];
  isFavorite: boolean;
  createdAt: string;
  updatedAt: string;
}

// ─── User Types ─────────────────────────────────────────
export interface UserProfile {
  id: string;
  displayName: string | null;
  preferredModel: ClaudeModel;
  preferredFormat: PromptFormat;
  theme: 'light' | 'dark' | 'system';
}
```

**Step 3: Create constants file**

Create `src/lib/constants.ts`:
```typescript
import type { ModelInfo, FormatInfo } from './types';

export const MODELS: ModelInfo[] = [
  {
    id: 'claude-opus-4-6',
    apiString: 'claude-opus-4-6-20250205',
    displayName: 'Claude Opus 4.6',
    description: 'Most powerful — adaptive thinking, 128K output, 1M context (beta)',
    supportsThinking: true,
    supportsAdaptiveThinking: true,
    supportsEffortMax: true,
    maxOutputTokens: 128_000,
    contextWindow: 200_000,
    inputPricePer1M: 5.0,
    outputPricePer1M: 25.0,
  },
  {
    id: 'claude-sonnet-4-6',
    apiString: 'claude-sonnet-4-6-20250217',
    displayName: 'Claude Sonnet 4.6',
    description: 'Best balance — near-Opus performance, effort support, great value',
    supportsThinking: true,
    supportsAdaptiveThinking: false,
    supportsEffortMax: false,
    maxOutputTokens: 64_000,
    contextWindow: 200_000,
    inputPricePer1M: 3.0,
    outputPricePer1M: 15.0,
  },
  {
    id: 'claude-haiku-4-5',
    apiString: 'claude-haiku-4-5-20251001',
    displayName: 'Claude Haiku 4.5',
    description: 'Fastest — quick tasks, cost-efficient, no extended thinking',
    supportsThinking: false,
    supportsAdaptiveThinking: false,
    supportsEffortMax: false,
    maxOutputTokens: 8_192,
    contextWindow: 200_000,
    inputPricePer1M: 1.0,
    outputPricePer1M: 5.0,
  },
];

export const FORMATS: FormatInfo[] = [
  { id: 'xml', displayName: 'XML (Anthropic)', description: 'Official Anthropic prompt structure with XML tags', fileExtension: 'xml', syntaxLanguage: 'xml' },
  { id: 'toon', displayName: 'TOON', description: '[ROLE], [TASK], [OUTPUT] block format', fileExtension: 'txt', syntaxLanguage: 'markdown' },
  { id: 'harness', displayName: 'Harness Style', description: 'YAML-like structured prompts with metadata', fileExtension: 'yaml', syntaxLanguage: 'yaml' },
  { id: 'markdown', displayName: 'Markdown', description: 'Headers and bullets, human-readable', fileExtension: 'md', syntaxLanguage: 'markdown' },
  { id: 'plaintext', displayName: 'Plain Text', description: 'No formatting, raw prompt text', fileExtension: 'txt', syntaxLanguage: 'text' },
  { id: 'json', displayName: 'JSON', description: 'Machine-readable structured JSON', fileExtension: 'json', syntaxLanguage: 'json' },
  { id: 'yaml', displayName: 'YAML Config', description: 'Key-value config-file style', fileExtension: 'yaml', syntaxLanguage: 'yaml' },
  { id: 'claudemd', displayName: 'Claude.md', description: 'Claude Code project rules format', fileExtension: 'md', syntaxLanguage: 'markdown' },
  { id: 'system-user-split', displayName: 'System + User', description: 'Separate system and user message blocks', fileExtension: 'json', syntaxLanguage: 'json' },
];

export const DEFAULT_MODEL = 'claude-sonnet-4-6' as const;
export const DEFAULT_FORMAT = 'xml' as const;
export const DEFAULT_EFFORT = 'medium' as const;
export const DEFAULT_MAX_TOKENS = 4096;

export const APP_NAME = 'ClaudeForge';
export const APP_DESCRIPTION = 'Craft perfect Claude prompts from plain English';
export const APP_VERSION = '0.1.0';
```

**Step 4: Commit**

```bash
git add .
git commit -m "feat: add type definitions, constants, and env config"
```

---

## Phase 2: Core Data Layer (Tasks 4-6)

### Task 4: Skill Registry Data

**Files:**
- Create: `src/data/skill-registry.ts`

**Step 1: Create the skill registry**

Create `src/data/skill-registry.ts` with all 200+ skills organized by category. Each entry has `id`, `name`, `category`, `description`, and `keywords` array for matching. Categories include: code-review, debugging, testing, backend, frontend, mobile, devops, security, database, documentation, ai-ml, design, performance, git, deployment.

The file should export `SKILL_REGISTRY: SkillRegistryEntry[]` containing entries like:
```typescript
import type { SkillRegistryEntry } from '@/lib/types';

export const SKILL_REGISTRY: SkillRegistryEntry[] = [
  // ─── Code Review ──────────────────────────────────────
  { id: 'code-review:code-review', name: 'Code Review', category: 'code-review', description: 'Elite code review for security, performance, and reliability', keywords: ['review', 'code quality', 'pull request', 'pr', 'lint', 'static analysis'] },
  { id: 'pr-review-toolkit:review-pr', name: 'PR Review', category: 'code-review', description: 'Comprehensive pull request review toolkit', keywords: ['pull request', 'pr review', 'github', 'merge', 'diff'] },
  { id: 'superpowers:requesting-code-review', name: 'Request Code Review', category: 'code-review', description: 'Structured code review request workflow', keywords: ['review request', 'code review', 'feedback'] },

  // ─── Debugging ────────────────────────────────────────
  { id: 'superpowers:systematic-debugging', name: 'Systematic Debugging', category: 'debugging', description: 'Hypothesis-driven debugging with evidence gathering', keywords: ['debug', 'error', 'bug', 'fix', 'troubleshoot', 'crash', 'exception'] },
  { id: 'error-debugging:debugger', name: 'Error Debugger', category: 'debugging', description: 'Specialist for errors, test failures, and unexpected behavior', keywords: ['error', 'stack trace', 'failure', 'unexpected'] },
  { id: 'error-debugging:error-detective', name: 'Error Detective', category: 'debugging', description: 'Search logs and codebases for error patterns', keywords: ['logs', 'error pattern', 'stack trace', 'anomaly'] },

  // ─── Testing ──────────────────────────────────────────
  { id: 'superpowers:test-driven-development', name: 'TDD Workflow', category: 'testing', description: 'Red-green-refactor test-driven development', keywords: ['tdd', 'test', 'unit test', 'testing', 'red green refactor'] },
  { id: 'tdd-workflows:tdd-cycle', name: 'TDD Cycle', category: 'testing', description: 'Complete TDD red-green-refactor cycle', keywords: ['tdd', 'test cycle', 'red green'] },
  { id: 'unit-testing:test-automator', name: 'Test Automator', category: 'testing', description: 'AI-powered test automation with modern frameworks', keywords: ['test automation', 'e2e', 'integration test', 'jest', 'pytest'] },

  // ─── Backend ──────────────────────────────────────────
  { id: 'backend-development:feature-development', name: 'Backend Feature', category: 'backend', description: 'Build backend features with scalable API design', keywords: ['api', 'backend', 'server', 'endpoint', 'rest', 'graphql'] },
  { id: 'api-scaffolding:fastapi-pro', name: 'FastAPI Pro', category: 'backend', description: 'High-performance async APIs with FastAPI', keywords: ['fastapi', 'python', 'async', 'api'] },
  { id: 'api-scaffolding:django-pro', name: 'Django Pro', category: 'backend', description: 'Django 5.x with DRF, Celery, and Channels', keywords: ['django', 'python', 'orm', 'drf'] },

  // ─── Frontend ─────────────────────────────────────────
  { id: 'frontend-mobile-development:frontend-developer', name: 'Frontend Developer', category: 'frontend', description: 'React 19, Next.js 15, modern frontend architecture', keywords: ['react', 'nextjs', 'frontend', 'ui', 'component', 'css', 'layout'] },
  { id: 'multi-platform-apps:mobile-developer', name: 'Mobile Developer', category: 'mobile', description: 'React Native, Flutter, or native mobile apps', keywords: ['mobile', 'ios', 'android', 'react native', 'flutter', 'app'] },

  // ─── DevOps & Infrastructure ──────────────────────────
  { id: 'cloud-infrastructure:kubernetes-architect', name: 'Kubernetes Architect', category: 'devops', description: 'Cloud-native infrastructure and GitOps workflows', keywords: ['kubernetes', 'k8s', 'docker', 'container', 'devops', 'deploy'] },
  { id: 'cicd-automation:deployment-engineer', name: 'Deployment Engineer', category: 'devops', description: 'CI/CD pipelines, GitOps, and deployment automation', keywords: ['ci', 'cd', 'pipeline', 'deploy', 'github actions', 'gitlab'] },
  { id: 'cloud-infrastructure:terraform-specialist', name: 'Terraform Specialist', category: 'devops', description: 'Advanced IaC automation and state management', keywords: ['terraform', 'iac', 'infrastructure', 'aws', 'azure', 'gcp'] },

  // ─── Security ─────────────────────────────────────────
  { id: 'security-scanning:security-auditor', name: 'Security Auditor', category: 'security', description: 'DevSecOps, vulnerability assessment, OWASP', keywords: ['security', 'audit', 'vulnerability', 'owasp', 'penetration', 'cve'] },
  { id: 'backend-api-security:backend-security-coder', name: 'Backend Security', category: 'security', description: 'Input validation, authentication, API security', keywords: ['auth', 'validation', 'injection', 'xss', 'csrf'] },

  // ─── Database ─────────────────────────────────────────
  { id: 'database-design:database-architect', name: 'Database Architect', category: 'database', description: 'Data layer design, technology selection, schema modeling', keywords: ['database', 'schema', 'sql', 'nosql', 'migration', 'postgres', 'mysql'] },
  { id: 'database-cloud-optimization:database-optimizer', name: 'Database Optimizer', category: 'database', description: 'Query optimization, indexing, caching strategies', keywords: ['query', 'performance', 'index', 'cache', 'n+1', 'slow query'] },

  // ─── Documentation ────────────────────────────────────
  { id: 'documentation-generation:docs-architect', name: 'Docs Architect', category: 'documentation', description: 'Comprehensive technical documentation from codebases', keywords: ['documentation', 'docs', 'readme', 'guide', 'manual', 'wiki'] },
  { id: 'documentation-generation:tutorial-engineer', name: 'Tutorial Engineer', category: 'documentation', description: 'Step-by-step tutorials and educational content', keywords: ['tutorial', 'guide', 'how-to', 'learn', 'onboarding', 'walkthrough'] },

  // ─── AI & LLM ─────────────────────────────────────────
  { id: 'llm-application-dev:ai-engineer', name: 'AI Engineer', category: 'ai-ml', description: 'Production LLM apps, RAG systems, and agents', keywords: ['ai', 'llm', 'rag', 'agent', 'chatbot', 'embedding', 'vector'] },
  { id: 'llm-application-dev:prompt-engineer', name: 'Prompt Engineer', category: 'ai-ml', description: 'Advanced prompting techniques and LLM optimization', keywords: ['prompt', 'prompt engineering', 'chain of thought', 'few-shot'] },

  // ─── Performance ──────────────────────────────────────
  { id: 'application-performance:performance-engineer', name: 'Performance Engineer', category: 'performance', description: 'Observability, optimization, and scalability', keywords: ['performance', 'optimize', 'slow', 'latency', 'throughput', 'profiling'] },

  // ─── Git & Workflow ───────────────────────────────────
  { id: 'git-pr-workflows:git-workflow', name: 'Git Workflow', category: 'git', description: 'Git branching, merging, and PR workflows', keywords: ['git', 'branch', 'merge', 'rebase', 'conflict', 'workflow'] },
  { id: 'superpowers:brainstorming', name: 'Brainstorming', category: 'workflow', description: 'Turn ideas into fully formed designs and specs', keywords: ['brainstorm', 'idea', 'design', 'plan', 'architecture', 'spec'] },

  // ─── Languages ────────────────────────────────────────
  { id: 'python-development:python-pro', name: 'Python Pro', category: 'language', description: 'Python 3.12+ with modern features and async', keywords: ['python', 'pip', 'venv', 'async', 'typing'] },
  { id: 'javascript-typescript:typescript-pro', name: 'TypeScript Pro', category: 'language', description: 'Advanced TypeScript with strict type safety', keywords: ['typescript', 'types', 'generics', 'interface'] },
  { id: 'systems-programming:rust-pro', name: 'Rust Pro', category: 'language', description: 'Rust with modern async and systems programming', keywords: ['rust', 'cargo', 'borrow checker', 'async', 'tokio'] },
  { id: 'systems-programming:golang-pro', name: 'Go Pro', category: 'language', description: 'Go 1.21+ with concurrency and microservices', keywords: ['go', 'golang', 'goroutine', 'channel', 'concurrency'] },
];
```

**Step 2: Commit**

```bash
git add .
git commit -m "feat: add curated skill registry with 30+ skills and keyword matching"
```

---

### Task 5: Zustand Store (Client State)

**Files:**
- Create: `src/store/use-forge-store.ts`
- Create: `src/store/use-history-store.ts`

**Step 1: Create the main forge store**

Create `src/store/use-forge-store.ts`:
```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { ClaudeModel, PromptFormat, EffortLevel, GenerationResult } from '@/lib/types';
import { DEFAULT_MODEL, DEFAULT_FORMAT, DEFAULT_EFFORT, DEFAULT_MAX_TOKENS } from '@/lib/constants';

interface ForgeState {
  // ─── API Key ──────────────────────────────────────────
  apiKey: string;
  setApiKey: (key: string) => void;
  clearApiKey: () => void;

  // ─── Configuration ────────────────────────────────────
  model: ClaudeModel;
  format: PromptFormat;
  enableThinking: boolean;
  effort: EffortLevel;
  maxTokens: number;
  setModel: (model: ClaudeModel) => void;
  setFormat: (format: PromptFormat) => void;
  setEnableThinking: (enabled: boolean) => void;
  setEffort: (effort: EffortLevel) => void;
  setMaxTokens: (tokens: number) => void;

  // ─── Input ────────────────────────────────────────────
  inputText: string;
  setInputText: (text: string) => void;

  // ─── Generation State ─────────────────────────────────
  isGenerating: boolean;
  result: GenerationResult | null;
  error: string | null;
  setIsGenerating: (generating: boolean) => void;
  setResult: (result: GenerationResult | null) => void;
  setError: (error: string | null) => void;

  // ─── Active Format Tab ────────────────────────────────
  activeOutputFormat: PromptFormat;
  setActiveOutputFormat: (format: PromptFormat) => void;
}

export const useForgeStore = create<ForgeState>()(
  persist(
    (set) => ({
      // API Key
      apiKey: '',
      setApiKey: (key) => set({ apiKey: key }),
      clearApiKey: () => set({ apiKey: '' }),

      // Configuration
      model: DEFAULT_MODEL,
      format: DEFAULT_FORMAT,
      enableThinking: false,
      effort: DEFAULT_EFFORT,
      maxTokens: DEFAULT_MAX_TOKENS,
      setModel: (model) => set({ model }),
      setFormat: (format) => set({ format, activeOutputFormat: format }),
      setEnableThinking: (enableThinking) => set({ enableThinking }),
      setEffort: (effort) => set({ effort }),
      setMaxTokens: (maxTokens) => set({ maxTokens }),

      // Input
      inputText: '',
      setInputText: (inputText) => set({ inputText }),

      // Generation State
      isGenerating: false,
      result: null,
      error: null,
      setIsGenerating: (isGenerating) => set({ isGenerating }),
      setResult: (result) => set({ result, error: null }),
      setError: (error) => set({ error }),

      // Active Format Tab
      activeOutputFormat: DEFAULT_FORMAT,
      setActiveOutputFormat: (activeOutputFormat) => set({ activeOutputFormat }),
    }),
    {
      name: 'claudeforge-config',
      partialize: (state) => ({
        apiKey: state.apiKey,
        model: state.model,
        format: state.format,
        enableThinking: state.enableThinking,
        effort: state.effort,
        maxTokens: state.maxTokens,
      }),
    }
  )
);
```

**Step 2: Create history store**

Create `src/store/use-history-store.ts`:
```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { PromptHistoryEntry } from '@/lib/types';

interface HistoryState {
  entries: PromptHistoryEntry[];
  addEntry: (entry: PromptHistoryEntry) => void;
  removeEntry: (id: string) => void;
  toggleFavorite: (id: string) => void;
  clearHistory: () => void;
  getEntry: (id: string) => PromptHistoryEntry | undefined;
}

export const useHistoryStore = create<HistoryState>()(
  persist(
    (set, get) => ({
      entries: [],

      addEntry: (entry) =>
        set((state) => ({
          entries: [entry, ...state.entries].slice(0, 500), // keep max 500
        })),

      removeEntry: (id) =>
        set((state) => ({
          entries: state.entries.filter((e) => e.id !== id),
        })),

      toggleFavorite: (id) =>
        set((state) => ({
          entries: state.entries.map((e) =>
            e.id === id ? { ...e, isFavorite: !e.isFavorite } : e
          ),
        })),

      clearHistory: () => set({ entries: [] }),

      getEntry: (id) => get().entries.find((e) => e.id === id),
    }),
    { name: 'claudeforge-history' }
  )
);
```

**Step 3: Commit**

```bash
git add .
git commit -m "feat: add Zustand stores for config persistence and prompt history"
```

---

### Task 6: Supabase Client Setup

**Files:**
- Create: `src/lib/supabase/client.ts`
- Create: `src/lib/supabase/server.ts`
- Create: `src/lib/supabase/middleware.ts`
- Modify: `src/middleware.ts`

**Step 1: Create browser client**

Create `src/lib/supabase/client.ts`:
```typescript
import { createBrowserClient } from '@supabase/ssr';

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
}
```

**Step 2: Create server client**

Create `src/lib/supabase/server.ts`:
```typescript
import { createServerClient } from '@supabase/ssr';
import { cookies } from 'next/headers';

export async function createClient() {
  const cookieStore = await cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            );
          } catch {
            // Called from Server Component — ignore
          }
        },
      },
    }
  );
}
```

**Step 3: Create middleware helper**

Create `src/lib/supabase/middleware.ts`:
```typescript
import { createServerClient } from '@supabase/ssr';
import { NextResponse, type NextRequest } from 'next/server';

export async function updateSession(request: NextRequest) {
  let supabaseResponse = NextResponse.next({ request });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value }) =>
            request.cookies.set(name, value)
          );
          supabaseResponse = NextResponse.next({ request });
          cookiesToSet.forEach(({ name, value, options }) =>
            supabaseResponse.cookies.set(name, value, options)
          );
        },
      },
    }
  );

  await supabase.auth.getUser();
  return supabaseResponse;
}
```

**Step 4: Create Next.js middleware**

Create `src/middleware.ts`:
```typescript
import { type NextRequest } from 'next/server';
import { updateSession } from '@/lib/supabase/middleware';

export async function middleware(request: NextRequest) {
  return await updateSession(request);
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ],
};
```

**Step 5: Commit**

```bash
git add .
git commit -m "feat: add Supabase client, server, and middleware setup"
```

---

## Phase 3: Prompt Engine (Tasks 7-9)

### Task 7: Meta-Prompt Builder

**Files:**
- Create: `src/lib/engine/meta-prompt-builder.ts`
- Create: `src/lib/engine/format-instructions.ts`
- Create: `src/lib/engine/model-context.ts`

**Step 1: Create model context provider**

Create `src/lib/engine/model-context.ts` that exports a function `getModelContext(model: ClaudeModel): string` which returns model-specific instructions for the meta-prompt. For Opus 4.6, it includes adaptive thinking and max effort info. For Haiku, it notes no extended thinking support. Each model context also lists capabilities and constraints.

**Step 2: Create format instructions provider**

Create `src/lib/engine/format-instructions.ts` that exports `getFormatInstructions(format: PromptFormat): string`. Each format returns detailed structural rules:
- XML: use `<system_prompt>`, `<task>`, `<rules>`, `<format>` tags etc.
- TOON: use `[ROLE]`, `[TASK]`, `[RULES]`, `[OUTPUT]` blocks
- Harness: YAML-like with `name:`, `description:`, `system:`, `user:` keys
- etc. for all 9 formats

**Step 3: Create the meta-prompt builder**

Create `src/lib/engine/meta-prompt-builder.ts` that exports `buildMetaPrompt(params: GenerationParams): { system: string; userPrefix: string }`. This function:
1. Gets model context for the selected model
2. Gets format instructions for the selected format
3. Builds a system prompt instructing Claude to act as an expert prompt engineer
4. Includes the skill registry summary so Claude can suggest relevant skills
5. Returns both the system message and any user message prefix

**Step 4: Commit**

```bash
git add .
git commit -m "feat: add meta-prompt builder with model context and format instructions"
```

---

### Task 8: Format Converter (Client-Side)

**Files:**
- Create: `src/lib/engine/format-converter.ts`

**Step 1: Create the format converter**

Create `src/lib/engine/format-converter.ts` that exports `convertFormat(structuredData: Record<string, string>, targetFormat: PromptFormat): string`. This takes the structured prompt data (role, task, rules, format, examples, thinking, background) and renders it in the target format. Pure function, no API calls — runs entirely client-side.

Each format converter is a simple string template that maps the structured fields into the target format's syntax.

**Step 2: Write tests for the converter**

Create `src/lib/engine/__tests__/format-converter.test.ts` with tests for each of the 9 formats. Verify that converting sample structured data produces valid output in each format.

**Step 3: Run tests**

```bash
npm test -- --testPathPattern=format-converter
```
Expected: All 9 format tests pass.

**Step 4: Commit**

```bash
git add .
git commit -m "feat: add client-side format converter for all 9 output formats"
```

---

### Task 9: Generation API Route (Edge Runtime + Streaming)

**Files:**
- Create: `src/app/api/generate/route.ts`

**Step 1: Create the streaming generation route**

Create `src/app/api/generate/route.ts`:
```typescript
import { NextRequest } from 'next/server';
import Anthropic from '@anthropic-ai/sdk';
import { buildMetaPrompt } from '@/lib/engine/meta-prompt-builder';
import type { GenerationParams } from '@/lib/types';

export const runtime = 'edge';

export async function POST(request: NextRequest) {
  try {
    const { text, params, apiKey } = await request.json() as {
      text: string;
      params: GenerationParams;
      apiKey: string;
    };

    if (!apiKey || !text) {
      return new Response(
        JSON.stringify({ error: 'API key and prompt text are required' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const client = new Anthropic({ apiKey });
    const { system, userPrefix } = buildMetaPrompt(params);

    const stream = await client.messages.stream({
      model: params.model === 'claude-opus-4-6'
        ? 'claude-opus-4-6-20250205'
        : params.model === 'claude-sonnet-4-6'
        ? 'claude-sonnet-4-6-20250217'
        : 'claude-haiku-4-5-20251001',
      max_tokens: params.maxTokens,
      system,
      messages: [
        {
          role: 'user',
          content: `${userPrefix}\n\nUser's request:\n${text}`,
        },
      ],
    });

    // Convert the Anthropic SDK stream to a ReadableStream
    const encoder = new TextEncoder();
    const readableStream = new ReadableStream({
      async start(controller) {
        try {
          for await (const event of stream) {
            if (event.type === 'content_block_delta' && event.delta.type === 'text_delta') {
              controller.enqueue(
                encoder.encode(`data: ${JSON.stringify({ text: event.delta.text })}\n\n`)
              );
            }
          }
          // Send final message with metadata
          const finalMessage = await stream.finalMessage();
          controller.enqueue(
            encoder.encode(`data: ${JSON.stringify({ done: true, usage: finalMessage.usage })}\n\n`)
          );
          controller.close();
        } catch (error) {
          controller.enqueue(
            encoder.encode(`data: ${JSON.stringify({ error: String(error) })}\n\n`)
          );
          controller.close();
        }
      },
    });

    return new Response(readableStream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        Connection: 'keep-alive',
      },
    });
  } catch (error) {
    return new Response(
      JSON.stringify({ error: `Generation failed: ${String(error)}` }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
}
```

**Step 2: Commit**

```bash
git add .
git commit -m "feat: add streaming prompt generation API route (Edge Runtime)"
```

---

## Phase 4: UI Components (Tasks 10-15)

### Task 10: Layout Shell (Header, Footer, Theme)

**Files:**
- Modify: `src/app/layout.tsx`
- Create: `src/components/layout/header.tsx`
- Create: `src/components/layout/footer.tsx`
- Create: `src/components/theme-provider.tsx`
- Create: `src/components/theme-toggle.tsx`

Build the app shell: root layout with ThemeProvider (next-themes), Header with logo + nav links + theme toggle + auth button placeholder, and Footer with "Open Source on GitHub" and version. Apple-clean minimal aesthetic: white background, subtle bottom border on header, lots of whitespace.

**Step 1:** Create ThemeProvider wrapper component
**Step 2:** Create Header with logo, nav (History, Docs), ThemeToggle, AuthButton placeholder
**Step 3:** Create Footer with GitHub link and version
**Step 4:** Wire everything into root `layout.tsx`
**Step 5:** Verify in browser — header/footer render, theme switching works
**Step 6:** Commit

```bash
git add .
git commit -m "feat: add layout shell with header, footer, and theme toggle"
```

---

### Task 11: Config Bar Component

**Files:**
- Create: `src/components/forge/config-bar.tsx`
- Create: `src/components/forge/model-selector.tsx`
- Create: `src/components/forge/format-selector.tsx`
- Create: `src/components/forge/thinking-toggle.tsx`
- Create: `src/components/forge/effort-selector.tsx`
- Create: `src/components/forge/max-tokens-input.tsx`

Build the configuration bar — a horizontal strip of controls. Each component reads/writes from the Zustand store.

- **ModelSelector:** shadcn Select dropdown showing all 3 models with descriptions
- **FormatSelector:** shadcn Select dropdown showing all 9 formats
- **ThinkingToggle:** shadcn Switch, disabled when model doesn't support thinking (Haiku)
- **EffortSelector:** Segmented control with low/medium/high/max buttons, "max" disabled unless Opus 4.6
- **MaxTokensInput:** Number input with sensible defaults per model

The ConfigBar wraps all of these in a responsive horizontal layout (flexbox, wraps on mobile).

**Step 1-5:** Create each sub-component
**Step 6:** Create ConfigBar wrapper
**Step 7:** Verify in browser — all controls work, state persists on refresh
**Step 8:** Commit

```bash
git add .
git commit -m "feat: add config bar with model, format, thinking, effort, and token controls"
```

---

### Task 12: Input Panel Component

**Files:**
- Create: `src/components/forge/input-panel.tsx`
- Create: `src/components/forge/api-key-input.tsx`
- Create: `src/hooks/use-generate.ts`

Build the input panel — textarea with auto-resize, placeholder text with examples, Cmd+Enter shortcut, and the Generate button. Also includes the API key input (shown inline if no key is set, collapsible once set).

The `use-generate.ts` hook handles:
1. Reading state from the forge store
2. Calling the `/api/generate` route with SSE
3. Parsing the streamed response
4. Updating the result in the store
5. Error handling

**Step 1:** Create API key input component (password field + show/hide toggle + "stored locally" note)
**Step 2:** Create the `useGenerate` hook with streaming SSE parsing
**Step 3:** Create the InputPanel with textarea, placeholder, Cmd+Enter binding, Generate button with loading state
**Step 4:** Verify — type text, see it in store, button triggers generation (will fail without real API key, but verify the flow)
**Step 5:** Commit

```bash
git add .
git commit -m "feat: add input panel with auto-resize textarea, API key input, and generation hook"
```

---

### Task 13: Output Panel Component

**Files:**
- Create: `src/components/forge/output-panel.tsx`
- Create: `src/components/forge/code-block.tsx`
- Create: `src/components/forge/copy-button.tsx`
- Create: `src/components/forge/skill-suggestions.tsx`
- Create: `src/components/forge/parameter-tips.tsx`
- Create: `src/components/forge/format-tabs.tsx`

Build the output panel — appears after generation with an animated slide-in (Framer Motion).

- **FormatTabs:** Tab bar for switching between formats (uses format converter client-side)
- **CodeBlock:** Shiki-highlighted prompt output with line numbers
- **CopyButton:** One-click copy with toast notification ("Copied!")
- **SkillSuggestions:** Horizontal row of pill badges showing suggested skills
- **ParameterTips:** Subtle text showing tips like "This task benefits from effort: high"

**Step 1:** Create CodeBlock with Shiki highlighting
**Step 2:** Create CopyButton with clipboard API + toast
**Step 3:** Create SkillSuggestions pill badges
**Step 4:** Create ParameterTips component
**Step 5:** Create FormatTabs using shadcn Tabs
**Step 6:** Create OutputPanel wrapper with Framer Motion animation
**Step 7:** Verify — mock a result in the store, see the output panel render
**Step 8:** Commit

```bash
git add .
git commit -m "feat: add output panel with format tabs, syntax highlighting, copy, and skill suggestions"
```

---

### Task 14: Home Page Assembly

**Files:**
- Modify: `src/app/page.tsx`
- Create: `src/components/forge/hero-section.tsx`
- Create: `src/components/forge/prompt-workspace.tsx`

Assemble the home page:
1. HeroSection — headline "Craft perfect Claude prompts", subheadline, subtle gradient background
2. PromptWorkspace — contains ConfigBar + InputPanel + OutputPanel in a responsive layout (side-by-side on desktop, stacked on mobile)

**Step 1:** Create HeroSection with headline and subheadline
**Step 2:** Create PromptWorkspace layout (flex on desktop, stack on mobile)
**Step 3:** Wire into `page.tsx`
**Step 4:** Verify full flow — type prompt, select model/format, generate, see output
**Step 5:** Commit

```bash
git add .
git commit -m "feat: assemble home page with hero section and prompt workspace"
```

---

### Task 15: History Page

**Files:**
- Create: `src/app/history/page.tsx`
- Create: `src/components/history/history-list.tsx`
- Create: `src/components/history/history-card.tsx`
- Create: `src/components/history/history-search.tsx`

Build the history page — lists saved prompts with search, filter by model/format, favorites toggle. Each card shows title, input preview, model badge, format badge, timestamp, favorite star, and delete button.

**Step 1:** Create HistoryCard component
**Step 2:** Create HistorySearch with text input + model/format filters
**Step 3:** Create HistoryList that reads from Zustand store and renders filtered results
**Step 4:** Create the history page
**Step 5:** Verify — generate a prompt, save it, navigate to /history, see it listed
**Step 6:** Commit

```bash
git add .
git commit -m "feat: add history page with search, filtering, and favorites"
```

---

## Phase 5: Auth & Settings (Tasks 16-18)

### Task 16: Supabase Auth Integration

**Files:**
- Create: `src/components/auth/auth-button.tsx`
- Create: `src/app/auth/callback/route.ts`
- Create: `src/hooks/use-user.ts`

Implement OAuth sign-in with GitHub and Google. AuthButton shows "Sign In" when logged out, shows avatar + dropdown when logged in. The callback route handles the OAuth redirect.

**Step 1:** Create the auth callback route handler
**Step 2:** Create the `useUser` hook (reads Supabase session)
**Step 3:** Create AuthButton with sign-in/sign-out dropdown
**Step 4:** Wire AuthButton into the Header
**Step 5:** Commit

```bash
git add .
git commit -m "feat: add Supabase auth with GitHub and Google OAuth"
```

---

### Task 17: Settings Page

**Files:**
- Create: `src/app/settings/page.tsx`
- Create: `src/components/settings/api-key-settings.tsx`
- Create: `src/components/settings/preferences-settings.tsx`

Build the settings page with two sections:
1. **API Key Management** — view masked key, update, clear, toggle server-side storage
2. **Preferences** — default model, default format, theme selection

**Step 1-3:** Create component files
**Step 4:** Verify settings persist after page refresh
**Step 5:** Commit

```bash
git add .
git commit -m "feat: add settings page with API key management and preferences"
```

---

### Task 18: Docs Page

**Files:**
- Create: `src/app/docs/page.tsx`

Build a simple docs page explaining:
- What ClaudeForge does
- How to get an API key
- The 9 output formats explained
- Parameter guide (thinking, effort, max tokens)
- Tips for writing good prompts

Static content, no API calls. Can reference the main Claude Prompt Engineering Guide repo.

**Step 1:** Create the docs page with MDX-like content
**Step 2:** Commit

```bash
git add .
git commit -m "feat: add docs page with format guide and parameter reference"
```

---

## Phase 6: Polish & Deploy (Tasks 19-21)

### Task 19: Animations & Transitions

**Files:**
- Modify: various components

Add Framer Motion animations:
- Page transitions (fade in)
- Output panel slide-up on generation
- Format tab switch animation
- Skeleton loading state during generation
- Toast notifications with slide-in

**Step 1-3:** Add animations to each component
**Step 4:** Verify smooth 60fps animations
**Step 5:** Commit

```bash
git add .
git commit -m "feat: add Framer Motion animations and loading states"
```

---

### Task 20: SEO, Metadata, & Accessibility

**Files:**
- Modify: `src/app/layout.tsx` (metadata)
- Create: `src/app/opengraph-image.tsx` (OG image)
- Create: `public/favicon.ico`

Add Next.js metadata, OpenGraph tags, semantic HTML, ARIA labels, keyboard navigation, and focus management.

**Step 1:** Add metadata to layout.tsx
**Step 2:** Create OG image
**Step 3:** Audit keyboard navigation and ARIA labels
**Step 4:** Run Lighthouse, target 90+ on all metrics
**Step 5:** Commit

```bash
git add .
git commit -m "feat: add SEO metadata, OG image, and accessibility improvements"
```

---

### Task 21: Vercel Deployment & README

**Files:**
- Create: `vercel.json` (if needed)
- Create: `README.md`

**Step 1:** Create README with project description, screenshots placeholder, setup instructions, tech stack, contributing guide
**Step 2:** Push to GitHub
**Step 3:** Connect to Vercel, configure environment variables
**Step 4:** Deploy and verify production build
**Step 5:** Commit

```bash
git add .
git commit -m "docs: add README and deployment configuration"
```

---

## Summary

| Phase | Tasks | Description |
|---|---|---|
| **1. Scaffolding** | 1-3 | Next.js project, deps, types, constants |
| **2. Data Layer** | 4-6 | Skill registry, Zustand stores, Supabase client |
| **3. Engine** | 7-9 | Meta-prompt builder, format converter, streaming API |
| **4. UI** | 10-15 | Layout, config bar, input, output, home page, history |
| **5. Auth** | 16-18 | Supabase auth, settings page, docs page |
| **6. Polish** | 19-21 | Animations, SEO, deployment |

**Total:** 21 tasks, estimated 3-5 days of focused implementation.

**Key Decision Points (where user input matters):**
- Task 7: The meta-prompt wording (the "secret sauce" of ClaudeForge)
- Task 8: Format conversion templates (each format's structural rules)
- Task 10: Visual design details (exact colors, spacing, typography)

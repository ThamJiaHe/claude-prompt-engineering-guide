# Creating Motion Graphics Videos with Claude Code + Remotion

A practical guide to making programmatic videos using Claude Code and the Remotion framework.

> **Last Updated: February 4, 2026** | Covers Remotion Skills (Jan 2026), Claude Code v2.1.x, and real-world workflow patterns

---

## Table of Contents

1. [What This Guide Covers](#what-this-guide-covers)
2. [Prerequisites and Setup](#prerequisites-and-setup)
3. [Remotion Core Concepts](#remotion-core-concepts)
4. [Claude Code + Remotion Workflow](#claude-code--remotion-workflow)
5. [Prompt Templates for Common Videos](#prompt-templates-for-common-videos)
6. [Code Examples](#code-examples)
7. [Troubleshooting and Common Issues](#troubleshooting-and-common-issues)
8. [Resources and Next Steps](#resources-and-next-steps)

---

## What This Guide Covers

Remotion is an open-source framework that turns React components into videos. You write TypeScript code. Remotion renders it frame-by-frame into an MP4 file. No timeline editor. No drag-and-drop. Just code.

In January 2026, Remotion released **Agent Skills** for Claude Code. This lets you describe a video in plain English and have Claude write the React code for you. The skill went viral — 13 million views in one week on X.

This guide walks through the full workflow: setup, core concepts, prompt patterns, code examples, and troubleshooting. By the end, you will be able to create motion graphics videos using Claude Code without writing React code yourself.

### Who This Guide Is For

- Developers who use Claude Code and want to make videos
- Content creators who are comfortable with the terminal
- Anyone curious about programmatic video generation

### What You Will Build

- Text animations (titles, lower thirds, kinetic typography)
- Data visualizations (animated charts, counters)
- Social media content (short loops, story templates)
- Explainer sequences (step-by-step reveals, diagram builds)

---

## Prerequisites and Setup

### Requirements

| Requirement | Details |
|-------------|---------|
| **Node.js** | v16 or later (v20+ recommended) |
| **Claude Code** | Paid subscription required |
| **Remotion** | Installed via `npx create-video@latest` |
| **OS** | macOS, Linux, or Windows |
| **Hardware** | Rendering is CPU-heavy. 8+ cores recommended for speed |

### Step 1: Create a Remotion Project

Open your terminal and run:

```bash
npx create-video@latest my-video
```

When prompted:
- **Template**: Choose `Blank`
- **TailwindCSS**: Yes (recommended — makes styling easier)

Then install dependencies:

```bash
cd my-video
npm install
```

### Step 2: Install Remotion Agent Skills

This is the key step. The Agent Skills package teaches Claude Code how to use Remotion properly.

```bash
npx skills add remotion-dev/skills
```

This creates a `.claude/skills/remotion/SKILL.md` file in your project. This file is the instruction set that Claude reads when you ask it to make videos.

### Step 3: Start the Dev Preview

In one terminal:

```bash
npm run dev
```

This opens the Remotion Studio at `http://localhost:3000`. You will use this to preview your videos before rendering.

### Step 4: Start Claude Code

In a second terminal, from the same project directory:

```bash
cd my-video
claude
```

Claude Code will detect the Remotion skill and be ready to create videos.

### Project Structure After Setup

```
my-video/
├── .claude/
│   └── skills/
│       └── remotion/
│           └── SKILL.md          # Agent skill instructions
├── public/                       # Static assets (images, fonts)
├── src/
│   ├── Composition.tsx           # Your video component
│   ├── Root.tsx                  # Composition registry
│   └── index.ts                  # Entry point
├── package.json
└── remotion.config.ts            # Rendering configuration
```

### Verify the Setup

After both terminals are running, type a test prompt in Claude Code:

```
Create a simple 3-second video that shows "Hello World" text
fading in from transparent to white on a black background
```

If Claude writes a component, the Remotion Studio updates, and you see the preview — your setup is working.

---

## Remotion Core Concepts

Before prompting Claude to make videos, it helps to understand what Remotion is doing under the hood. You do not need to memorize this. But knowing the building blocks makes your prompts more effective.

### Compositions

A **Composition** is a video definition. It combines a React component with metadata like width, height, duration, and frame rate.

```tsx
<Composition
  id="MyVideo"
  durationInFrames={150}   // 5 seconds at 30fps
  fps={30}
  width={1920}
  height={1080}
  component={MyVideoComponent}
/>
```

Key properties:
- **`id`** — Name used to reference this video when rendering
- **`durationInFrames`** — Total frames. At 30fps, 150 frames = 5 seconds
- **`fps`** — Frames per second. Default is 30
- **`width` / `height`** — Video resolution in pixels

You register compositions in `src/Root.tsx`. A single project can have multiple compositions.

### Frames and Hooks

Remotion gives you two hooks to work with:

**`useCurrentFrame()`** — Returns the current frame number (starts at 0).

**`useVideoConfig()`** — Returns `{ fps, durationInFrames, width, height }`.

Every React render corresponds to one frame. Your component receives a frame number and returns what that frame should look like. Remotion calls your component once per frame and screenshots the result.

```tsx
import { useCurrentFrame, useVideoConfig } from "remotion";

export const MyVideo = () => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  return (
    <div style={{ fontSize: 60, color: "white" }}>
      Frame {frame} of {durationInFrames}
    </div>
  );
};
```

### Interpolate

The `interpolate()` function maps one range of values to another. This is how you create smooth animations.

```tsx
import { interpolate, useCurrentFrame } from "remotion";

export const FadeIn = () => {
  const frame = useCurrentFrame();

  // Frame 0 → opacity 0, Frame 30 → opacity 1
  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <div style={{ opacity, fontSize: 80, color: "white" }}>
      Hello World
    </div>
  );
};
```

The four arguments:
1. **Input value** — usually the current frame
2. **Input range** — `[start, end]` frames
3. **Output range** — `[startValue, endValue]` for your property
4. **Options** — `extrapolateLeft` and `extrapolateRight` control what happens outside the range. Use `"clamp"` to cap values at the range boundaries.

### Spring

The `spring()` function creates physics-based animations. Springs feel more natural than linear interpolation because they accelerate and decelerate like real objects.

```tsx
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

export const BounceIn = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame,
    fps,
    config: {
      mass: 1,
      stiffness: 100,
      damping: 10,
    },
  });

  return (
    <div style={{
      transform: `scale(${scale})`,
      fontSize: 80,
      color: "white",
    }}>
      Bounce!
    </div>
  );
};
```

Spring config options:
- **`mass`** — Heavier = slower. Default: 1
- **`stiffness`** — Higher = snappier. Default: 100
- **`damping`** — Higher = less bounce. Default: 10
- **`overshootClamping`** — Set to `true` to prevent overshoot

You can also use `delay` to offset when the spring starts and `durationInFrames` to stretch it to a specific length.

### Sequence

The `<Sequence>` component controls when things appear and disappear. It shifts the frame timeline for its children.

```tsx
import { Sequence, AbsoluteFill } from "remotion";

export const MyVideo = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      {/* Shows from frame 0, lasts 30 frames */}
      <Sequence durationInFrames={30}>
        <Title text="Act One" />
      </Sequence>

      {/* Shows from frame 30, lasts 60 frames */}
      <Sequence from={30} durationInFrames={60}>
        <MainContent />
      </Sequence>

      {/* Shows from frame 90 until end */}
      <Sequence from={90}>
        <Outro />
      </Sequence>
    </AbsoluteFill>
  );
};
```

Key props:
- **`from`** — The frame where the sequence starts. Default: 0
- **`durationInFrames`** — How long the sequence lasts. Default: Infinity (until video ends)

Children inside a Sequence see their own local frame count starting at 0. If a Sequence starts at frame 30, the child's `useCurrentFrame()` returns 0 at global frame 30.

### AbsoluteFill

`<AbsoluteFill>` is a layout helper. It is a `<div>` that fills the entire video frame with absolute positioning. Use it to layer elements on top of each other.

```tsx
<AbsoluteFill style={{ backgroundColor: "#000" }}>
  <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
    <h1>Centered Text</h1>
  </AbsoluteFill>
</AbsoluteFill>
```

### Rendering

To render a video to a file:

```bash
npx remotion render MyVideo out/video.mp4
```

Replace `MyVideo` with your composition ID. The output file can be `.mp4`, `.webm`, or `.gif`.

Rendering uses your CPU. More cores = faster rendering. A 30-second video with moderate animations typically renders in 1–3 minutes on modern hardware.

For still images (thumbnails, social cards):

```bash
npx remotion still MyVideo out/thumbnail.png
```

---

## Claude Code + Remotion Workflow

This section covers the practical workflow of using Claude Code to generate videos.

### The Basic Loop

The workflow is a conversation. You describe what you want. Claude writes the code. You preview it. You refine.

```
1. Describe the video to Claude Code
2. Claude writes/modifies the React component
3. Remotion Studio hot-reloads the preview
4. Watch the preview
5. Tell Claude what to change
6. Repeat until satisfied
7. Render to MP4
```

### Good Prompts vs Bad Prompts

The quality of your video depends on the quality of your prompt. Be specific about what you want to see on screen.

**Bad prompt:**
```
Make a cool intro video
```

**Good prompt:**
```
Create a 5-second intro video at 1920x1080, 30fps.

Background: dark navy (#0a0a2e) with subtle gradient to black.
Text: "ACME CORP" in white, bold, 80px, centered.
Animation: Text starts invisible, fades in over 1 second,
then scales up slightly (1.0 to 1.05) over the next 2 seconds.
At 3.5 seconds, a thin white horizontal line draws in from
the center outward beneath the text.
```

**Why the second prompt works better:**
- Specific colors (hex codes)
- Exact timing (seconds, not vague)
- Clear animation sequence (what happens when)
- Defined resolution and frame rate

### Iteration Tips

After the first draft renders, you can refine with follow-up prompts:

```
Make the text fade in faster — 0.5 seconds instead of 1 second
```

```
Change the background to a dark gradient from #1a1a2e to #0a0a1a
```

```
Add a 0.3 second delay before the line animation starts
```

```
The text is too small on mobile. Increase font size to 100px
```

Keep each change small and specific. Claude handles incremental changes better than complete rewrites.

### Working With Multiple Scenes

For longer videos, break your work into separate compositions. Ask Claude to create one scene at a time:

```
Create a composition called "Intro" — 3 seconds,
shows the company logo fading in with a spring bounce

Create a composition called "Features" — 10 seconds,
shows 3 feature bullets appearing one by one from the left

Create a composition called "Outro" — 3 seconds,
shows a call-to-action text with website URL
```

Then combine them in a main composition using `<Sequence>`.

### Rendering Workflow

After you are satisfied with the preview:

```bash
# Render a specific composition
npx remotion render Intro out/intro.mp4

# Render all compositions
npx remotion render Main out/final.mp4
```

For social media formats, adjust the composition dimensions:

| Platform | Resolution | Aspect Ratio |
|----------|-----------|--------------|
| YouTube | 1920x1080 | 16:9 |
| Instagram Reels | 1080x1920 | 9:16 |
| TikTok | 1080x1920 | 9:16 |
| Twitter/X | 1280x720 | 16:9 |
| Square (Instagram) | 1080x1080 | 1:1 |

Tell Claude the target platform and it will set the right dimensions.

---

## Prompt Templates for Common Videos

These templates are copy-paste starting points. Replace the bracketed values with your content.

### Template 1: Text Animation Intro

```
Create a [duration]-second video at [width]x[height], 30fps.

Background: solid [color/hex].
Text: "[YOUR TEXT]" in [color], [weight], [size]px, centered.
Font: sans-serif (or specify a Google Font).

Animation sequence:
- 0.0s: Text invisible (opacity 0, scale 0.8)
- 0.0–0.8s: Text fades in and scales to 1.0 using spring animation
- 0.8–[duration-1]s: Text holds steady
- [duration-1]s–[duration]s: Text fades out to opacity 0
```

### Template 2: Animated Counter / Number Reveal

```
Create a [duration]-second video at 1920x1080, 30fps.

Background: [color].
Display a large number counter in the center.
The number should count from [start] to [end].

Animation:
- Use interpolate to smoothly count the number over [duration] seconds
- Display the number with [formatting: commas, dollar sign, percentage, etc.]
- Number font size: [size]px, color: [color], font-weight: bold
- Add a label below: "[label text]" in [size]px, [color]
```

### Template 3: List / Bullet Point Reveal

```
Create a [duration]-second video at 1920x1080, 30fps.

Background: [color].
Title: "[TITLE]" at the top, [size]px, [color], bold.

Items to reveal one by one:
1. "[Item 1]"
2. "[Item 2]"
3. "[Item 3]"

Animation:
- Title appears first with a spring scale (0 to 1) over 0.5s
- Each item slides in from the left with 0.4s stagger between items
- Use spring animation with damping: 15, stiffness: 120
- Items appear at left: 10% margin, vertically spaced evenly
- Each item has a small colored bullet/icon before the text
```

### Template 4: Social Media Story / Reel

```
Create a 15-second video at 1080x1920 (portrait), 30fps.

Background: gradient from [color1] to [color2], top to bottom.

Scene 1 (0–3s): Large hook text "[HOOK LINE]"
  centered, spring bounce in, white, 72px bold.

Scene 2 (3–8s): Three key points appear one by one:
  - "[Point 1]" at 3.5s
  - "[Point 2]" at 5.0s
  - "[Point 3]" at 6.5s
  Each slides up from below with spring animation.

Scene 3 (8–12s): Supporting visual or stat.
  "[BIG NUMBER]" scales in with spring, then
  "[context text]" fades in below.

Scene 4 (12–15s): Call to action.
  "[CTA TEXT]" pulses gently (scale 1.0 to 1.03, looping).
  "[handle/url]" fades in below.
```

### Template 5: Progress Bar / Timeline Animation

```
Create a [duration]-second video at 1920x1080, 30fps.

Background: [color].
Title: "[TITLE]" at top, centered, [size]px.

Show a horizontal progress bar:
- Bar background: [light color], height: 20px, width: 80%
- Bar fill: [accent color], animates from 0% to 100% over [duration-2] seconds
- Percentage label above the bar, updating in real time: "0%" to "100%"
- Use interpolate with clamp for smooth fill

Below the bar, show milestone labels at 25%, 50%, 75%, 100% marks.
Each label fades in when the bar reaches its position.
```

### Template 6: Logo Reveal

```
Create a [duration]-second video at 1920x1080, 30fps.

Background: [color].
Logo: Use the image at public/logo.png, centered.

Animation:
- 0.0–0.3s: Logo invisible
- 0.3–1.0s: Logo scales from 0.5 to 1.0 with spring (stiffness: 80, damping: 12)
- 1.0–1.3s: Tagline "[TAGLINE]" fades in below logo
- Hold until [duration-0.5]s
- [duration-0.5]s–end: Everything fades out
```

---

## Code Examples

These are complete, working examples you can copy into your Remotion project. Each one demonstrates a different technique.

### Example 1: Kinetic Typography

A sentence that reveals word by word with staggered spring animations.

```tsx
import { AbsoluteFill, spring, useCurrentFrame, useVideoConfig } from "remotion";

const words = ["Build", "Videos", "With", "Code"];

export const KineticText: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0a0a0a",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "row",
        gap: 20,
      }}
    >
      {words.map((word, i) => {
        const delay = i * 8;
        const scale = spring({
          frame: frame - delay,
          fps,
          config: { damping: 12, stiffness: 200, mass: 0.5 },
        });
        const opacity = Math.min(1, scale);

        return (
          <span
            key={word}
            style={{
              fontSize: 90,
              fontWeight: "bold",
              color: "#ffffff",
              transform: `scale(${scale})`,
              opacity,
              display: "inline-block",
            }}
          >
            {word}
          </span>
        );
      })}
    </AbsoluteFill>
  );
};
```

**What this does:** Each word pops in with a bouncy spring effect. The `delay` offsets each word by 8 frames (about 0.27 seconds at 30fps). The spring overshoots slightly before settling, giving a playful feel.

Register it in `src/Root.tsx`:
```tsx
<Composition
  id="KineticText"
  component={KineticText}
  durationInFrames={90}
  fps={30}
  width={1920}
  height={1080}
/>
```

### Example 2: Animated Data Bar Chart

A horizontal bar chart where bars grow from zero to their target width.

```tsx
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const data = [
  { label: "React", value: 85, color: "#61dafb" },
  { label: "TypeScript", value: 72, color: "#3178c6" },
  { label: "Node.js", value: 68, color: "#68a063" },
  { label: "Python", value: 90, color: "#ffd43b" },
];

const maxValue = Math.max(...data.map((d) => d.value));

export const BarChart: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#1a1a2e",
        justifyContent: "center",
        padding: 80,
      }}
    >
      <h1 style={{ color: "#fff", fontSize: 48, marginBottom: 40 }}>
        Skills Breakdown
      </h1>
      {data.map((item, i) => {
        const delay = i * 10;
        const progress = spring({
          frame: frame - delay,
          fps,
          config: { damping: 15, stiffness: 80 },
        });
        const width = interpolate(
          progress,
          [0, 1],
          [0, (item.value / maxValue) * 100]
        );

        return (
          <div key={item.label} style={{ marginBottom: 24 }}>
            <div
              style={{
                color: "#ccc",
                fontSize: 24,
                marginBottom: 8,
              }}
            >
              {item.label}
            </div>
            <div
              style={{
                height: 36,
                backgroundColor: "#2a2a3e",
                borderRadius: 8,
                overflow: "hidden",
              }}
            >
              <div
                style={{
                  height: "100%",
                  width: `${width}%`,
                  backgroundColor: item.color,
                  borderRadius: 8,
                }}
              />
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
```

**What this does:** Each bar grows outward using a spring animation. The stagger delay means bars appear one after another. The spring prevents a robotic linear animation — bars overshoot slightly and settle.

### Example 3: Multi-Scene Video With Sequences

A complete video with intro, main content, and outro scenes.

```tsx
import {
  AbsoluteFill,
  Sequence,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const Intro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const scale = spring({ frame, fps, config: { damping: 12 } });
  const opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0f0f23",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          fontSize: 72,
          fontWeight: "bold",
          color: "#fff",
          transform: `scale(${scale})`,
          opacity,
        }}
      >
        Weekly Report
      </div>
    </AbsoluteFill>
  );
};

const StatCard: React.FC<{ label: string; value: string }> = ({
  label,
  value,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = spring({ frame, fps, config: { damping: 14 } });

  return (
    <div
      style={{
        transform: `translateY(${interpolate(enter, [0, 1], [40, 0])}px)`,
        opacity: enter,
        backgroundColor: "#1e1e3a",
        padding: 32,
        borderRadius: 16,
        textAlign: "center",
        minWidth: 200,
      }}
    >
      <div style={{ fontSize: 48, fontWeight: "bold", color: "#6c63ff" }}>
        {value}
      </div>
      <div style={{ fontSize: 20, color: "#aaa", marginTop: 8 }}>{label}</div>
    </div>
  );
};

const MainContent: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0f0f23",
        justifyContent: "center",
        alignItems: "center",
        gap: 40,
        flexDirection: "row",
      }}
    >
      <Sequence from={0}>
        <StatCard label="Users" value="12,847" />
      </Sequence>
      <Sequence from={10}>
        <StatCard label="Revenue" value="$84.2K" />
      </Sequence>
      <Sequence from={20}>
        <StatCard label="Growth" value="+23%" />
      </Sequence>
    </AbsoluteFill>
  );
};

const Outro: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0f0f23",
        justifyContent: "center",
        alignItems: "center",
        opacity,
      }}
    >
      <div style={{ fontSize: 36, color: "#888" }}>acme.com/dashboard</div>
    </AbsoluteFill>
  );
};

export const WeeklyReport: React.FC = () => {
  return (
    <AbsoluteFill>
      <Sequence durationInFrames={60}>
        <Intro />
      </Sequence>
      <Sequence from={60} durationInFrames={90}>
        <MainContent />
      </Sequence>
      <Sequence from={150}>
        <Outro />
      </Sequence>
    </AbsoluteFill>
  );
};
```

**What this does:** Three scenes play in order. The intro bounces in a title. The main content staggers three stat cards sliding up. The outro fades in a URL. Total duration: about 7 seconds at 30fps (210 frames).

### Example 4: Looping Pulse Animation (Social Media)

A short looping animation for social media posts.

```tsx
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";

export const PulseLoop: React.FC = () => {
  const frame = useCurrentFrame();

  // Creates a smooth 0 → 1 → 0 pulse over 60 frames (2 seconds)
  const pulse = Math.sin((frame / 60) * Math.PI * 2) * 0.5 + 0.5;
  const scale = interpolate(pulse, [0, 1], [1.0, 1.08]);
  const glowOpacity = interpolate(pulse, [0, 1], [0.3, 0.8]);

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#0a0a0a",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      {/* Glow behind text */}
      <div
        style={{
          position: "absolute",
          width: 300,
          height: 300,
          borderRadius: "50%",
          backgroundColor: "#6c63ff",
          opacity: glowOpacity,
          filter: "blur(80px)",
        }}
      />
      <div
        style={{
          fontSize: 64,
          fontWeight: "bold",
          color: "#fff",
          transform: `scale(${scale})`,
          zIndex: 1,
        }}
      >
        LIVE NOW
      </div>
    </AbsoluteFill>
  );
};
```

**What this does:** Uses `Math.sin()` instead of spring for a continuously looping pulse. The text scales gently while a blurred glow circle behind it breathes. Set the composition to 60 frames and it loops seamlessly.

---

## Troubleshooting and Common Issues

### "Skill not found" or Claude does not know Remotion

**Cause:** The skill was not installed, or Claude Code was started before the skill was added.

**Fix:**
```bash
# Re-install the skill
npx skills add remotion-dev/skills

# Restart Claude Code (exit and re-open)
exit
claude
```

As of January 2026, newly installed skills require a Claude Code restart to take effect. There is no hot-reload for skills yet.

### Preview does not update in Remotion Studio

**Cause:** Hot Module Replacement (HMR) occasionally fails after large code changes.

**Fix:**
1. Save the file manually
2. If still stuck, stop and restart `npm run dev`
3. Check the terminal for compilation errors

### Rendering fails with "Composition not found"

**Cause:** The composition ID in the render command does not match the `id` prop in `src/Root.tsx`.

**Fix:**
```bash
# Check available compositions
npx remotion compositions

# Use the exact ID from the list
npx remotion render "ExactCompositionId" out/video.mp4
```

### Animations look choppy or flickering

**Cause:** Animations driven by something other than `useCurrentFrame()` — like CSS transitions or `setTimeout` — do not work in Remotion. Remotion renders each frame independently. There is no continuous time between frames.

**Fix:** Always drive animations with `useCurrentFrame()`, `interpolate()`, or `spring()`. Never use:
- CSS `transition` or `animation`
- `setTimeout` / `setInterval`
- `requestAnimationFrame`

### Elements positioned wrong or overlapping

**Cause:** When Claude generates complex layouts with many animated elements, positioning can break down.

**Fix:**
1. Keep it simple. Fewer elements = fewer positioning issues
2. Use `<AbsoluteFill>` with flexbox for centering
3. Ask Claude to fix specific positioning: "Move the subtitle 40px lower"
4. If a layout is too complex, break it into separate `<Sequence>` scenes

### Render is slow

**Cause:** Remotion rendering is CPU-bound. Complex scenes with many elements render slower.

**Fix:**
- Close other applications during rendering
- Use `--concurrency` flag to control parallel rendering:
  ```bash
  npx remotion render MyVideo out/video.mp4 --concurrency=8
  ```
- Reduce resolution for drafts: render at 720p first, then 1080p for final
- Remotion supports parallel rendering across CPU cores by default

### Fonts not showing in render

**Cause:** Custom fonts load asynchronously. They might not be ready when Remotion renders a frame.

**Fix:** Use the `@remotion/google-fonts` package:
```bash
npm install @remotion/google-fonts
```

Then import the font in your component:
```tsx
import { loadFont } from "@remotion/google-fonts/Inter";
const { fontFamily } = loadFont();
```

Use `fontFamily` in your styles. Remotion will wait for the font to load before rendering each frame.

### Images not appearing

**Cause:** Using `<img>` tags. Remotion needs to know when images finish loading.

**Fix:** Use Remotion's `<Img>` component instead:
```tsx
import { Img } from "remotion";

<Img src="https://example.com/photo.jpg" style={{ width: 400 }} />
```

For local images, place them in the `public/` folder and reference with:
```tsx
import { staticFile, Img } from "remotion";

<Img src={staticFile("logo.png")} />
```

---

## Resources and Next Steps

### Official Documentation

| Resource | URL |
|----------|-----|
| Remotion Docs | [remotion.dev/docs](https://www.remotion.dev/docs/) |
| Claude Code + Remotion | [remotion.dev/docs/ai/claude-code](https://www.remotion.dev/docs/ai/claude-code) |
| Starter Templates | [remotion.dev/templates](https://www.remotion.dev/templates/) |
| Spring Visualizer | [springs.remotion.dev](https://springs.remotion.dev/) |
| Timing Editor | [remotion.dev/timing-editor](https://www.remotion.dev/timing-editor) |
| API Reference | [remotion.dev/docs/api](https://www.remotion.dev/docs/api) |

### Community Resources

| Resource | URL |
|----------|-----|
| Remotion GitHub | [github.com/remotion-dev/remotion](https://github.com/remotion-dev/remotion) |
| Claude Remotion Kickstart | [github.com/jhartquist/claude-remotion-kickstart](https://github.com/jhartquist/claude-remotion-kickstart) |
| Remotion Discord | [remotion.dev/discord](https://remotion.dev/discord) |

### Tutorials and Guides

- [Making Videos with Code: Complete Guide](https://medium.com/@creativeaininja/making-videos-with-code-the-complete-guide-to-remotion-and-claude-code-82892e21d022) — Medium, Jan 2026
- [Claude Code Can Make Videos Now](https://alexmcfarland.substack.com/p/claude-code-can-make-videos-now-full) — Substack guide
- [Remotion Skills for Education Videos](https://www.x-pilot.ai/blog/remotion-claude-skill-education-video-complete-guide-2026) — X-Pilot, 2026
- [How to Create Professional Videos with Claude Code](https://work.randyellis.design/blog/create-professional-videos-claude-code-guide) — Rand Ellis
- [Remotion Turned Claude Code into a Video Production Tool](https://jpcaparas.medium.com/remotion-turned-claude-code-into-a-video-production-tool-f83fd761b158) — JP Caparas, Jan 2026

### What to Try Next

1. **Batch rendering** — Generate 50 variations of a template from a JSON dataset. See [remotion.dev/docs/dataset-render](https://www.remotion.dev/docs/dataset-render)
2. **3D graphics** — Use `@remotion/three` for React Three Fiber integration
3. **Cloud rendering** — Use Remotion Lambda to render videos serverlessly on AWS
4. **Audio** — Add background music and sound effects with Remotion's `<Audio>` component
5. **Captions** — Generate and overlay captions programmatically

### Licensing

Remotion uses a custom license:
- **Free** for individuals, non-profits, and companies with 3 or fewer employees
- **Commercial license required** for companies with 4+ employees
- The Skills feature has no additional cost beyond base Remotion licensing
- Check [remotion.dev/license](https://remotion.dev/license) for current terms

---

## Related Guides

- [Claude Code Guide](./claude-code-guide.md) — Full Claude Code reference
- [Skills Guide](./skills-guide.md) — Working with Claude Code skills
- [MCP Integration](./mcp-integration.md) — External tool connections

---

**Last Updated:** February 4, 2026
**Version:** 1.0.0
**Status:** Production Ready

### Research Sources

- [Remotion Official Docs](https://www.remotion.dev/docs/)
- [Remotion + Claude Code Docs](https://www.remotion.dev/docs/ai/claude-code)
- [Remotion GitHub](https://github.com/remotion-dev/remotion)
- [Remotion Skills Guide (gaga.art)](https://gaga.art/blog/remotion-skills/)
- [Claude Code Remotion Kickstart (GitHub)](https://github.com/jhartquist/claude-remotion-kickstart)
- [Making Videos with Code (Medium)](https://medium.com/@creativeaininja/making-videos-with-code-the-complete-guide-to-remotion-and-claude-code-82892e21d022)
- [Apidog: Claude Code + Remotion Guide](https://apidog.com/blog/claude-code-remotion/)
- [DEV Community: Claude + Remotion](https://dev.to/mayu2008/new-clauderemotion-to-create-amazing-videos-using-ai-37bp)

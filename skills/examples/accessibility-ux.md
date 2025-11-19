---
name: "Accessibility & UX"
description: "Build WCAG 2.1 AA compliant interfaces with keyboard navigation, error prevention, and screen reader support. Apply when designing UI, building forms, implementing admin flows, or testing accessibility."
allowed-tools: Read, Write, Edit
version: 2.0.0
---

# Accessibility & UX

Systematic accessibility implementation ensuring usable interfaces for all users.

## Overview

This Skill enforces a **mandatory 5-step accessibility audit workflow**:
1. Automated Testing (axe, Lighthouse, Pa11y)
2. Keyboard Navigation (no traps)
3. Screen Reader Testing (VoiceOver/NVDA)
4. Color & Contrast (4.5:1 ratio)
5. Manual Verification (semantic HTML, forms, errors)

Apply when designing UI, building forms, or implementing admin flows.

## Accessibility Audit Workflow

**Before deploying UI to production**:

### Step 1: Automated Testing

```bash
# Axe DevTools browser extension
# Lighthouse in Chrome DevTools (Ctrl+Shift+I)
# Pa11y CLI
npm install -g pa11y
pa11y https://yoursite.com
```

**Checklist**:
- [ ] Axe DevTools shows no errors
- [ ] Lighthouse accessibility score ≥ 90
- [ ] Pa11y reports no critical issues

### Step 2: Keyboard Navigation

Test **without mouse**, using only Tab, Enter, Escape, Arrow keys.

```tsx
// ✅ GOOD: Full keyboard support
export function UserList() {
  const [selected, setSelected] = useState(0);
  const users = useUsers();

  const handleKeyDown = (e: KeyboardEvent) => {
    switch (e.key) {
      case 'ArrowDown':
        setSelected(Math.min(selected + 1, users.length - 1));
        break;
      case 'ArrowUp':
        setSelected(Math.max(selected - 1, 0));
        break;
      case 'Enter':
      case ' ':
        handleSelect(users[selected]);
        break;
      case 'Escape':
        setSelected(-1);
        break;
    }
  };

  return (
    <div onKeyDown={handleKeyDown} role="listbox">
      {users.map((user, idx) => (
        <div
          role="option"
          aria-selected={idx === selected}
          tabIndex={idx === selected ? 0 : -1}
          onClick={() => handleSelect(user)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ' ') {
              handleSelect(user);
            }
          }}
        >
          {user.name}
        </div>
      ))}
    </div>
  );
}

// ❌ BAD: No keyboard support
<div onClick={() => deleteUser()}>Delete</div>  // Click-only
```

**Checklist**:
- [ ] Tab through entire interface
- [ ] No keyboard traps (can't escape focused element)
- [ ] All interactions work with Enter/Space
- [ ] Focus management visible (highlight current element)
- [ ] **U-2 (SHOULD)**: Admin features keyboard accessible

### Step 3: Screen Reader Testing

Test with VoiceOver (macOS: Cmd+F5) or NVDA (Windows: free).

```tsx
// ✅ GOOD: Screen reader friendly
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<main id="main">
  <h1>Dashboard</h1>
  <section aria-labelledby="stats-heading">
    <h2 id="stats-heading">Statistics</h2>
  </section>
</main>

// ❌ BAD: Not screen reader friendly
<div className="nav">
  <div><a href="/">Home</a></div>
  <div><a href="/about">About</a></div>
</div>

<div>
  <div style={{ fontSize: '2em' }}>Dashboard</div>
</div>
```

**Checklist**:
- [ ] All content announced by screen reader
- [ ] Headings properly announce hierarchy
- [ ] Form inputs have labels
- [ ] Images have alt text
- [ ] Status updates announced (aria-live)
- [ ] Errors announced as alerts

### Step 4: Color & Contrast

**4.5:1 contrast ratio minimum** (WCAG AA):

```css
/* ✅ GOOD: High contrast */
.button {
  background-color: #000;  /* Black */
  color: #fff;             /* White */
  /* Contrast ratio: 21:1 */
}

.text {
  background-color: #fff;
  color: #333;             /* Dark gray */
  /* Contrast ratio: 12.63:1 */
}

/* ❌ BAD: Low contrast */
.button {
  background-color: #f0f0f0;  /* Light gray */
  color: #aaa;                /* Medium gray */
  /* Contrast ratio: 3.51:1 - FAILS */
}
```

### Use Color + Text Indicator

```tsx
// ✅ GOOD: Color + text/icon
export function StatusBadge({ status }) {
  return (
    <span
      style={{ color: status === 'error' ? 'red' : 'green' }}
      role="status"
    >
      {status === 'error' ? '✗ Error' : '✓ Valid'}
    </span>
  );
}

// ❌ BAD: Color only
export function StatusBadge({ status }) {
  return (
    <div
      style={{
        width: '20px',
        height: '20px',
        backgroundColor: status === 'error' ? 'red' : 'green'
      }}
    />
  );
}
```

**Checklist**:
- [ ] Text contrast 4.5:1 (large text 3:1)
- [ ] Color not only indicator
- [ ] Tested with colorblindness simulator

### Step 5: Manual Verification

#### Semantic HTML

```tsx
// ✅ GOOD: Semantic structure
<header>
  <nav>Navigation items</nav>
</header>

<main>
  <article>
    <h1>Article Title</h1>
    <p>Content</p>
  </article>
</main>

<aside>
  <h2>Related</h2>
</aside>

<footer>Copyright</footer>

// ❌ BAD: All divs
<div>
  <div>Navigation</div>
</div>

<div>
  <div>
    <div>Article Title</div>
    <p>Content</p>
  </div>
</div>
```

#### Form Accessibility

```tsx
// ✅ GOOD: Complete form accessibility
<div>
  <label htmlFor="email">Email Address</label>
  <input
    id="email"
    type="email"
    value={value}
    onChange={handleChange}
    aria-invalid={!!error}
    aria-describedby={error ? 'email-error' : undefined}
  />
  {error && (
    <p id="email-error" role="alert" className="error">
      {error}
    </p>
  )}
</div>

// ❌ BAD: Missing label
<input type="email" placeholder="Email" />

// ❌ BAD: Unassociated error
<input type="email" value={email} />
Error: Invalid email
```

#### Error Prevention & Recovery

```tsx
// ✅ GOOD: U-5 - Confirmation required
export function DeleteUserButton({ userId }) {
  const [showConfirm, setShowConfirm] = useState(false);

  if (showConfirm) {
    return (
      <div role="alertdialog">
        <p>Delete user? This cannot be undone.</p>
        <button onClick={() => deleteUser(userId)}>
          Yes, Delete
        </button>
        <button onClick={() => setShowConfirm(false)}>
          Cancel
        </button>
      </div>
    );
  }

  return (
    <button onClick={() => setShowConfirm(true)} className="danger">
      Delete User
    </button>
  );
}

// ✅ GOOD: U-6 - Undo available
export async function deleteUser(userId: UserId) {
  await db.users.softDelete(userId);  // Don't hard delete
  
  showNotification({
    message: 'User deleted',
    action: 'Undo',
    onAction: () => restoreUser(userId),
    duration: 5000  // 5 seconds to undo
  });
}

// ❌ BAD: Direct deletion
<button onClick={() => deleteUser()}>Delete</button>
```

## Anti-Patterns

```tsx
// ❌ BAD: No ARIA labels
<button>✕</button>

// ❌ BAD: Skip heading levels
<h1>Title</h1>
<h3>Subtitle</h3>  {/* Skipped h2 */}

// ❌ BAD: No alt text
<img src="user-avatar.jpg" />

// ❌ BAD: Placeholder as label
<input placeholder="Email" />

// ❌ BAD: No keyboard support
<div onClick={handleClick} role="button">
  Click me
</div>

// ❌ BAD: Tab trap
<div onKeyDown={(e) => {
  if (e.key === 'Tab') {
    e.preventDefault();  // Prevents leaving modal
  }
}}>

// ❌ BAD: Using divs as buttons
<div onClick={deleteUser}>Delete</div>
// Should be: <button onClick={deleteUser}>Delete</button>
```

## WCAG 2.1 AA Standards

### U-1 (MUST): WCAG 2.1 AA Compliant

**Perceivable**:
- Text alternatives for images
- Captions for videos
- Distinguishable: 4.5:1 contrast

**Operable**:
- Keyboard accessible
- No keyboard traps
- Sufficient time (no auto-advancing)

**Understandable**:
- Readable language
- Predictable navigation
- Error messages and recovery

**Robust**:
- Valid HTML
- Compatible with assistive tech

## Keyboard Navigation Checklist

- [ ] **U-2 (SHOULD)**: Keyboard navigation works
- [ ] No keyboard traps (can't escape focused element)
- [ ] Tab order logical (left-to-right, top-to-bottom)
- [ ] Focus indicator visible
- [ ] All interactions (Enter, Space, Escape, Arrows) work
- [ ] Skip links available for navigation

## Admin Portal Accessibility

- [ ] **AP-6 (MUST)**: Admin portal WCAG 2.1 AA
- [ ] **AP-7 (SHOULD)**: Admin features keyboard accessible

## Form Accessibility

- [ ] Labels associated with inputs (htmlFor)
- [ ] Error messages announce to screen readers
- [ ] Required fields marked
- [ ] Validation feedback before submission
- [ ] Submit button descriptive ("Create User" not "OK")

## Destructive Actions

- [ ] **U-5 (MUST)**: Destructive actions need confirmation
- [ ] **U-6 (SHOULD)**: Undo available for destructive actions
- [ ] **S-7 (MUST)**: No accidental deletions

## Testing Tools

```bash
# Axe DevTools
# Browser extension for Chrome, Firefox, Safari

# Lighthouse
# Built into Chrome DevTools (Ctrl+Shift+I → Lighthouse)

# Pa11y CLI
npm install -g pa11y
pa11y https://example.com

# WAVE
# https://wave.webaim.org/extension/

# Color contrast checker
# https://webaim.org/resources/contrastchecker/

# Screen readers
# macOS: VoiceOver (Cmd+F5)
# Windows: NVDA (free) or JAWS (paid)
```

## Verification Before Deployment

Before deploying UI:

- [ ] Automated tests pass (axe, Lighthouse, Pa11y)
- [ ] Keyboard navigation works (no traps)
- [ ] Screen reader tested
- [ ] 4.5:1 contrast ratio verified
- [ ] All forms labeled
- [ ] Semantic HTML used
- [ ] Images have alt text
- [ ] Error messages clear
- [ ] Status updates announced
- [ ] Destructive actions confirmed
- [ ] **U-1 (MUST)**: WCAG 2.1 AA
- [ ] **AP-6 (MUST)**: Admin portal accessible

## Integration with CLAUDE.md

Enforces CLAUDE.md Section 9 & 8:
- **U-1 through U-6**: UX/accessibility
- **AP-6, AP-7, AP-10**: Admin portal accessibility

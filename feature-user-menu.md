Implement the following features.

Keep the current visual design.

Do not modify business logic, Firebase, OCR, calculations, persistence or existing workflows.

## 1. User avatar

Replace the current "MP" avatar.

Display the first two initials derived from the logged user's email.

Examples:

gustavomarsan@gmail.com → GM

john.smith@gmail.com → JS

maria@gmail.com → MA

Ignore dots, underscores and numbers.

Keep the current fallback if initials cannot be determined.

---

## 2. User menu

Clicking the avatar should open a small dropdown menu.

Menu items:

- Sign out

Requirements:

- Open on click.
- Close when clicking outside.
- Close after selecting an option.
- Match the application's visual language.

---

## 3. Hide financial values

Add an eye icon in the application's top bar.

Clicking it should toggle between visible and hidden values.

When hidden:

- replace every numeric digit with an asterisk
- preserve currency symbols
- preserve separators
- preserve percentage symbols
- preserve labels

Examples:

R$ 695.673,09

↓

R$ ***.***,**

+R$ 5.608,44

↓

+R$ *.***,**

12,45%

↓

**,**

Apply to every screen.

Apply to:

- cards
- tables
- charts
- tooltips
- summaries
- projections
- historical values

Persist the selected state during the current browser session.

Default state: visible.

---

Validate HTML, CSS and JavaScript before finishing.
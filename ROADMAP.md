# Implementation Roadmap

## Pass 1

### Objective

Improve clarity, accessibility, navigation, and interaction consistency without changing financial calculations, Firebase integration, persistence behavior, import formats, or stored user data.

### Expected visual impact

High. The application should immediately feel calmer, more legible, and more intentional through clearer navigation, stronger typography, larger controls, and consistent interaction states.

### Scope

- Reorganize bottom navigation into Carteira, Evolução, Projeções, and Ajustes.
- Consolidate all new-closing entry points into one unmistakable primary action.
- Establish a practical typography scale and remove critically small text.
- Replace ambiguous text glyphs with a consistent accessible icon system.
- Add accessible names and `aria-current`.
- Add semantic dialogs, focus trapping, focus restoration, and Escape dismissal.
- Bring interactive targets to at least 44×44 px where practical.
- Add reduced-motion behavior.
- Apply visible focus treatment consistently.
- Replace native confirmation dialogs with in-app confirmation sheets.
- Add an accessible textual or tabular summary for the evolution chart.
- Clarify the distinction between contribution, investment return, and total wealth variation.

### Files likely to change

- `index.html`
- A future stylesheet if CSS is extracted from `index.html`
- A future interaction script if JavaScript is extracted from `index.html`
- Optional icon assets or icon component source

### Implementation risk

Low. Most work affects presentation, semantics, and navigation wiring. The principal risks are breaking current view switching, sheet behavior, or focus flow. Firebase calls, IndexedDB records, backup formats, imports, and financial calculations should remain untouched.

## Pass 2

### Objective

Transform the home screen from a balance display into a concise portfolio narrative using the closing, contribution, and category data already available.

### Expected visual impact

Very high. This pass should create the largest improvement in perceived product value by making portfolio status, contributions, returns, and allocation understandable at a glance.

### Scope

- Redesign the home summary around total portfolio, return, contributions, net change, and last update.
- Add a compact allocation visualization derived from existing category totals.
- Show the strongest positive and negative contributors to monthly performance.
- Replace repeated card treatments with a clearer surface hierarchy.
- Standardize spacing, radii, colors, borders, and typography as reusable tokens.
- Introduce tabular numerals for financial values.
- Reserve performance green primarily for positive financial results.
- Separate portfolio content from synchronization and administrative state.
- Redesign empty states as guided sequences.
- Simplify investment rows and improve comparative scanning.

### Files likely to change

- `index.html`
- A future design-token or stylesheet file if styles are extracted
- A future dashboard-rendering script if JavaScript is extracted
- No Firebase schema or stored-data migration should be required

### Implementation risk

Low to moderate. Most metrics can be derived from existing records. The main risk is displaying a metric that differs from the application’s established contribution-adjusted performance logic. Calculation definitions should be documented and reused consistently.

## Pass 3

### Objective

Make evolution and projection features explain financial change rather than only display balances, while preserving the product’s focused personal-wealth scope.

### Expected visual impact

High. The analytical screens should feel substantially more capable and comparable to premium portfolio products, especially through interactive charts and clearer scenario presentation.

### Scope

- Add 3M, 6M, 1A, and Tudo time filters.
- Make chart points inspectable by touch, pointer, and keyboard.
- Show balance, contributions, absolute return, and percentage return for the selected point.
- Add Patrimônio, Rendimento, and Aportes chart modes.
- Visually distinguish contributions from organic performance.
- Adjust axis-label density dynamically.
- Add monthly and accumulated return summaries.
- Expose contribution-adjusted performance attribution by investment.
- Stack projection scenarios vertically on narrow screens.
- Allow adjustment of the target amount and expected monthly contribution.
- Present conservative, base, and optimistic scenarios.
- Prefer estimated ranges over false date precision where appropriate.
- Keep external benchmark data out of scope unless a reliable source is intentionally introduced.

### Files likely to change

- `index.html`
- Chart rendering and interaction logic, currently embedded in `index.html`
- Projection calculation and rendering logic, currently embedded in `index.html`
- A future chart component or module if the monolithic file is separated
- Possible financial-calculation tests if a test structure is introduced

### Implementation risk

Moderate. Interactive charts, responsive inspection, and adjustable scenarios introduce state and edge cases. New projection preferences should remain local unless a deliberate storage extension is designed. Existing closings and Firebase documents should not be mutated or reinterpreted.

## Pass 4

### Objective

Refine feedback, motion, edge cases, and brand expression after the structural and analytical improvements are stable.

### Expected visual impact

Moderate to high. This pass will not materially change the information architecture, but it should significantly improve perceived craftsmanship, responsiveness, and trust.

### Scope

- Refine motion for sheets, charts, save confirmation, and synchronization.
- Add skeleton and contextual loading states.
- Design clear offline, syncing, synced, conflict, and error states.
- Improve microcopy for OCR confidence, merge behavior, backup, and irreversible actions.
- Add restrained haptic feedback where supported.
- Introduce a subtle, consistent brand signature.
- Test compact phones, large phones, landscape, browser zoom, dynamic text, keyboard navigation, and screen readers.
- Validate color contrast.
- Test long investment names, large values, negative performance, missing months, and long histories.
- Run task-based usability testing for monthly closing, correction, import, and recovery.

### Files likely to change

- `index.html`
- A future stylesheet and interaction module if the file is separated
- Optional brand and icon assets
- Optional manifest or platform metadata if installable-app behavior is later adopted
- Test and accessibility audit files if introduced

### Implementation risk

Moderate. Individual polish changes are generally low risk, but their breadth can create inconsistent states without a stable component system. Motion, loading, and offline messaging must not interfere with Firebase synchronization or imply that data has been saved before persistence succeeds.

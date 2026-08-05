# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

An individual managing and reviewing their own investment portfolio, primarily on desktop, through periodic portfolio closings and contribution records.

## Product Purpose

Provide a private, user-controlled view of total wealth, monthly change, contributions, investment performance, allocation, history, and progress toward financial goals.

## Positioning

Meu Patrimônio separates contributions from organic investment performance while keeping the portfolio record personally controlled and understandable without brokerage-platform complexity.

## Operating Context

The user periodically records investment values manually or through OCR, reviews extracted values before saving, tracks monthly closings, inspects portfolio evolution and projections, and may synchronize or back up their data.

## Capabilities and Constraints

- Preserve all Firebase integration, persistence, calculations, OCR, imports, exports, backup behavior, and stored user data.
- Preserve the existing contribution-adjusted performance logic.
- Existing functionality is implemented as a self-contained static web application in `index.html`.
- Visual composition, hierarchy, navigation, charts, and components may be redesigned.

## Brand Commitments

- Product name: Meu Patrimônio.
- Brazilian Portuguese interface.
- The product should sit at the craft level of Apple Stocks, Kinvo, Linear, and BTG Pactual Private Banking without copying their branding.

## Evidence on Hand

- The working application and its complete interface, calculations, Firebase integration, persistence, OCR, import/export, and backup flows are present in `index.html`.
- Product review and implementation priorities are documented in `REVIEW.md`, `ROADMAP.md`, and `visual-pass2.md`.
- No external benchmarks, commercial claims, customer evidence, or proprietary brand assets are available and none should be fabricated.

## Product Principles

- Financial totals and changes should be understandable immediately.
- Contributions and investment performance must remain clearly distinguished.
- The interface should explain why wealth changed and what deserves attention next.
- Administrative and synchronization states should never compete with the portfolio story.
- User control and transparent financial logic take priority over brokerage-style complexity.

## Accessibility & Inclusion

Maintain strong contrast, keyboard-visible focus, reduced-motion support, semantic interaction states, readable financial typography, and comfortable pointer and touch targets.

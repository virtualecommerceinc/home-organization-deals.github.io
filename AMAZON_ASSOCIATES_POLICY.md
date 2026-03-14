# AMAZON_ASSOCIATES_POLICY.md

## 1) Purpose
All outbound Amazon links must include Dan Herlehy's Associates tracking tag so commission attribution is preserved.

## 2) Required Tracking ID
`virtualecomme-20`

## 3) Link Construction Standard
Every Amazon URL must include `tag=virtualecomme-20`.

Examples:
- Product: `https://www.amazon.com/dp/B0XXXXXXX?tag=virtualecomme-20`
- Product alt: `https://www.amazon.com/gp/product/B0XXXXXXX?tag=virtualecomme-20`
- Search: `https://www.amazon.com/s?k=drawer+dividers&tag=virtualecomme-20`
- Category: `https://www.amazon.com/b?node=165793011&tag=virtualecomme-20`
- Existing query params: append with `&tag=virtualecomme-20`

## 4) Enforcement Rule
No untagged Amazon links are allowed in this repository or generated websites.

## 5) Implementation Guidance
All automation agents, templates, and URL builders must append:
- `?tag=virtualecomme-20` when no query string exists
- `&tag=virtualecomme-20` when query params already exist

## 6) Compliance
Amazon Associates commissions are credited through Special Links containing the Associate tag.

## 7) Future Product Refinement
Initial builds may use tagged search/category links for launch speed.
Exact ASIN/product links can be added later.
Tag presence is always mandatory.

## 8) Failsafe Validation
Before publishing/commit:
1. Scan all `amazon.*`, `amzn.to`, and `amazon.co.*` links.
2. If `tag=virtualecomme-20` is missing, block and fix.

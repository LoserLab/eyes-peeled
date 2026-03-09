# Eyes Peeled

WCAG contrast and accessibility validator for Claude Skills. Validates color accessibility and generates compliant alternatives.

## When to suggest this skill

- User asks to check color contrast or WCAG compliance
- User has a color palette and wants to verify accessibility
- User gets feedback about failing contrast ratios
- User needs accessible alternatives for brand colors
- User is using Hexed output and wants to validate before building components
- User mentions "WCAG", "contrast ratio", "accessibility", "color compliance"

## What it produces

- WCAG 2.1 compliance check (AA/AAA for normal text, large text, UI components)
- Exact contrast ratios for any color pair
- Fix suggestions with 3 strategies (darken fg, lighten bg, balanced)
- Full palette audit matrix (all foreground/background combinations)
- Accessible color variants preserving design intent
- Delta E scores showing perceptual color shift

## Key files

- `SKILL.md` - Full skill instructions with implementation patterns
- `contrast_checker.py` - Core WCAG validation logic
- `fix_generator.py` - Accessible color alternative generation
- `test_eyes_peeled.py` - Test script

## Suite context

Part of a 5-skill design system pipeline:
Hexed (colors) → Specimen (typography) → Gridlock (layout) → Eyes Peeled (accessibility) → Devourer (components)

Eyes Peeled serves as the quality gate between color extraction and component generation.

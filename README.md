<div align="center">
  <img src="assets/eyes-peeled-logo.png?raw=true" alt="Eyes Peeled" width="600"/>
  
  <br/>
  <br/>
  
  **Contrast & Accessibility Validator for Claude Skills**
  
  [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)]()
  [![Claude Skills](https://img.shields.io/badge/Claude-Skills-purple)]()
  
</div>

---

# Eyes Peeled

Eyes Peeled is a Claude skill that validates WCAG color accessibility compliance and generates compliant alternatives while preserving design intent.

## What It Does

- Validates color combinations against WCAG 2.1 standards (AA/AAA)
- Generates minimal adjustments to meet accessibility requirements
- Preserves hue relationships and design intent
- Audits entire color palettes for accessibility issues
- Creates accessible variants using perceptual color science (CIELAB)
- Exports detailed compliance reports

## Installation

### For Claude Users

Install Eyes Peeled from the [Claude Skills marketplace](https://claude.ai):
1. Go to Settings → Skills
2. Search for "Eyes Peeled"
3. Click "Add Skill"

See [INSTALLATION.md](INSTALLATION.md) for detailed instructions.

### For Developers

To run locally or integrate into your own projects:

```bash
pip install colormath numpy
python test_eyes_peeled.py
```

## Files

- `SKILL.md` - Instructions for Claude on how to use the skill
- `contrast_checker.py` - Core WCAG validation logic
- `fix_generator.py` - Accessible color alternative generation
- `test_eyes_peeled.py` - Test script to verify functionality

## Usage

When a user asks for accessibility validation:

1. Import and run the contrast checker:
   ```python
   from contrast_checker import check_wcag, hex_to_rgb
   fg = hex_to_rgb('#2563eb')
   bg = hex_to_rgb('#ffffff')
   result = check_wcag(fg, bg)
   ```
2. Generate fixes if needed:
   ```python
   from fix_generator import generate_fixes
   fixes = generate_fixes('#60a5fa', '#ffffff', target_ratio=4.5)
   ```
3. Present results to user with specific contrast ratios and recommendations

See `SKILL.md` for complete usage instructions.

## Testing

To test the skill:

```bash
python test_eyes_peeled.py
```

This will:
- Test contrast ratio calculations
- Verify WCAG compliance checking
- Test hex/RGB conversions
- Validate output formatting

## Algorithm

1. **Relative Luminance**: Calculate per WCAG 2.1 formula
2. **Contrast Ratio**: (L1 + 0.05) / (L2 + 0.05)
3. **WCAG Check**: Compare against AA/AAA thresholds
4. **Fix Generation**: Use CIELAB color space for perceptual adjustments
5. **Preserve Intent**: Maintain hue and saturation, adjust only lightness

## WCAG Standards

### Contrast Requirements
- **AA Normal Text**: 4.5:1 minimum
- **AA Large Text**: 3:1 minimum (18pt+ or 14pt+ bold)
- **AAA Normal Text**: 7:1 minimum
- **AAA Large Text**: 4.5:1 minimum
- **UI Components**: 3:1 minimum

## Limitations

- Text/JSON output only (no visual previews)
- Requires colormath library for LAB color space conversions
- Some color combinations may be mathematically impossible to fix while maintaining color character
- Each validation is independent (no persistence between checks)

## Version

Current version: 1.0.0

## Author

Created by Heathen ([@heathenft](https://x.com/heathenft))

## License

MIT License

Copyright (c) 2026 Heathen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

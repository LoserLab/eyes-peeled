# Installing Eyes Peeled

Eyes Peeled is available as a Claude Skill for use in conversations with Claude.

## For Users

### Install from Claude Skills Marketplace

1. Go to [claude.ai](https://claude.ai)
2. Navigate to **Settings** → **Skills**
3. Search for **"Eyes Peeled"**
4. Click **"Add Skill"**
5. Start a new conversation

### Usage

Once installed, simply:
1. Ask Claude to check color contrast: *"Check if #3b82f6 on #ffffff meets AA standards"*
2. Request accessibility fixes: *"This blue (#60a5fa) fails on white - give me accessible alternatives"*
3. Audit entire palettes: *"Audit this palette for WCAG compliance"*

## For Developers

### Running Locally

If you want to use Eyes Peeled outside of Claude:

```bash
# Clone the repository
git clone https://github.com/yourusername/eyes-peeled.git
cd eyes-peeled

# Install dependencies
pip install colormath numpy

# Run tests
python test_eyes_peeled.py
```

### Integration

```python
from scripts.contrast_checker import check_wcag, hex_to_rgb
from scripts.fix_generator import generate_fixes

# Check contrast
fg = hex_to_rgb('#2563eb')
bg = hex_to_rgb('#ffffff')
result = check_wcag(fg, bg)

# Generate fixes if needed
if not result['AA_normal']:
    fixes = generate_fixes('#2563eb', '#ffffff', target_ratio=4.5)
    print(fixes)
```

## Requirements

- Python 3.8+
- colormath
- NumPy

All dependencies are included in Claude's environment.

## Support

- **Issues**: [GitHub Issues]TBA
- **Documentation**: See [README.md](README.md)
- **Author**: [@heathenft](https://x.com/heathenft)

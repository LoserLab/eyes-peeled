"""
Eyes Peeled - WCAG Contrast Checker
Core functionality for validating color accessibility
"""

def relative_luminance(rgb):
    """Calculate relative luminance per WCAG formula"""
    r, g, b = [v/255.0 for v in rgb]
    
    def adjust(val):
        return val/12.92 if val <= 0.03928 else ((val + 0.055)/1.055) ** 2.4
    
    R = adjust(r)
    G = adjust(g)
    B = adjust(b)
    
    return 0.2126 * R + 0.7152 * G + 0.0722 * B


def contrast_ratio(rgb1, rgb2):
    """Calculate WCAG contrast ratio between two colors"""
    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    
    lighter = max(l1, l2)
    darker = min(l1, l2)
    
    return (lighter + 0.05) / (darker + 0.05)


def check_wcag(fg_rgb, bg_rgb):
    """Return compliance levels for a color pair"""
    ratio = contrast_ratio(fg_rgb, bg_rgb)
    
    return {
        'ratio': round(ratio, 2),
        'AA_normal': ratio >= 4.5,
        'AA_large': ratio >= 3.0,
        'AAA_normal': ratio >= 7.0,
        'AAA_large': ratio >= 4.5,
        'UI_component': ratio >= 3.0
    }


def hex_to_rgb(hex_code):
    """Convert hex to RGB tuple"""
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    """Convert RGB tuple to hex"""
    return '#{:02x}{:02x}{:02x}'.format(*[int(v) for v in rgb])


def format_result(fg_hex, bg_hex, compliance):
    """Format compliance results in a readable way"""
    output = []
    output.append(f"\nContrast Check: {fg_hex} on {bg_hex}")
    output.append("━" * 50)
    output.append(f"Contrast Ratio: {compliance['ratio']}:1\n")
    output.append("WCAG Compliance:")
    
    checks = [
        ('AA_normal', 'AA Normal Text (4.5:1)'),
        ('AA_large', 'AA Large Text (3:1)'),
        ('AAA_normal', 'AAA Normal Text (7:1)'),
        ('AAA_large', 'AAA Large Text (4.5:1)'),
        ('UI_component', 'UI Components (3:1)')
    ]
    
    for key, label in checks:
        status = "✓" if compliance[key] else "✗"
        output.append(f"  {status} {label}")
    
    all_pass = all(compliance[k] for k, _ in checks)
    output.append(f"\nStatus: {'PASSES ALL REQUIREMENTS' if all_pass else 'FAILS SOME REQUIREMENTS'}")
    
    return '\n'.join(output)


if __name__ == '__main__':
    # Example usage
    fg = hex_to_rgb('#2563eb')
    bg = hex_to_rgb('#ffffff')
    result = check_wcag(fg, bg)
    print(format_result('#2563eb', '#ffffff', result))

"""
Eyes Peeled - Accessibility Fix Generator
Generates accessible color alternatives while preserving design intent
"""

try:
    from colormath.color_objects import sRGBColor, LabColor
    from colormath.color_conversions import convert_color
    from colormath.color_diff import delta_e_cie2000
    COLORMATH_AVAILABLE = True
except ImportError:
    COLORMATH_AVAILABLE = False
    print("Note: colormath not installed. Install with: pip install colormath")

from contrast_checker import relative_luminance, contrast_ratio, hex_to_rgb, rgb_to_hex


def lab_to_rgb(lab_color):
    """Convert LAB to RGB tuple"""
    if not COLORMATH_AVAILABLE:
        raise ImportError("colormath required for LAB conversions")
    
    rgb = convert_color(lab_color, sRGBColor)
    return (
        max(0, min(255, int(rgb.rgb_r * 255))),
        max(0, min(255, int(rgb.rgb_g * 255))),
        max(0, min(255, int(rgb.rgb_b * 255)))
    )


def lab_to_hex(lab_color):
    """Convert LAB to hex"""
    return rgb_to_hex(lab_to_rgb(lab_color))


def adjust_lightness(color_lab, target_ratio, fixed_color_lab, darken=False, lighten=False):
    """Adjust L* in LAB space to meet target contrast while preserving a* and b*"""
    if not COLORMATH_AVAILABLE:
        return None
    
    # Binary search for the right L* value
    current_L = color_lab.lab_l
    min_L, max_L = (0, current_L) if darken else (current_L, 100)
    
    for _ in range(20):  # Iterate to find optimal L*
        test_L = (min_L + max_L) / 2
        test_color = LabColor(test_L, color_lab.lab_a, color_lab.lab_b)
        test_rgb = lab_to_rgb(test_color)
        fixed_rgb = lab_to_rgb(fixed_color_lab)
        
        ratio = contrast_ratio(test_rgb, fixed_rgb)
        
        if abs(ratio - target_ratio) < 0.1:
            return test_color
        
        if ratio < target_ratio:
            if darken:
                max_L = test_L
            else:
                min_L = test_L
        else:
            if darken:
                min_L = test_L
            else:
                max_L = test_L
    
    return None


def generate_fixes(fg_hex, bg_hex, target_ratio=4.5):
    """Generate minimal adjustments to meet target contrast ratio"""
    if not COLORMATH_AVAILABLE:
        return None
    
    fg_rgb = hex_to_rgb(fg_hex)
    bg_rgb = hex_to_rgb(bg_hex)
    current_ratio = contrast_ratio(fg_rgb, bg_rgb)
    
    if current_ratio >= target_ratio:
        return None  # Already passes
    
    # Convert to LAB for perceptual adjustments
    fg_lab = convert_color(sRGBColor(*[v/255 for v in fg_rgb]), LabColor)
    bg_lab = convert_color(sRGBColor(*[v/255 for v in bg_rgb]), LabColor)
    
    fixes = []
    
    # Strategy 1: Darken foreground only
    fg_darker = adjust_lightness(fg_lab, target_ratio, bg_lab, darken=True)
    if fg_darker:
        fixes.append({
            'strategy': 'darken_foreground',
            'foreground': lab_to_hex(fg_darker),
            'background': bg_hex,
            'ratio': contrast_ratio(lab_to_rgb(fg_darker), bg_rgb)
        })
    
    # Strategy 2: Lighten background only
    bg_lighter = adjust_lightness(bg_lab, target_ratio, fg_lab, lighten=True)
    if bg_lighter:
        fixes.append({
            'strategy': 'lighten_background',
            'foreground': fg_hex,
            'background': lab_to_hex(bg_lighter),
            'ratio': contrast_ratio(fg_rgb, lab_to_rgb(bg_lighter))
        })
    
    return fixes


if __name__ == '__main__':
    # Example usage
    if COLORMATH_AVAILABLE:
        fixes = generate_fixes('#60a5fa', '#ffffff', target_ratio=4.5)
        if fixes:
            print("\nAccessible Fixes for #60a5fa on #ffffff:")
            print("━" * 50)
            for fix in fixes:
                print(f"\nStrategy: {fix['strategy']}")
                print(f"  Foreground: {fix['foreground']}")
                print(f"  Background: {fix['background']}")
                print(f"  Ratio: {fix['ratio']:.2f}:1")
        else:
            print("Colors already meet target contrast ratio")
    else:
        print("Install colormath to use fix generation: pip install colormath")

"""
Eyes Peeled - Test Suite
Verifies that all core functionality works correctly
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from contrast_checker import hex_to_rgb, contrast_ratio, check_wcag, format_result

def test_contrast_calculations():
    """Test basic contrast ratio calculations"""
    print("\n🧪 Testing Contrast Calculations")
    print("=" * 60)
    
    # Test case 1: Black on white (should be 21:1)
    black = (0, 0, 0)
    white = (255, 255, 255)
    ratio = contrast_ratio(black, white)
    expected = 21.0
    assert abs(ratio - expected) < 0.1, f"Expected {expected}, got {ratio}"
    print(f"✓ Black on white: {ratio:.2f}:1 (expected ~21:1)")
    
    # Test case 2: Same color (should be 1:1)
    blue = (37, 99, 235)
    ratio = contrast_ratio(blue, blue)
    expected = 1.0
    assert abs(ratio - expected) < 0.1, f"Expected {expected}, got {ratio}"
    print(f"✓ Same color: {ratio:.2f}:1 (expected 1:1)")
    
    # Test case 3: Known good contrast
    blue = hex_to_rgb('#2563eb')
    white = hex_to_rgb('#ffffff')
    ratio = contrast_ratio(blue, white)
    print(f"✓ Blue #2563eb on white: {ratio:.2f}:1")
    
    print("\n✅ All contrast calculations passed!")


def test_wcag_compliance():
    """Test WCAG compliance checking"""
    print("\n🧪 Testing WCAG Compliance")
    print("=" * 60)
    
    # Test passing combination
    fg = hex_to_rgb('#2563eb')  # Blue
    bg = hex_to_rgb('#ffffff')  # White
    result = check_wcag(fg, bg)
    
    assert result['AA_normal'], "Should pass AA normal text"
    print(f"✓ #2563eb on #ffffff passes AA normal ({result['ratio']}:1)")
    
    # Test failing combination
    fg = hex_to_rgb('#60a5fa')  # Light blue
    bg = hex_to_rgb('#ffffff')  # White
    result = check_wcag(fg, bg)
    
    assert not result['AA_normal'], "Should fail AA normal text"
    print(f"✓ #60a5fa on #ffffff fails AA normal ({result['ratio']}:1)")
    
    print("\n✅ All WCAG compliance checks passed!")


def test_hex_conversions():
    """Test hex to RGB conversions"""
    print("\n🧪 Testing Hex Conversions")
    print("=" * 60)
    
    test_cases = [
        ('#000000', (0, 0, 0)),
        ('#ffffff', (255, 255, 255)),
        ('#2563eb', (37, 99, 235)),
        ('#ff0000', (255, 0, 0)),
    ]
    
    for hex_code, expected_rgb in test_cases:
        result = hex_to_rgb(hex_code)
        assert result == expected_rgb, f"Expected {expected_rgb}, got {result}"
        print(f"✓ {hex_code} → {result}")
    
    print("\n✅ All hex conversions passed!")


def test_format_output():
    """Test formatted output generation"""
    print("\n🧪 Testing Output Formatting")
    print("=" * 60)
    
    fg = hex_to_rgb('#2563eb')
    bg = hex_to_rgb('#ffffff')
    result = check_wcag(fg, bg)
    output = format_result('#2563eb', '#ffffff', result)
    
    assert 'Contrast Ratio' in output
    assert 'WCAG Compliance' in output
    assert '✓' in output  # Should have passing checks
    print(output)
    
    print("\n✅ Output formatting works!")


def run_all_tests():
    """Run all test suites"""
    print("\n" + "=" * 60)
    print("EYES PEELED - Test Suite")
    print("=" * 60)
    
    try:
        test_hex_conversions()
        test_contrast_calculations()
        test_wcag_compliance()
        test_format_output()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED!")
        print("=" * 60)
        print("\nEyes Peeled is working correctly.")
        print("You can now use it for accessibility validation.\n")
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)

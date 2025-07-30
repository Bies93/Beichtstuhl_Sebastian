#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Color Contrast Analyzer for Beichtsthul Modern
Analyzes color contrast ratios to ensure WCAG 2.1 AA compliance.
"""

import math
import sys
import os
from typing import Tuple, Dict

# Add the parent directory to sys.path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.constants import *


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Convert hex color to RGB tuple
    
    Args:
        hex_color: Hex color string (e.g., "#ffffff")
        
    Returns:
        Tuple of RGB values (r, g, b)
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_luminance(rgb: Tuple[int, int, int]) -> float:
    """
    Calculate relative luminance of an RGB color
    Formula from WCAG 2.1 specification
    
    Args:
        rgb: RGB tuple (r, g, b) with values 0-255
        
    Returns:
        Relative luminance value
    """
    r, g, b = [c / 255.0 for c in rgb]
    
    # Apply gamma correction
    r = r / 12.92 if r <= 0.03928 else math.pow((r + 0.055) / 1.055, 2.4)
    g = g / 12.92 if g <= 0.03928 else math.pow((g + 0.055) / 1.055, 2.4)
    b = b / 12.92 if b <= 0.03928 else math.pow((b + 0.055) / 1.055, 2.4)
    
    # Calculate luminance
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def calculate_contrast_ratio(color1: str, color2: str) -> float:
    """
    Calculate contrast ratio between two colors
    Formula from WCAG 2.1 specification
    
    Args:
        color1: First hex color string
        color2: Second hex color string
        
    Returns:
        Contrast ratio (typically between 1:1 and 21:1)
    """
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    lum1 = rgb_to_luminance(rgb1)
    lum2 = rgb_to_luminance(rgb2)
    
    # Ensure lighter color is first
    if lum1 < lum2:
        lum1, lum2 = lum2, lum1
        
    return (lum1 + 0.05) / (lum2 + 0.05)


def check_wcag_compliance(contrast_ratio: float) -> Dict[str, bool]:
    """
    Check WCAG compliance levels for a given contrast ratio
    
    Args:
        contrast_ratio: Contrast ratio to check
        
    Returns:
        Dictionary with compliance status for different levels
    """
    return {
        "AA_normal": contrast_ratio >= 4.5,      # AA for normal text
        "AA_large": contrast_ratio >= 3.0,       # AA for large text
        "AAA_normal": contrast_ratio >= 7.0,     # AAA for normal text
        "AAA_large": contrast_ratio >= 4.5       # AAA for large text
    }


def analyze_color_combinations() -> Dict[str, Dict]:
    """
    Analyze all important color combinations in the application for WCAG compliance
    
    Returns:
        Dictionary with analysis results for each combination
    """
    # Define important color combinations to check
    combinations = [
        # Text on backgrounds
        ("Primary Text", COLOR_PRIMARY_TEXT, "Primary Background", COLOR_PRIMARY_BG),
        ("Primary Text", COLOR_PRIMARY_TEXT, "Secondary Background", COLOR_SECONDARY_BG),
        ("Secondary Text", COLOR_SECONDARY_TEXT, "Primary Background", COLOR_PRIMARY_BG),
        ("Secondary Text", COLOR_SECONDARY_TEXT, "Secondary Background", COLOR_SECONDARY_BG),
        ("Disabled Text", COLOR_DISABLED_TEXT, "Primary Background", COLOR_PRIMARY_BG),
        
        # Accent colors on backgrounds
        ("Primary Accent", COLOR_PRIMARY_ACCENT, "Primary Background", COLOR_PRIMARY_BG),
        ("Secondary Accent", COLOR_SECONDARY_ACCENT, "Primary Background", COLOR_PRIMARY_BG),
        ("Warning", COLOR_WARNING, "Primary Background", COLOR_PRIMARY_BG),
        ("Error", COLOR_ERROR, "Primary Background", COLOR_PRIMARY_BG),
        ("Success", COLOR_SUCCESS, "Primary Background", COLOR_PRIMARY_BG),
        
        # Special cases
        ("Primary Accent", COLOR_PRIMARY_ACCENT, "Secondary Background", COLOR_SECONDARY_BG),
        ("Error", COLOR_ERROR, "Secondary Background", COLOR_SECONDARY_BG),
    ]
    
    results = {}
    
    for combo in combinations:
        text_name, text_color, bg_name, bg_color = combo
        key = f"{text_name} on {bg_name}"
        
        contrast_ratio = calculate_contrast_ratio(text_color, bg_color)
        compliance = check_wcag_compliance(contrast_ratio)
        
        results[key] = {
            "text_color": text_color,
            "background_color": bg_color,
            "contrast_ratio": round(contrast_ratio, 2),
            "compliance": compliance,
            "wcag_pass": compliance["AA_normal"]  # Primary requirement
        }
    
    return results


def generate_contrast_report() -> str:
    """
    Generate a comprehensive contrast analysis report
    
    Returns:
        Formatted report string
    """
    results = analyze_color_combinations()
    
    report = "WCAG 2.1 AA Contrast Analysis Report\n"
    report += "=" * 50 + "\n\n"
    
    compliant_count = 0
    total_count = len(results)
    
    for combination, data in results.items():
        compliance_status = "PASS" if data["wcag_pass"] else "FAIL"
        status_symbol = "✓" if data["wcag_pass"] else "✗"
        
        if data["wcag_pass"]:
            compliant_count += 1
        
        report += f"{status_symbol} {combination}\n"
        report += f"   Text: {data['text_color']} | Background: {data['background_color']}\n"
        report += f"   Contrast Ratio: {data['contrast_ratio']}:1 ({compliance_status})\n"
        
        # Detailed compliance info
        comp = data["compliance"]
        report += f"   Compliance: AA Normal: {'✓' if comp['AA_normal'] else '✗'} | "
        report += f"AA Large: {'✓' if comp['AA_large'] else '✗'} | "
        report += f"AAA Normal: {'✓' if comp['AAA_normal'] else '✗'} | "
        report += f"AAA Large: {'✓' if comp['AAA_large'] else '✗'}\n\n"
    
    report += f"Summary: {compliant_count}/{total_count} combinations pass WCAG AA compliance\n"
    
    if compliant_count < total_count:
        report += "\n⚠️  WARNING: Some color combinations do not meet WCAG AA requirements!\n"
        report += "Consider adjusting colors to improve accessibility.\n"
    
    return report


def run_contrast_analysis():
    """
    Run the complete contrast analysis and print results
    """
    print("Running WCAG 2.1 AA Contrast Analysis...")
    report = generate_contrast_report()
    print(report)
    
    # Check if all combinations pass
    results = analyze_color_combinations()
    all_pass = all(data["wcag_pass"] for data in results.values())
    
    if not all_pass:
        print("\n❌ CI FAILURE: Some color combinations do not meet WCAG AA requirements!")
        print("Please review the report above and adjust colors accordingly.")
        return False
    else:
        print("\n✅ All color combinations meet WCAG AA requirements!")
        return True


if __name__ == "__main__":
    run_contrast_analysis()
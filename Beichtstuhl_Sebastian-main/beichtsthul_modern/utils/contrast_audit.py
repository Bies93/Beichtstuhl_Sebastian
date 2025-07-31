#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contrast Audit Script for Beichtsthul Modern
Checks color contrast ratios from design tokens against WCAG AA standards.
"""

import json
import os
import sys

def hex_to_rgb(hex_color):
    """Converts a hex color string to an (R, G, B) tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_luminance(rgb):
    """Calculates the relative luminance of an RGB color."""
    r, g, b = [x / 255.0 for x in rgb]
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def get_contrast_ratio(rgb1, rgb2):
    """Calculates the contrast ratio between two RGB colors."""
    lum1 = get_luminance(rgb1)
    lum2 = get_luminance(rgb2)
    return (max(lum1, lum2) + 0.05) / (min(lum1, lum2) + 0.05)

def run_contrast_audit():
    """
    Runs the contrast audit and returns True if all checks pass,
    otherwise False.
    """
    script_dir = os.path.dirname(__file__)
    tokens_path = os.path.join(script_dir, "..", "design_tokens", "design_tokens.json")
    
    with open(tokens_path, "r", encoding="utf-8") as f:
        tokens = json.load(f)

    colors = tokens.get("colors", {})
    bg_base = hex_to_rgb(colors.get("bg", {}).get("base", "#000000"))
    text_primary = hex_to_rgb(colors.get("text", {}).get("primary", "#FFFFFF"))

    contrast_ratio = get_contrast_ratio(text_primary, bg_base)
    
    print(f"Contrast ratio between text.primary and bg.base: {contrast_ratio:.2f}")

    if contrast_ratio < 4.5:
        print("Error: Contrast ratio is below WCAG AA standard of 4.5:1.")
        return False
    
    print("Contrast ratio meets WCAG AA standards.")
    return True

if __name__ == "__main__":
    if not run_contrast_audit():
        sys.exit(1)
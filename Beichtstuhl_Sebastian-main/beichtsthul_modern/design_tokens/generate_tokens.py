#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Token Generator for Beichtsthul Modern
Generates Python enums and QSS variables from design tokens.
"""

import json
import os
from typing import Dict, Any


def load_design_tokens() -> Dict[str, Any]:
    """
    Load design tokens from JSON file
    
    Returns:
        Dictionary containing design tokens
    """
    tokens_path = os.path.join(os.path.dirname(__file__), "design_tokens.json")
    with open(tokens_path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_python_tokens(tokens: Dict[str, Any]) -> str:
    """
    Generate Python enums from design tokens
    
    Args:
        tokens: Design tokens dictionary
        
    Returns:
        Python code as string
    """
    code = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Design Tokens for Beichtsthul Modern
Auto-generated from design_tokens.json
"""

from enum import Enum


'''
    
    # Generate color enums
    code += "class ColorTokens(Enum):\n"
    code += "    \"\"\"Color design tokens\"\"\"\n"
    
    # Base colors
    for key, value in tokens["colors"]["base"]["bg"].items():
        enum_name = f"BG_{key.upper()}"
        code += f"    {enum_name} = \"{value}\"\n"
    
    for key, value in tokens["colors"]["base"]["text"].items():
        enum_name = f"TEXT_{key.upper()}"
        code += f"    {enum_name} = \"{value}\"\n"
    
    # Accent colors
    for key, value in tokens["colors"]["accent"].items():
        enum_name = f"ACCENT_{key.upper()}"
        code += f"    {enum_name} = \"{value}\"\n"
    
    # Semantic colors
    for key, value in tokens["colors"]["semantic"].items():
        if isinstance(value, str):
            enum_name = f"SEMANTIC_{key.upper()}"
            code += f"    {enum_name} = \"{value}\"\n"
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                enum_name = f"SEMANTIC_{key.upper()}_{sub_key.upper()}"
                code += f"    {enum_name} = \"{sub_value}\"\n"
    
    code += "\n"
    
    # Generate radius enums
    code += "class RadiusTokens(Enum):\n"
    code += "    \"\"\"Border radius design tokens\"\"\"\n"
    for key, value in tokens["radius"].items():
        enum_name = key.upper()
        code += f"    {enum_name} = {value}\n"
    
    code += "\n"
    
    # Generate spacing enums
    code += "class SpacingTokens(Enum):\n"
    code += "    \"\"\"Spacing design tokens\"\"\"\n"
    for key, value in tokens["spacing"].items():
        enum_name = key.upper()
        code += f"    {enum_name} = {value}\n"
    
    code += "\n"
    
    # Generate duration enums
    code += "class DurationTokens(Enum):\n"
    code += "    \"\"\"Animation duration design tokens\"\"\"\n"
    for key, value in tokens["duration"].items():
        enum_name = key.upper()
        code += f"    {enum_name} = {value}\n"
    
    code += "\n"
    
    # Generate font enums
    code += "class FontTokens(Enum):\n"
    code += "    \"\"\"Font design tokens\"\"\"\n"
    
    # Headline fonts
    code += f"    HEADLINE_FAMILY = \"{tokens['fonts']['headline']['family']}\"\n"
    for key, value in tokens["fonts"]["headline"]["sizes"].items():
        enum_name = f"HEADLINE_SIZE_{key.upper()}"
        code += f"    {enum_name} = {value}\n"
    for key, value in tokens["fonts"]["headline"]["weight"].items():
        enum_name = f"HEADLINE_WEIGHT_{key.upper()}"
        code += f"    {enum_name} = {value}\n"
    
    # Body fonts
    code += f"    BODY_FAMILY = \"{tokens['fonts']['body']['family']}\"\n"
    for key, value in tokens["fonts"]["body"]["sizes"].items():
        enum_name = f"BODY_SIZE_{key.upper()}"
        code += f"    {enum_name} = {value}\n"
    for key, value in tokens["fonts"]["body"]["weight"].items():
        enum_name = f"BODY_WEIGHT_{key.upper()}"
        code += f"    {enum_name} = {value}\n"
    
    # Mono fonts
    code += f"    MONO_FAMILY = \"{tokens['fonts']['mono']['family']}\"\n"
    for key, value in tokens["fonts"]["mono"]["sizes"].items():
        enum_name = f"MONO_SIZE_{key.upper()}"
        code += f"    {enum_name} = {value}\n"
    for key, value in tokens["fonts"]["mono"]["weight"].items():
        enum_name = f"MONO_WEIGHT_{key.upper()}"
        code += f"    {enum_name} = {value}\n"
    
    return code


def generate_qss_variables(tokens: Dict[str, Any]) -> str:
    """
    Generate QSS variables from design tokens
    
    Args:
        tokens: Design tokens dictionary
        
    Returns:
        QSS variables as string
    """
    qss = "/* Design Tokens for Beichtsthul Modern */\n"
    qss += "/* Auto-generated from design_tokens.json */\n\n"
    
    # Generate color variables
    qss += "/* Color Tokens */\n"
    
    # Base colors
    for key, value in tokens["colors"]["base"]["bg"].items():
        var_name = f"bg-{key}"
        qss += f"@{var_name}: {value};\n"
    
    for key, value in tokens["colors"]["base"]["text"].items():
        var_name = f"text-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Accent colors
    for key, value in tokens["colors"]["accent"].items():
        var_name = f"accent-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Semantic colors
    for key, value in tokens["colors"]["semantic"].items():
        if isinstance(value, str):
            var_name = f"semantic-{key}"
            qss += f"@{var_name}: {value};\n"
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                var_name = f"semantic-{key}-{sub_key}"
                qss += f"@{var_name}: {sub_value};\n"
    
    qss += "\n"
    
    # Generate radius variables
    qss += "/* Radius Tokens */\n"
    for key, value in tokens["radius"].items():
        var_name = f"radius-{key}"
        qss += f"@{var_name}: {value}px;\n"
    
    qss += "\n"
    
    # Generate spacing variables
    qss += "/* Spacing Tokens */\n"
    for key, value in tokens["spacing"].items():
        var_name = f"spacing-{key}"
        qss += f"@{var_name}: {value}px;\n"
    
    qss += "\n"
    
    # Generate duration variables
    qss += "/* Duration Tokens */\n"
    for key, value in tokens["duration"].items():
        var_name = f"duration-{key}"
        qss += f"@{var_name}: {value}ms;\n"
    
    qss += "\n"
    
    # Generate font variables
    qss += "/* Font Tokens */\n"
    
    # Headline fonts
    qss += f"@font-headline-family: \"{tokens['fonts']['headline']['family']}\";\n"
    for key, value in tokens["fonts"]["headline"]["sizes"].items():
        var_name = f"font-headline-size-{key}"
        qss += f"@{var_name}: {value}px;\n"
    for key, value in tokens["fonts"]["headline"]["weight"].items():
        var_name = f"font-headline-weight-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Body fonts
    qss += f"@font-body-family: \"{tokens['fonts']['body']['family']}\";\n"
    for key, value in tokens["fonts"]["body"]["sizes"].items():
        var_name = f"font-body-size-{key}"
        qss += f"@{var_name}: {value}px;\n"
    for key, value in tokens["fonts"]["body"]["weight"].items():
        var_name = f"font-body-weight-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Mono fonts
    qss += f"@font-mono-family: \"{tokens['fonts']['mono']['family']}\";\n"
    for key, value in tokens["fonts"]["mono"]["sizes"].items():
        var_name = f"font-mono-size-{key}"
        qss += f"@{var_name}: {value}px;\n"
    for key, value in tokens["fonts"]["mono"]["weight"].items():
        var_name = f"font-mono-weight-{key}"
        qss += f"@{var_name}: {value};\n"
    
    return qss


def generate_qss_variables(tokens: Dict[str, Any]) -> str:
    """
    Generate QSS variables from design tokens
    
    Args:
        tokens: Design tokens dictionary
        
    Returns:
        QSS variables as string
    """
    qss = "/* Design Tokens for Beichtsthul Modern */\n"
    qss += "/* Auto-generated from design_tokens.json */\n\n"
    
    # Generate color variables
    qss += "/* Color Tokens */\n"
    
    # Base colors
    for key, value in tokens["colors"]["base"]["bg"].items():
        var_name = f"bg-{key}"
        qss += f"@{var_name}: {value};\n"
    
    for key, value in tokens["colors"]["base"]["text"].items():
        var_name = f"text-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Accent colors
    for key, value in tokens["colors"]["accent"].items():
        var_name = f"accent-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Semantic colors
    for key, value in tokens["colors"]["semantic"].items():
        if isinstance(value, str):
            var_name = f"semantic-{key}"
            qss += f"@{var_name}: {value};\n"
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                var_name = f"semantic-{key}-{sub_key}"
                qss += f"@{var_name}: {sub_value};\n"
    
    qss += "\n"
    
    # Generate radius variables
    qss += "/* Radius Tokens */\n"
    for key, value in tokens["radius"].items():
        var_name = f"radius-{key}"
        qss += f"@{var_name}: {value}px;\n"
    
    qss += "\n"
    
    # Generate spacing variables
    qss += "/* Spacing Tokens */\n"
    for key, value in tokens["spacing"].items():
        var_name = f"spacing-{key}"
        qss += f"@{var_name}: {value}px;\n"
    
    qss += "\n"
    
    # Generate duration variables
    qss += "/* Duration Tokens */\n"
    for key, value in tokens["duration"].items():
        var_name = f"duration-{key}"
        qss += f"@{var_name}: {value}ms;\n"
    
    qss += "\n"
    
    # Generate font variables
    qss += "/* Font Tokens */\n"
    
    # Headline fonts
    qss += f"@font-headline-family: \"{tokens['fonts']['headline']['family']}\";\n"
    for key, value in tokens["fonts"]["headline"]["sizes"].items():
        var_name = f"font-headline-size-{key}"
        qss += f"@{var_name}: {value}px;\n"
    for key, value in tokens["fonts"]["headline"]["weight"].items():
        var_name = f"font-headline-weight-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Body fonts
    qss += f"@font-body-family: \"{tokens['fonts']['body']['family']}\";\n"
    for key, value in tokens["fonts"]["body"]["sizes"].items():
        var_name = f"font-body-size-{key}"
        qss += f"@{var_name}: {value}px;\n"
    for key, value in tokens["fonts"]["body"]["weight"].items():
        var_name = f"font-body-weight-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Mono fonts
    qss += f"@font-mono-family: \"{tokens['fonts']['mono']['family']}\";\n"
    for key, value in tokens["fonts"]["mono"]["sizes"].items():
        var_name = f"font-mono-size-{key}"
        qss += f"@{var_name}: {value}px;\n"
    for key, value in tokens["fonts"]["mono"]["weight"].items():
        var_name = f"font-mono-weight-{key}"
        qss += f"@{var_name}: {value};\n"
    
    # Generate cyberpunk effect variables
    qss += "\n/* Cyberpunk Effects */\n"
    qss += f"@glow-blur: {tokens['effects']['glow']['blur']}px;\n"
    qss += f"@glow-spread: {tokens['effects']['glow']['spread']}px;\n"
    qss += f"@glass-opacity: {tokens['effects']['glass']['opacity']};\n"
    qss += f"@glass-blur: {tokens['effects']['glass']['blur']}px;\n"
    qss += f"@scanlines-opacity: {tokens['effects']['scanlines']['opacity']};\n"
    qss += f"@scanlines-fps: {tokens['effects']['scanlines']['fps']};\n"
    
    # Generate gradient variables for neon buttons
    qss += "\n/* Neon Button Gradients */\n"
    qss += "@neon-gradient-primary: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 @accent-primary, stop: 1 @accent-secondary);\n"
    qss += "@neon-gradient-secondary: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 @accent-secondary, stop: 1 @accent-primary);\n"
    qss += "@neon-gradient-warning: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 @accent-warn, stop: 1 @accent-error);\n"
    
    # Generate glassmorphism effect variables
    qss += "\n/* Glassmorphism Effects */\n"
    qss += "@glass-panel-bg: rgba(20, 24, 38, @glass-opacity);\n"
    
    # Generate glow effect variables
    qss += "\n/* Glow Effects */\n"
    qss += "@glow-primary: 0 0 @glow-blur @accent-primary;\n"
    qss += "@glow-secondary: 0 0 @glow-blur @accent-secondary;\n"
    qss += "@glow-warning: 0 0 @glow-blur @accent-warn;\n"
    qss += "@glow-error: 0 0 @glow-blur @accent-error;\n"
    
    return qss


def main():
    """Main function to generate tokens"""
    print("Generating design tokens...")
    
    # Load design tokens
    tokens = load_design_tokens()
    
    # Generate Python tokens
    python_tokens = generate_python_tokens(tokens)
    python_path = os.path.join(os.path.dirname(__file__), "design_tokens.py")
    with open(python_path, "w", encoding="utf-8") as f:
        f.write(python_tokens)
    print(f"Generated Python tokens: {python_path}")
    
    # Generate QSS variables
    qss_variables = generate_qss_variables(tokens)
    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    with open(qss_path, "w", encoding="utf-8") as f:
        f.write(qss_variables)
    print(f"Generated QSS variables: {qss_path}")
    
    print("Token generation complete!")


if __name__ == "__main__":
    main()
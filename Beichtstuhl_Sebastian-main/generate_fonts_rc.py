#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility to generate a proper PyQt6 resource module from assets/fonts.qrc.
Runs pyrcc6 if available and writes beichtsthul_modern/assets/fonts_rc.py.
If pyrcc6 is not installed, this script will print a clear message.
"""

import os
import sys
import subprocess
from shutil import which

ROOT = os.path.dirname(os.path.abspath(__file__))
QRC = os.path.join(ROOT, "beichtsthul_modern", "assets", "fonts.qrc")
OUT = os.path.join(ROOT, "beichtsthul_modern", "assets", "fonts_rc.py")

def main():
    exe = which("pyrcc6")
    if not exe:
        print("pyrcc6 not found. Install PyQt6 and ensure pyrcc6 is on PATH, then run:")
        print("  pyrcc6 beichtsthul_modern/assets/fonts.qrc -o beichtsthul_modern/assets/fonts_rc.py")
        sys.exit(1)
    if not os.path.exists(QRC):
        print(f"fonts.qrc not found at {QRC}")
        sys.exit(1)
    cmd = [exe, QRC, "-o", OUT]
    try:
        subprocess.check_call(cmd)
        print(f"Generated {OUT}")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate fonts_rc.py: {e}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
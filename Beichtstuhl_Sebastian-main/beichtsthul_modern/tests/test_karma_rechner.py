#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for KarmaRechner
"""

import sys
import os
import unittest

# Add the project root to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.karma_rechner import KarmaRechner


class TestKarmaRechner(unittest.TestCase):
    """Test cases for KarmaRechner"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.karma_rechner = KarmaRechner()

    def test_berechne_karma_schulden_lügen(self):
        """Test karma debt calculation for lies"""
        schulden = self.karma_rechner.berechne_karma_schulden("lügen", "Ich habe gelogen")
        self.assertEqual(schulden, 15)

    def test_berechne_karma_schulden_geld(self):
        """Test karma debt calculation for money-related sins"""
        schulden = self.karma_rechner.berechne_karma_schulden("geld", "Ich habe Geld gestohlen")
        # Should be 12 + 10 (penalty for "gestohlen") = 22
        self.assertEqual(schulden, 22)

    def test_berechne_karma_schulden_essen(self):
        """Test karma debt calculation for food-related sins"""
        schulden = self.karma_rechner.berechne_karma_schulden("essen", "Ich habe zu viel gegessen")
        self.assertEqual(schulden, 8)

    def test_berechne_karma_schulden_faul(self):
        """Test karma debt calculation for laziness"""
        schulden = self.karma_rechner.berechne_karma_schulden("faul", "Ich war faul")
        self.assertEqual(schulden, 5)

    def test_berechne_karma_schulden_neid(self):
        """Test karma debt calculation for envy"""
        schulden = self.karma_rechner.berechne_karma_schulden("neid", "Ich habe Neid verspürt")
        self.assertEqual(schulden, 10)

    def test_berechne_karma_schulden_standard(self):
        """Test karma debt calculation for standard sins"""
        schulden = self.karma_rechner.berechne_karma_schulden("standard", "Ich habe gesündigt")
        self.assertEqual(schulden, 7)

    def test_berechne_karma_schulden_with_penalty_words(self):
        """Test karma debt calculation with penalty words"""
        # Test with penalty words (10 bonus points)
        schulden1 = self.karma_rechner.berechne_karma_schulden("lügen", "Ich habe betrogen")
        self.assertEqual(schulden1, 25)  # 15 + 10 penalty
        
        # Test with penalty words (10 bonus points)
        schulden2 = self.karma_rechner.berechne_karma_schulden("geld", "Ich habe gestohlen")
        self.assertEqual(schulden2, 22)  # 12 + 10 penalty
        
        # Test with penalty words (10 bonus points)
        schulden3 = self.karma_rechner.berechne_karma_schulden("neid", "Ich habe verletzt")
        self.assertEqual(schulden3, 20)  # 10 + 10 penalty
        
        # Test with penalty words (10 bonus points)
        schulden4 = self.karma_rechner.berechne_karma_schulden("faul", "Ich habe absichtlich nichts getan")
        self.assertEqual(schulden4, 15)  # 5 + 10 penalty

    def test_berechne_karma_schulden_case_insensitive(self):
        """Test that penalty word detection is case insensitive"""
        schulden = self.karma_rechner.berechne_karma_schulden("lügen", "Ich habe BETROGEN")
        self.assertEqual(schulden, 25)  # 15 + 10 penalty

    def test_berechne_karma_schulden_multiple_penalty_words(self):
        """Test karma debt calculation with multiple penalty words"""
        schulden = self.karma_rechner.berechne_karma_schulden("lügen", "Ich habe betrogen und gestohlen")
        self.assertEqual(schulden, 25)  # 15 + 10 penalty (only one bonus applied)

    def test_berechne_karma_schulden_unknown_category(self):
        """Test karma debt calculation for unknown category"""
        schulden = self.karma_rechner.berechne_karma_schulden("unknown", "Ich habe gesündigt")
        self.assertEqual(schulden, 7)  # Should default to standard


if __name__ == '__main__':
    unittest.main()
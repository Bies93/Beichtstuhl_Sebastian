#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for AntwortGenerator
"""

import sys
import os
import unittest

# Add the project root to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.antwort_generator import AntwortGenerator


class TestAntwortGenerator(unittest.TestCase):
    """Test cases for AntwortGenerator"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.antwort_generator = AntwortGenerator()

    def test_kategorisiere_suende_lügen(self):
        """Test sin categorization for lies"""
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe gelogen")
        self.assertEqual(kategorie, "lügen")
        
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe eine Lüge erzählt")
        self.assertEqual(kategorie, "lügen")

    def test_kategorisiere_suende_geld(self):
        """Test sin categorization for money-related sins"""
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe Geld")
        # Should match "geld" keyword "geld"
        self.assertEqual(kategorie, "geld")
        
        kategorie = self.antwort_generator.kategorisiere_suende("Ich bin verschuldet")
        # Should match "geld" keyword "verschuldet"
        self.assertEqual(kategorie, "geld")

    def test_kategorisiere_suende_essen(self):
        """Test sin categorization for food-related sins"""
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe gegessen")
        # Should match "essen" keyword "gegessen"
        self.assertEqual(kategorie, "essen")
        
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe Schokolade")
        # Should match "essen" keyword "schokolade"
        self.assertEqual(kategorie, "essen")

    def test_kategorisiere_suende_faul(self):
        """Test sin categorization for laziness"""
        kategorie = self.antwort_generator.kategorisiere_suende("Ich war faul")
        self.assertEqual(kategorie, "faul")
        
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe nichts getan")
        # Should match "faul" keyword "nichts getan"
        self.assertEqual(kategorie, "faul")

    def test_kategorisiere_suende_neid(self):
        """Test sin categorization for envy"""
        kategorie = self.antwort_generator.kategorisiere_suende("Ich bin neidisch")
        # Should match "neid" keyword "neidisch"
        self.assertEqual(kategorie, "neid")
        
        kategorie = self.antwort_generator.kategorisiere_suende("Ich beneide ihn")
        # Should match "neid" keyword "beneid"
        self.assertEqual(kategorie, "neid")

    def test_kategorisiere_suende_standard(self):
        """Test sin categorization for standard sins"""
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe gesündigt")
        self.assertEqual(kategorie, "standard")
        
        kategorie = self.antwort_generator.kategorisiere_suende("Ich habe etwas Schlechtes getan")
        self.assertEqual(kategorie, "standard")

    def test_kategorisiere_suende_case_insensitive(self):
        """Test that sin categorization is case insensitive"""
        kategorie = self.antwort_generator.kategorisiere_suende("ICH HABE GELOGEN")
        self.assertEqual(kategorie, "lügen")

    def test_get_antwort_lügen(self):
        """Test getting response for lies category"""
        antwort = self.antwort_generator.get_antwort("lügen")
        self.assertIn(antwort, self.antwort_generator.antworten["lügen"])

    def test_get_antwort_geld(self):
        """Test getting response for money category"""
        antwort = self.antwort_generator.get_antwort("geld")
        self.assertIn(antwort, self.antwort_generator.antworten["geld"])

    def test_get_antwort_essen(self):
        """Test getting response for food category"""
        antwort = self.antwort_generator.get_antwort("essen")
        self.assertIn(antwort, self.antwort_generator.antworten["essen"])

    def test_get_antwort_faul(self):
        """Test getting response for laziness category"""
        antwort = self.antwort_generator.get_antwort("faul")
        self.assertIn(antwort, self.antwort_generator.antworten["faul"])

    def test_get_antwort_neid(self):
        """Test getting response for envy category"""
        antwort = self.antwort_generator.get_antwort("neid")
        self.assertIn(antwort, self.antwort_generator.antworten["neid"])

    def test_get_antwort_standard(self):
        """Test getting response for standard category"""
        antwort = self.antwort_generator.get_antwort("standard")
        self.assertIn(antwort, self.antwort_generator.antworten["standard"])

    def test_get_antwort_unknown_category(self):
        """Test getting response for unknown category"""
        antwort = self.antwort_generator.get_antwort("unknown")
        self.assertIn(antwort, self.antwort_generator.antworten["standard"])

    def test_prüfe_easter_eggs_match(self):
        """Test easter egg detection with matching phrases"""
        antwort, emotion = self.antwort_generator.prüfe_easter_eggs("Ich habe eine Katze")
        self.assertEqual(antwort, "Tiere sind unschuldig! Du hingegen... NICHT")
        self.assertEqual(emotion, "schockiert")

    def test_prüfe_easter_eggs_no_match(self):
        """Test easter egg detection with no matching phrases"""
        antwort, emotion = self.antwort_generator.prüfe_easter_eggs("Ich habe gesündigt")
        self.assertIsNone(antwort)
        self.assertIsNone(emotion)

    def test_prüfe_easter_eggs_case_insensitive(self):
        """Test that easter egg detection is case insensitive"""
        antwort, emotion = self.antwort_generator.prüfe_easter_eggs("ICH HABE EINE KATZE")
        self.assertEqual(antwort, "Tiere sind unschuldig! Du hingegen... NICHT")
        self.assertEqual(emotion, "schockiert")

    def test_emotionen_mapping(self):
        """Test emotion mapping for categories"""
        self.assertEqual(self.antwort_generator.emotionen_mapping["lügen"], "urteilend")
        self.assertEqual(self.antwort_generator.emotionen_mapping["geld"], "genervt")
        self.assertEqual(self.antwort_generator.emotionen_mapping["essen"], "lachend")
        self.assertEqual(self.antwort_generator.emotionen_mapping["faul"], "genervt")
        self.assertEqual(self.antwort_generator.emotionen_mapping["neid"], "schockiert")
        self.assertEqual(self.antwort_generator.emotionen_mapping["standard"], "neutral")


if __name__ == '__main__':
    unittest.main()
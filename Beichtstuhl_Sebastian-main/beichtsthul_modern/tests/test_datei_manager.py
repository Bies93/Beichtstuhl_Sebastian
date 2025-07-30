#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for DateiManager
"""

import sys
import os
import unittest
import json
import tempfile
import shutil

# Add the project root to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.datei_manager import DateiManager
from core.constants import DATA_FILE_NAME


class TestDateiManager(unittest.TestCase):
    """Test cases for DateiManager"""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.original_data_file = DATA_FILE_NAME
        
        # Create a DateiManager instance with a test file path
        self.test_data_file = os.path.join(self.test_dir, "beichtstuh_daten_.json")
        self.datei_manager = DateiManager(self.test_data_file)

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        # Remove the temporary directory
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_init(self):
        """Test DateiManager initialization"""
        self.assertIsNotNone(self.datei_manager)
        self.assertTrue(os.path.exists(self.test_dir))

    def test_lade_daten_file_not_exists(self):
        """Test loading data when file doesn't exist"""
        # Ensure the test file doesn't exist
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
            
        karma_schulden, beicht_historie, suenden_kategorien = self.datei_manager.lade_daten()
        
        # Should return default values
        self.assertEqual(karma_schulden, 0)
        self.assertEqual(beicht_historie, [])
        self.assertEqual(suenden_kategorien, {})

    def test_lade_daten_file_exists_valid_data(self):
        """Test loading data from a valid file"""
        # Create test data
        test_data = {
            "karma_schulden": 42,
            "beicht_historie": [
                {"suende": "Ich habe gelogen", "kategorie": "lügen", "karma": 15}
            ],
            "suenden_kategorien": {"lügen": 1}
        }
        
        # Write test data to file
        with open(self.test_data_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
            
        karma_schulden, beicht_historie, suenden_kategorien = self.datei_manager.lade_daten()
        
        # Should return the test data
        self.assertEqual(karma_schulden, 42)
        self.assertEqual(len(beicht_historie), 1)
        self.assertEqual(beicht_historie[0]["suende"], "Ich habe gelogen")
        self.assertEqual(suenden_kategorien["lügen"], 1)

    def test_lade_daten_file_exists_invalid_json(self):
        """Test loading data from a file with invalid JSON"""
        # Create invalid JSON file
        with open(self.test_data_file, 'w', encoding='utf-8') as f:
            f.write("invalid json content")
            
        karma_schulden, beicht_historie, suenden_kategorien = self.datei_manager.lade_daten()
        
        # Should return default values
        self.assertEqual(karma_schulden, 0)
        self.assertEqual(beicht_historie, [])
        self.assertEqual(suenden_kategorien, {})

    def test_lade_daten_file_exists_missing_keys(self):
        """Test loading data from a file with missing keys"""
        # Create test data with missing keys
        test_data = {
            "karma_schulden": 42
            # Missing beicht_historie and suenden_kategorien
        }
        
        # Write test data to file
        with open(self.test_data_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
            
        karma_schulden, beicht_historie, suenden_kategorien = self.datei_manager.lade_daten()
        
        # Should return partial data with defaults for missing keys
        self.assertEqual(karma_schulden, 42)
        self.assertEqual(beicht_historie, [])
        self.assertEqual(suenden_kategorien, {})

    def test_speichere_daten(self):
        """Test saving data to file"""
        karma_schulden = 42
        beicht_historie = [
            {"suende": "Ich habe gelogen", "kategorie": "lügen", "karma": 15}
        ]
        suenden_kategorien = {"lügen": 1}
        
        # Save data
        self.datei_manager.speichere_daten(karma_schulden, beicht_historie, suenden_kategorien)
        
        # Check that file was created
        self.assertTrue(os.path.exists(self.test_data_file))
        
        # Load data back and verify
        with open(self.test_data_file, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
            
        self.assertEqual(saved_data["karma_schulden"], karma_schulden)
        self.assertEqual(len(saved_data["beicht_historie"]), len(beicht_historie))
        self.assertEqual(saved_data["beicht_historie"][0]["suende"], beicht_historie[0]["suende"])
        self.assertEqual(saved_data["suenden_kategorien"], suenden_kategorien)

    def test_speichere_daten_overwrites_existing(self):
        """Test that saving data overwrites existing file"""
        # Create initial data
        initial_data = {
            "karma_schulden": 10,
            "beicht_historie": [],
            "suenden_kategorien": {}
        }
        
        with open(self.test_data_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f)
            
        # Save new data
        new_karma_schulden = 42
        self.datei_manager.speichere_daten(new_karma_schulden, [], {})
        
        # Load data back and verify it was overwritten
        with open(self.test_data_file, 'r', encoding='utf-8') as f:
            saved_data = json.load(f)
            
        self.assertEqual(saved_data["karma_schulden"], new_karma_schulden)
        self.assertNotEqual(saved_data["karma_schulden"], initial_data["karma_schulden"])


if __name__ == '__main__':
    unittest.main()
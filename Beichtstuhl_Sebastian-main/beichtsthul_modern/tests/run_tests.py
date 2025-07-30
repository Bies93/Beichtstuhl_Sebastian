#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test runner for Beichtsthul Modern
Runs all unit tests and generates coverage report.
"""

import sys
import os
import unittest
import argparse

# Add the project root to sys.path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_tests(verbosity=2):
    """Run all unit tests"""
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Run Beichtsthul Modern unit tests')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-q', '--quiet', action='store_true', help='Quiet output')
    
    args = parser.parse_args()
    
    # Set verbosity level
    if args.quiet:
        verbosity = 0
    elif args.verbose:
        verbosity = 2
    else:
        verbosity = 1
    
    # Run tests
    exit_code = run_tests(verbosity)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
# test_banditsecurity.py
"""
Tests for BanditSecurity module.
"""

import unittest
from banditsecurity import BanditSecurity

class TestBanditSecurity(unittest.TestCase):
    """Test cases for BanditSecurity class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BanditSecurity()
        self.assertIsInstance(instance, BanditSecurity)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BanditSecurity()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

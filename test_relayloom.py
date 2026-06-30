# test_relayloom.py
"""
Tests for RelayLoom module.
"""

import unittest
from relayloom import RelayLoom

class TestRelayLoom(unittest.TestCase):
    """Test cases for RelayLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RelayLoom()
        self.assertIsInstance(instance, RelayLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RelayLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

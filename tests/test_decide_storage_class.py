import unittest
from src.decide_storage_class import decide_storage_class

class TestDecideStorageClass(unittest.TestCase):
    
    def test_cold_data_transition(self, last_accessed_days=45):
        # Test case: Objects older than the 30-day threshold should transition to STANDARD_IA
        days_threshold = 30
        result = decide_storage_class(last_accessed_days, threshold=days_threshold)
        self.assertEqual(result, "STANDARD_IA")

    def test_hot_data_retention(self, last_accessed_days=10):
        # Test case: Objects accessed recently should remain in standard storage (None or STANDARD)
        days_threshold = 30
        result = decide_storage_class(last_accessed_days, threshold=days_threshold)
        self.assertIn(result, [None, "STANDARD", "NO_ACTION"])

if __name__ == '__main__':
    unittest.main()

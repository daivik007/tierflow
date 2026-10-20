import unittest
from unittest.mock import MagicMock
from src.athena_parser import parse_athena_results

class TestAthenaParser(unittest.TestCase):
    
    def test_parse_athena_rows(self):
        # Mocking Athena ResultSet response structure
        mock_response = {
            'ResultSet': {
                'Rows': [
                    {'Data': [{'VarCharValue': 'prefix'}, {'VarCharValue': 'last_accessed_days_ago'}]},
                    {'Data': [{'VarCharValue': 'project-data/'}, {'VarCharValue': '48'}]}
                ]
            }
        }
        
        parsed_data = parse_athena_results(mock_response)
        
        # Verify it successfully extracts prefix and days
        self.assertEqual(len(parsed_data), 1)
        self.assertEqual(parsed_data[0]['prefix'], 'project-data/')
        self.assertEqual(parsed_data[0]['days_ago'], 48)

if __name__ == '__main__':
    unittest.main()

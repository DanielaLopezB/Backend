# Author : Daniela López Barahona
# openAssessment.test.py does the test of the method GET openAssement()
# July 2020

import unittest
import json
from main import app
import sys

class BasicTestCase(unittest.TestCase):
    def test_openAssesment(self):
            tester = app.test_client(self)
            response = tester.get('/api/v1/assessment/test/mode/179/undefined', content_type='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())),  {"Status": 1, "Message": "success", "Data": {
            "IsInviteOnly": False, "IsEligible": True}})

if __name__ == '__main__':
    unittest.main()

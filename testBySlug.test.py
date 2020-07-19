# Author : Daniela López Barahona
# testBy.test.py does the test of the method GET testBySlug()
# July 2020

import unittest
import json
import sys

from main import app

class BasicTestCase(unittest.TestCase):
    def test_testBySlug(self):
            tester = app.test_client(self)
            response = tester.get('/api/v1/survey/testBySlug/data-scientist/false', content_type='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())),  {'Status': 1, 'Message': 'Success',  'Data': []})

if __name__ == '__main__':
    unittest.main()

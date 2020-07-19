# Author : Daniela López Barahona
# startAssessment.test.py does the test of the method POST startAssessment()
# July 2020

import unittest
import json
import sys
from bson.objectid import ObjectId

from main import app, mongo


class BasicTestCase(unittest.TestCase):
    def test_startAssessment(self):

        print("\n Enter the idSession")
        idSession = input()

        url = '/api/v1/assessment/' + idSession + '/start'

        tester = app.test_client(self)
        response = tester.post(
            url, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), {"Status": 1, "Message": "success", "Data": True
                                                                                            })


if __name__ == '__main__':
    unittest.main()

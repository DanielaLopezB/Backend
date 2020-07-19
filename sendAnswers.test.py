# Author : Daniela López Barahona
# sendAnswers.test.py does the test of the method POST sendAnswers()
#July 2020

import unittest
import json
import sys

from main import app

class BasicTestCase(unittest.TestCase):
    def test_createUser(self):

        print("\n Enter the idSession")
        idSession = input()

        print("\n Enter the Body request")
        body = input()

        url = '/api/v1/assessment/' + idSession + '/answerAll'

        tester = app.test_client(self)
        response = tester.post(
            url,content_type='application/json',data = body )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), {"Status": 1, "Message": "success", "Data": True
                                                                                            })

if __name__ == '__main__':
    unittest.main()

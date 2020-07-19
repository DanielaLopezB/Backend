# Author : Daniela López Barahona
# showQuestion.test.py does the test of the method GET showQuestion()
# July 2020

import unittest
import json
import sys

from main import app
from dataBase import lookQuestion



class BasicTestCase(unittest.TestCase):
    def test_showQuestion(self):

        print("\n Enter the id Session")
        idSession = input()

        print("\n Enter the question number")
        numQ = input()
        
        url = '/api/v1/assessment/' + idSession + '/question/' + numQ
        print ("\n Loading... \n")

        responseDB = lookQuestion(idSession,numQ)

        tester = app.test_client(self)
        response = tester.get(
            url, content_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), responseDB)


if __name__ == '__main__':
    unittest.main()

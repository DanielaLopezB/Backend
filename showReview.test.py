# Author : Daniela López Barahona
# showReview.test.py does the test of the method GET showReview()
#July 2020

import unittest
import json
import sys

from main import app
from dataBase import showAnswers

class BasicTestCase(unittest.TestCase):
    def test_showReview(self):

        print("\n Enter the id Session")
        idSession = input()

        url = '/api/v1/assessment/' + idSession + '/review' 
        print ("\n Loading... \n")

        responseDB = showAnswers(idSession)

        tester = app.test_client(self)
        response = tester.get(
            url, content_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), responseDB)


if __name__ == '__main__':
    unittest.main()








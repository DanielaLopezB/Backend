# Author : Daniela López Barahona
# callSession.test.py does the test of the method GET callSession()
# July 2020

import unittest
import json
import sys

from main import app
from dataBase import lookS



class BasicTestCase(unittest.TestCase):
    def test_callSession(self):

        print("\n Enter the is Session")
        idSession = input()

        print("\n Enter the tsp")
        idTest = input()
        
        url = '/api/v1/assessment/' + idSession + '/'+ idTest
        print ("\n Loading... \n")

        responseDB = lookS(idSession)

        tester = app.test_client(self)
        response = tester.get(
            url, content_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), responseDB)


if __name__ == '__main__':
    unittest.main()

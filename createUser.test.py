# Author : Daniela López Barahona
# createUser.test.py does the test of the method POST createUser()
#July 2020

import unittest
import json
import sys
from bson.objectid import ObjectId

from main import app,mongo

class BasicTestCase(unittest.TestCase):
    def test_createUser(self):

        print("\n Enter the parentId")
        parentId = input()

        print("\n Enter the Name")
        name = input()

        print("\n Enter the Surname")
        surname = input()

        print("\n Enter the Email")
        email = input()

        url = '/api/v1/assessment/create/' + parentId
        print("\n Loading... \n")

        information =json.dumps({'Name': name, 'Surname': surname, 'Email': email})

        tester = app.test_client(self)
        response = tester.post(
            url,content_type='application/json',data = information )

        user = mongo.db.tests.find_one({'_id':  ObjectId(response.json['Data'])})
        emailDB = user['Email']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(email, emailDB)


if __name__ == '__main__':
    unittest.main()

# Author : Daniela López Barahona
# dataBase.py hs the corresponding request to the data base
# July 2020

from app import mongo
from bson.objectid import ObjectId
from datetime import datetime


def addUser(name, lastName, email, ParentTestId):

    try:
        Q = []
        questions = mongo.db.questions.find({}, {'_id': 0}).limit(15)

        for question in questions:
            Q.append(question)

        id = mongo.db.tests.insert(
            {'Name': name, 'Surname': lastName,
                'Email': email, 'ParentTestId': ParentTestId, 'questions': Q}
        )

        return str(id)

    except Exception as e:
        return {"Error": str(e)}


def lookS(idSession):
    try:
        user = mongo.db.tests.find_one({'_id':  ObjectId(idSession)})
        PId = user['ParentTestId']

        if PId != None:
            message = {"Status": 1, "Message": "success",
                       "Data": {'ParentTestId': PId}}
            return (message)
        else:
            message = {"Message": "Don't found"}
            return (message)

    except Exception as e:
        return {"Error": str(e)}


def startTest(idSession):
    try:
        startDate = datetime.now()
        myquery = {'_id':  ObjectId(idSession)}
        addTime = {'$set': {'time': 3600}}
        addData = {'$set': {'date': startDate}}
        mongo.db.tests.update_one(myquery, addTime)
        mongo.db.tests.update_one(myquery, addData)

        message = {"Status": 1, "Message": "success", "Data": True}

        return (message)

    except Exception as e:
        return {"Error": str(e)}


def lookQuestion(idSession, numQ):

    try:
        user = mongo.db.tests.find_one(
            {'_id': ObjectId(idSession)}, {'_id': 0})
        time = user['time']

        if time > 0:
            question = user['questions'][numQ-1]

            timer(idSession)

            message = {"Status": 1, "Message": "success", "Data": question}
        
        else:
            message = {"Status": 1, "Message": "success", "Data": False}

        return (message)

    except Exception as e:
        return {"Error": str(e)}


def addAnswer(idSession, QuestionId, OptionId, At, Ct, Ct2):

    try:
        user = mongo.db.tests.find_one(
            {'_id': ObjectId(idSession)}, {'_id': 0})
        time = user['time']

        if time > 0:
            question = mongo.db.tests.find_one({'_id': ObjectId(idSession)}, {
                '_id': 0, "questions": {'$elemMatch': {"Id": QuestionId}}})

            questionType = question['questions'][0]['QuestionType']

            if questionType == 1:
                mongo.db.tests.update_one(
                    {
                        '_id': ObjectId(idSession),
                        'questions.Id': QuestionId
                    },
                    {
                        '$set': {"questions.$.AnswerOptionId": OptionId}
                    }

                )
            if questionType == 3:
                mongo.db.tests.update_one(
                    {
                        '_id': ObjectId(idSession),
                        "questions.Id": QuestionId
                    },
                    {
                        '$set': {"questions.$.AnsweredText": At}
                    }

                )

            remindSeconds = time - timer(idSession) 

            mongo.db.tests.update_one(
                {
                    '_id': ObjectId(idSession),
                    'questions.Id': QuestionId
                },
                {
                    '$set': {"questions.$.RemainingSecond":  remindSeconds }
                }

            )

            message = {"Status": 1, "Message": "success", "Data": True}

        else:

            message = {"Status": 1, "Message": "success", "Data": False}

        return (message)

    except Exception as e:
        return {"Error": str(e)}


def showAnswers(idSession):
    try:
        user = mongo.db.tests.find_one(
            {'_id': ObjectId(idSession)}, {'_id': 0})
        time = user['time']

        if time > 0:
            user = mongo.db.tests.find_one(
                {'_id': ObjectId(idSession)}, {'_id': 0})
            questions = user['questions']

            message = {"Status": 1, "Message": "success", "Data": questions}

        else:

            message = {"Status": 1, "Message": "success", "Data": False}

        return (message)

    except Exception as e:
        return {"Error": str(e)}



def editAnswers(idSession, data):
    try:

        user = mongo.db.tests.find_one(
            {'_id': ObjectId(idSession)}, {'_id': 0})
        time = user['time']

        if time > 0:
            for x in data:
                questionId = x['QuestionId']
                question = mongo.db.tests.find_one({'_id': ObjectId(idSession)}, {
                '_id': 0, "questions": {'$elemMatch': {'Id': questionId }}})

                questionType = question['questions'][0]['QuestionType']


                if questionType == 1:
                    mongo.db.tests.update_one(
                        {
                            '_id': ObjectId(idSession),
                            'questions.Id': x['QuestionId']
                        },
                        {
                            '$set': {'questions.$.AnswerOptionId': x['OptionId']}
                        }

                    )
                if questionType == 3:
                    mongo.db.tests.update_one(
                        {
                            '_id': ObjectId(idSession),
                            "questions.Id": x['QuestionId']
                        },
                        {
                            '$set': {'questions.$.AnsweredText': x['AnsweredText']}
                        }

                    )
            message = {"Status": 1, "Message": "success", "Data": True}
        else:
            message = {"Status": 1, "Message": "success", "Data": False}



        return (message)

    except Exception as e:

        return {"Error": str(e)}


def lookResult(idSession):
    try:
        emptyQuestion = 0
        questionCount = 0

        user = mongo.db.tests.find_one(
            {'_id': ObjectId(idSession)}, {'_id': 0})

        questions = user['questions']

        for x in questions:

            if x['Id'] != None:
                questionCount += 1

            if x['QuestionType'] == 1:
                if x['AnswerOptionId'] == None:
                    emptyQuestion += 1

            if x['QuestionType'] == 3:
                if x['AnsweredText'] == None:
                    emptyQuestion += 1

        message = {"Status": 1, "Message": "success", "Data": {'Gkey': idSession,
                                                               'TakerName': user['Name'], 'TakerSurname': user['Surname'], 'TakerEmail': user['Email'], 'QuestionCount': questionCount, 'EmptyAnswers': emptyQuestion}}

        return (message)

    except Exception as e:
        return {"Error": str(e)}


def addFeedback(idSession, feedback):
    try:
        myquery = {'_id':  ObjectId(idSession)}
        addTime = {'$set': {'feedback': feedback}}
        mongo.db.tests.update_one(myquery, addTime)

        message = {"Status": 1, "Message": "success", "Data": True}

        return (message)

    except Exception as e:
        return {"Error": str(e)}


def timer(idSession):

    user = mongo.db.tests.find_one(
        {'_id': ObjectId(idSession)}, {'_id': 0})
    date = user['date']
    time = user['time']

    currentDate = datetime.now()
    diference = currentDate-date
    timeNow = time - diference.seconds

    myquery = {'_id':  ObjectId(idSession)}
    addTime = {'$set': {'time': timeNow}}
    addData = {'$set': {'date': currentDate}}
    mongo.db.tests.update_one(myquery, addTime)
    mongo.db.tests.update_one(myquery, addData)

    return diference.seconds

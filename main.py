# Author : Daniela López Barahona
# main.py has the corresponding routes of the API-REST
# July 2020


#IMPORTS

from app import app, mongo
from flask import request, jsonify, Response, session
from bson import json_util

from dataBase import addUser, lookS, startTest, lookQuestion, addAnswer, showAnswers, editAnswers, lookResult,addFeedback

#METHODS GET

@app.route('/api/v1/survey/test/179/true', methods=['GET', 'OPTION'])
def openSurvey():
    try:
        response = jsonify({'Status': 1, 'Message': 'Success',  'Data': []})
        return response

    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/test/mode/179/undefined', methods=['GET', 'OPTION'])
def openAssessment():
    try:
        response = jsonify({"Status": 1, "Message": "success", "Data": {
            "IsInviteOnly": False, "IsEligible": True}})

        return response

    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/<test>', methods=['GET', 'OPTION'])
def callSession(id_session, test):
    try:
        response = json_util.dumps(lookS(id_session))

        return Response(response, mimetype="application/json")

    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/question/<int:num_Q>', methods=['GET', 'OPTION'])
def showQuestion(id_session, num_Q):
    try:
        response = json_util.dumps(lookQuestion(id_session,num_Q))
 
        return  Response(response, mimetype="application/json")
        
    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/review' , methods=['GET', 'OPTION'])
def showReview(id_session):
    try:
        response = json_util.dumps(showAnswers(id_session))
 
        return  Response(response, mimetype="application/json")
        
    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/result' , methods=['GET', 'OPTION'])
def showResult(id_session):
    try:
        response = json_util.dumps(lookResult(id_session))
 
        return  Response(response, mimetype="application/json")
        
    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/survey/testBySlug/data-scientist/false' , methods=['GET', 'OPTION'])
def testBySlug():
    try:
        response = jsonify({'Status': 1, 'Message': 'Success',  'Data': []})
        return response

    except Exception as e:
        return {"Error": str(e)}


#METHODS POST

@app.route('/api/v1/assessment/create/<ParentTestId>', methods=['POST', 'OPTION'])
def createUser(ParentTestId):
    try:
        name = request.json['Name']
        lastName = request.json['Surname']
        email = request.json['Email']

        idSession = addUser(name, lastName, email, ParentTestId)
        
        response = jsonify(
            {'Status': 1, 'Message': 'Success',  'Data': idSession})

        return response

    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/start', methods=['POST', 'OPTION'])
def startAssessment(id_session):
    try:
        response = json_util.dumps(startTest(id_session))
        return Response(response, mimetype="application/json")
    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/answer' , methods=['POST', 'OPTION'])
def sendAnswer(id_session):
    try:
        session.permanent = True
        QuestionId = request.json['QuestionId']
        OptionId = request.json['OptionId']
        At = request.json['AnsweredText']
        Ct = request.json['ChildQuestionAnsweredText']
        Ct2 = request.json['ChildQuestionAnsweredText2']

        response = json_util.dumps(addAnswer(id_session,QuestionId,OptionId,At,Ct,Ct2))

        return  Response(response, mimetype="application/json")
        
    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/answerAll', methods=['POST', 'OPTION'])
def sendAnswers (id_session):
    try:

        data = request.get_json()

        response = json_util.dumps(editAnswers(id_session,data))
 
        return  Response(response, mimetype="application/json")
        
    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/end', methods=['POST', 'OPTION'])
def endSurvey(id_session):
    try:
        response = jsonify({'Status': 1, 'Message': 'Success',  'Data': True})
        return response

    except Exception as e:
        return {"Error": str(e)}


@app.route('/api/v1/assessment/<id_session>/feedback' , methods=['POST', 'OPTION'])
def sendFeedback(id_session):
    try:
        feedback = request.json['Text']

        response = json_util.dumps(addFeedback(id_session,feedback))

        return  Response(response, mimetype="application/json")
        
    except Exception as e:
        return {"Error": str(e)}


#------------------------------------------------
if __name__ == '__main__': 
    app.run(debug=True, port=5000)


# Author : Daniela López Barahona
# app.py creates de app impOrting flaSk and makes the connection with the DB
# July 2020

#IMPORTS
from flask import Flask,request, jsonify
from flask_pymongo import PyMongo
from datetime import timedelta

#Configuration------------------------------------------------------------------------------------
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/survey"
app.secret_key ="123"
#app.config["MONGO_URI"] = "mongodb+srv://danielaLopez:testAPI@cluster0.deqyf.mongodb.net/survey"
mongo = PyMongo(app)

app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(seconds=3600)



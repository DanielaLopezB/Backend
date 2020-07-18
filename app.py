# Author : Daniela López Barahona
# app.py creates de app impOrting flaSk and makes the connection with the DB
# July 2020

from flask import Flask,request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/survey"
#app.config["MONGO_URI"] = "mongodb+srv://danielaLopez:testAPI@cluster0.deqyf.mongodb.net/survey"
mongo = PyMongo(app)



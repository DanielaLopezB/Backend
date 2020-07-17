from flask import Flask,request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/survey"
mongo = PyMongo(app)



import os, json
from flask import Flask, request
from bson import json_util
from bson.objectid import ObjectId


app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
  return 'hello world'


import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import threading
import base64
from dotenv import load_dotenv
import bcrypt
import json
import jwt
import datetime
import numpy as np
from glob import glob
from util.jwt import create_jwt_token
import os
import math

load_dotenv()

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

UPLOAD_FOLDER = '/content/drive/MyDrive/FlaskProject/Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
port = 5000


app.config['DEBUG'] = True


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, support_credentials=True)

@app.route("/")
def hello_world():
    return {"message":"hello world"}

@app.route("/register",methods=["POST"])
def register():
    body = request.json
    username = body["username"]
    password = body["password"]
    hash_salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), hash_salt)

    user_file = open("users.json","r")
    users = json.load(user_file)
    users.append({
        "username":username,
        "password":hashed_password.decode('utf-8'),
        "salt":hash_salt.decode('utf-8')
    })
  
    with open("users.json","w") as user_file:
        json.dump(users,user_file)

   
    

    return {
        "message":"success",
        "username":username,
        "password":hashed_password.decode('utf-8'),
    }

@app.route("/login",methods=["POST"])
def login():
    body = request.json
    username = body["username"]
    password = body["password"]
    user_file = open("users.json","r")
    users = json.load(user_file)
    for user in users:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
                payload = {
                
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiration time
                }
                token = create_jwt_token(payload)
                return {
                    "message":"success",
                    "token":token
                }
            else:
                return {
                    "message":"password incorrect"
                }

    return {
        message:"user not found"
    }







if __name__ == '__main__':
    app.run()




import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import threading
# from pyngrok import ngrok
from dotenv import load_dotenv
import bcrypt

# Load variables from the .env file into the script's environment

import numpy as np
from glob import glob

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

@app.route("/login",methods=["POST"])
def login():
    body = request.json
    username = body["username"]
    password = body["password"]
    hash_salt = os.getenv("HASH_SALT")
    hashed_password = bcrypt.hashpw(password, hash_salt)

    # print(username, password)
    

    return "Login route"







if __name__ == '__main__':
    app.run()




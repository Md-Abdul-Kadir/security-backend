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
from algorithms.rsa import encrypt
from algorithms.rsa import findP
from algorithms.rsa import decrypt
from algorithms.rsa import find_modular_inverse
from algorithms.ceaser_cipher import caesar_encryption
from algorithms.ceaser_cipher import caesar_decryption
from algorithms.vigenere import vig_enc, vig_dec
from algorithms.hill_cipher import encrypt,decrypt

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



@app.route("/rsa-encryption",methods=["POST"])
def rsa_encryption():
    body = request.json
    message = body["message"]
    e = body["e"]
    n = body["n"]

    encrypted_message = encrypt(message,e,n)
    
    
    return {
        "message":"success",
        "encrypted_message":encrypted_message
    }

@app.route("/rsa-decryption",methods=["POST"])
def rsa_decryption():
    body = request.json
    message = body["encrypted_message"]
    e = body["e"]
    n = body["n"]
    p = findP(n)
    q = n//p
    phi = (p-1)*(q-1)
    
    d = find_modular_inverse(e,phi)
   


    decrypted_message = decrypt(message,d,n)
    return {
        "status":"success",
        "decrypted_messsage":decrypted_message
    }


@app.route("/ceaser-cipher",methods=["POST"])
def ceaser_cipher():
    body = request.json
    message = body["message"]
    ceaser_cipher_key = os.getenv("CEASER_CIPHER_KEY")
    encrypted = caesar_encryption(message,int(ceaser_cipher_key))
    return {
        "status":"success",
        "encrypted_message":encrypted
    }

@app.route("/ceaser-cipher-decryption",methods=["POST"])
def ceaser_cipher_decryption():
    body = request.json
    message = body["encrypted_message"]
    ceaser_cipher_key = os.getenv("CEASER_CIPHER_KEY")
    decrypted = caesar_decryption(message,int(ceaser_cipher_key))
    return {
        "status":"success",
        "decrypted_message":decrypted
    }

@app.route("/vigenere-encryption",methods=["POST"])
def vigenere_encryption():
    body = request.json
    message = body["message"]
    
    key = os.getenv("VIGENERE_KEY")
    print("key",key)
    encrypted = vig_enc(message,key)
    return {
        "status":"success",
        "encrypted_message":encrypted
    }

@app.route("/vigenere-decryption",methods=["POST"])
def vigenere_decryption():
    body = request.json
    message = body["encrypted_message"]
    key = os.getenv("VIGENERE_KEY")
    decrypted = vig_dec(message,key)
    return {
        "status":"success",
        "decrypted_message":decrypted
    }

@app.route("/hillcipher-encryption",methods=["POST"])
def hillcipher_encryption():
    body = request.json
    message = body["message"]
    # key = body["key"]
    matrix = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
    key = 3
    encrypted = encrypt(message,key,matrix)
    return {
        "status":"success",
        "encrypted_message":encrypted
    }

@app.route("/hillcipher-decryption",methods=["POST"])
def hillcipher_decryption():
    body = request.json
    message = body["encrypted_message"]
    # key = body["key"]
    matrix = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
    key = 3
    decrypted = decrypt(message,key,matrix)
    return {
        "status":"success",
        "encrypted_message":decrypted
    }

# @app.route("/")

if __name__ == '__main__':
    app.run()




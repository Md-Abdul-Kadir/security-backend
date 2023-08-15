import jwt
import datetime

def create_jwt_token(payload):
    payload = {
        "user_id": 123,
        "username": "john_doe",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiration time
    }

    # Secret key for signing the JWT
    secret_key = "tondrabhalona"

    # Encode the JWT
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token

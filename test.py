import bcrypt

password = "super secret password"
password = password.encode("utf-8")
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(type(password))
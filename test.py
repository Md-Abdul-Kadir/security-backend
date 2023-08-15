import bcrypt
salt = bcrypt.gensalt()
print("salt",salt)
# Declaring our password
# password = 'GeekPassword'
 
# # Adding the salt to password
# salt = bcrypt.gensalt()
# print("salt",salt)
# salt = "hello".encode("utf-8")
# # Hashing the password
# hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
 
# # printing the salt
# print("Salt :")
# print(salt)
 
# # printing the hashed
# print("Hashed")
# print(hashed)
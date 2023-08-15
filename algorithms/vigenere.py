def key_make(text,key):
    key1= key
    n=len(key)
    m= len(text)
    i=0
    while(m>n):
        key1+= key[i%len(key)]
        i+=1
        n+=1
    return key1

def de(x,k):
    
    return chr((((ord(x)-ord('a'))-(ord(k)-ord('a')))%26)+ord('a'))

def en(x,k):
    return chr((((ord(x)-ord('a'))+(ord(k)-ord('a')))%26)+ord('a'))

def encryption(text,key):
    l = []
    i = 0

    for c in text:
        if c.isalpha():
            l.append(en(c,key[i]))
            i += 1
        else:
            l.append(c)

    ciphertext = ''.join(l)      
    return ciphertext

#Encryption
def vig_enc(text,key):
    
    # key = input("Enter key: ")
    # key =key_make(text,key)
    # print(key)
    ct=encryption(text,key_make(text,key))
    # print("cipher text "+ct)
    return ct

def decryption(text,key):
    l = []
    i = 0

    for c in text:
        if c.isalpha():
            l.append(de(c,key[i]))
            i += 1
        else:
            l.append(c)

    ciphertext = ''.join(l)      
    

    return ciphertext

#Decrypt
def vig_dec(text,key):
    # file_path = input('Input File name :')  # Replace with the actual path to your input file

    # Read the lines from the input file and store them in a list
    # with open(file_path, 'r') as file:
        # lines = file.readlines()

    # Combine the lines into a single text variable
    # text = ''.join(lines)
    # key = input("Enter key: ")
    ct=decryption(text,key_make(text,key))
    # print("Plain text "+ct)
    return ct
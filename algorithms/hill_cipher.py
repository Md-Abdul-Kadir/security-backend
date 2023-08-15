import numpy as np

def convert(s, k):
    ara = []
    for i in range(0, k * k, k):
        row = []
        for j in range(i, i + k):
            row.append(ord(s[j]) - 97)
        ara.append(row)
    return ara

def canDec(matrix):
    det = np.linalg.det(matrix)
    if det != 0:
        return True
    else:
        return False

def process(matrix, k):
    for i in range(k):
        for j in range(k):
            matrix[i][j] = (((matrix[i][j] % 26) + 26) % 26)
    return matrix

def mul(v, matrix, k):
    ans = []
    for i in range(k):
        x = 0
        for j in range(k):
            x += v[j] * matrix[j][i]
        x = ((x % 26) + 26) % 26
        ans.append(x)
    return ans

def encrypt(plain, k, matrix):
    cipher = ""
    for i in range(0, len(plain), k):
        v = []
        for j in range(i, i + k):
            v.append(ord(plain[j]) - 97)

        temp = mul(v, matrix, k)
        for j in range(len(temp)):
            cipher += (chr(int(temp[j]) + 97))
    return cipher

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return (x % m + m) % m

def decrypt(cipher, k, matrix):
    ans = ""
    det = int(np.linalg.det(matrix))
    det = ((det % 26) + 26) % 26
    det = inverse(det, 26)
    adj = np.linalg.inv(matrix) * np.linalg.det(matrix)
    adj = np.round(adj, decimals=3)
    adj = process(adj, k)
    for i in range(k):
        for j in range(k):
            adj[i][j] = (adj[i][j] * det) % 26
            adj[i][j] = int(adj[i][j])

    ans += encrypt(cipher, k, adj)
    return ans

# k = int(input('Enter key size: '))
# matrix = convert(str(input(f'Enter key string: ')), k)
# operation = input("Enter 'encrypt' or 'decrypt': ")

# # Read input from a text file
# # file_path = input("Enter the path of the input text file: ")
# try:
#     with open(file_path, 'r') as file:
#         input_text = file.read().strip()
# except FileNotFoundError:
#     print("Input file not found. Please provide a valid file path.")
#     exit(1)

# output_file_path = input("Enter the path for the output text file: ")

# if not canDec(matrix):
#     print('Enter a valid key')
# else:
#     matrix = process(matrix, k)
#     if operation == 'encrypt':
#         result_text = encrypt(input_text, k, matrix)
#     elif operation == 'decrypt':
#         result_text = decrypt(input_text, k, matrix)
#     else:
#         print("Invalid operation. Please enter 'encrypt' or 'decrypt'")
#         exit(1)

#     # Write the result to the output file
#     with open(output_file_path, 'w') as output_file:
#         output_file.write(result_text)

#     print("Operation completed successfully. Result written to the output file.")

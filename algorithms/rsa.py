def findP(n):
  for i in range(2,n+1):
    if ((n%i) == 0):
      return i
  return 1


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

def find_modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"The modular inverse of {a} modulo {m} does not exist.")

    return (x % m + m) % m

def bigmod(a, b, m):
    if b == 0:
        return 1 % m
    if b % 2 == 0:
        # If b is even, use the property (a^b) % m = ((a^(b/2)) % m * (a^(b/2)) % m) % m
        temp = bigmod(a, b // 2, m)
        return (temp * temp) % m
    else:
        # If b is odd, use the property (a^b) % m = (a % m * (a^(b-1)) % m) % m
        temp = bigmod(a, b - 1, m)
        return (a % m * temp) % m

def encrypt(m, e, n):
    encrypted_values = []
    for char in m:
        val = ord(char) - ord('a') + 1
        ans = bigmod(val, e, n)
        encrypted_values.append(ans)
    return encrypted_values

def decrypt(ch, d, n):
  s = ""
  for c in ch:
    ans = bigmod(c,d,n)
    print(ans)
    s+= chr(ans-1+ ord('a'))

  return s
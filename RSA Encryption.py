import sys

# extended Euclidean algorithm
# https://hackmd.io/@arutoria/BJIs-JA-H
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)

def modinv(a, m):
    g, x, y = egcd(a, m)    
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

print()
print("RSA Encryption")
print("---------------")

# input plaintext
pt = input("Please enter your plaintext: ")
print("---------------")
print("Convert input:")
print("    1. Original input:", pt)
pt = bytes(pt, "utf-8")
print("    2. Split into bytes:", pt)
pt = int(pt.hex(), 16)
print("    3. Convert into decimal:", pt)
print("---------------")

# input p and q -> compute N
# I hope that the user will input prime...... 
p = int(input("Please enter your prime p: "))
q = int(input("Please enter your prime q: "))
N = p * q
print("Your N is:", N)
print("---------------")

# https://stackoverflow.com/questions/10061626/message-length-restriction-in-rsa
# https://crypto.stackexchange.com/questions/71960/rsa-what-to-do-when-message-is-greater-than-n
if N < pt:
	print("Plaintext should not be greater than N")
	sys.exit()

# input e
e = int(input("Please enter your public key e: "))
phiN = (p - 1) * (q - 1)
d = modinv(e, phiN)
print("Your d is:", d)
print("---------------")

if ((p - 1) * (q - 1) <= e) or (e % 2 == 0):
	print("e should not be greater than φ(N) or be an even number")
	sys.exit()

# encryption
ct = pow(pt, e, N)
print("Ciphertext:", ct)
import sys

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

# input e
e = int(input("Please enter your public key e: "))
print("---------------")

if (p - 1) * (q - 1) <= e or e % 2 == 0:
	print("e should not be greater than φ(N) or be an even number")
	sys.exit()

# encryption
ct = pow(pt, e, N)
print("Ciphertext:", ct)
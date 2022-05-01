from Crypto.Util.number import long_to_bytes

def intToBytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, "big")

print()
print("RSA Decryption")
print("---------------")

# input ciphertext
ct = int(input("Please enter your ciphertext: "))
print("---------------")

# input d
d = int(input("Please enter your private key d: "))
print("---------------")

# input N
N = int(input("Please enter your N: "))
print("---------------")

# decryption
pt = pow(ct, d, N)
print("Plaintext:", intToBytes(pt))
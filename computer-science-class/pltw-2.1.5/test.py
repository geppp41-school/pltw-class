


def encrypt(key, n,  plaintext):
   #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(key, n, ciphertext):
    #Generate the plaintext based on the ciphertext and key using a^b mod m
 
  plain = [chr((int(char) ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
  return ''.join(plain)

Input = "password"
public = 31961
private = 21013
mod = 42781
Encripted = encrypt(public, mod, Input)

Decripted = decrypt(private, mod, Encripted)
print(Decripted)

#179
#239
#public 31961
#private 21013
#modulus 42781

#40524, 33083, 32436, 40524
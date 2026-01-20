#   a212_rsa_encrypt.py
import rsa as rsa


key = input("Enter the Encryption Key: " )
while(not key.isdigit()):
      print("not a valid key try again")
      key = input("Enter the Encryption Key: ")
key = int(key)

mod_value = input("Enter the Modulus: " )
while(not mod_value.isdigit()):
      print("not a valid mod try again")
      mod_value = input("Enter the Modulus: ")
mod_value = int(key)

plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)


## isalpha checks if a string only contians letters a-z and A-Z and returns True if true and False if false
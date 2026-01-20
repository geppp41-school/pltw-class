#   a212_generate_keys.py
import rsa as rsa

print("Generating your public/private keypairs now . . .")
keys = rsa.generate_keypair()
print("Public key: ", keys[0])
print("Private key: ", keys[1])
print("Modulus: ",keys[2])

#179
#239
#public 31961
#private 21013
#modulus 42781

#[30651, 10176, 6155, 30651, 6155]
#30651,10176,6155,30651,6155

#116, 101, 115, 116
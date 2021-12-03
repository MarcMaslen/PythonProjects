
### First first time use, you need to install module pycryptodome using the following commands (without #) in terminal:
# pip uninstall crypto
# pip install pycryptodome

from Crypto.PublicKey import RSA
from hashlib import sha512, sha256
import random


#The following function generateRSAKeys creates the RSA public/private key pair.
def generateRSAKeys(numBits):
    keyPair = RSA.generate(numBits)
    
    return keyPair


def digitalSignRSA(msg, keyPairRSA):

    # compute the hash value of the message to be signed with hash algorithm SHA-256
    hashValue = int.from_bytes(sha256(msg).digest(), byteorder='big')
    signature = pow(hashValue, keyPair.d, keyPair.n)

    return(hashValue, signature)

def checkOneNonce(numZerosNeeded, nonce):

    #convert the random integer to a byte array
    nByte = bytes(str(nonce), 'utf-8')

    # compute the hash of the nonce
    hash = int.from_bytes(sha256(nByte).digest(), byteorder='big')

    # convert the hash value to binary number and extract the needed LSBs.
    hashBin = bin(hash)
    hashLSB = int(hashBin[-numZerosNeeded:])

    # check if the LSBs are all zero
    if hashLSB == 0:
        print('nRand:', nonce, '; hash_lsb:', hashLSB)
    validity = (hashLSB == 0)
    return (validity)

numBits = 1024
keyPair = generateRSAKeys(numBits)
print("Public key:  n={", hex(keyPair.n), "}, e={", hex(keyPair.e), "})")
print('  ')
print("Private key: n={", hex(keyPair.n), "}, d={", hex(keyPair.d), "})")
print('  ')


# the nonce may be valid or may be invalid.
numZerosNeeded = 5
nonce = random.randint(0,1000000)
for validity in numZerosNeeded:
    validity = checkOneNonce(numZerosNeeded, nonce)
    print('The validity of this nonce ', nonce, ' is:', validity)
#print('================================================================  ')

msg = bytes('A message for signing', 'utf-8')
(hashValue, signature) = digitalSignRSA(msg, keyPair)
print("Hash value of message:", hashValue)
print("Signature:", hex(signature))
print('  ')


def digitalVerifyRSA(msg, keyPairRSA, signature):
    ### Verify the digital signature

    # compute the hash value of the message to be signed with hash algorithm SHA-256
    hashValue = int.from_bytes(sha256(msg).digest(), byteorder='big')

    # decrypt the signature of the message to obtain the hash value with RSA public key
    # everyone with RSA public key can perform the operation
    hashFromSignature = pow(signature, keyPair.e, keyPair.n)

    validity = (hashValue == hashFromSignature)
    return (validity)
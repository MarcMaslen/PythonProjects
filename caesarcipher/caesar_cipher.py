import sys

# the alphabet with all symbols in the set can be encrypted
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 


def caesar_cipher(message, mode, key):
    ciphertext = ''

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) index of this symbol in the LETTERS
            num = LETTERS.find(symbol) 
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            else:
                print('Correct operation mode is needed')
                exit()
            
            # handle the wrap-around if num is larger than the length of LETTERS or less than 0
            num = num % len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            ciphertext = ciphertext + LETTERS[num]

        else:
            ciphertext= ciphertext + symbol

  
    return ciphertext


def monoalphabetic_cipher(message, mode, key):
    return ciphertext



if __name__ == '__main__':

    numArgv = len(sys.argv) 
 
    message = 'a secret message.'

    key = 3
        
    if numArgv == 2:
        # get the message from the input given in the command line
        message = sys.argv[1]
    elif numArgv == 3:
        # get the message and key specified the input given in the command line
        message = sys.argv[1]
        key = int(sys.argv[2])

    elif numArgv > 3:
        # Instruction on providing message and key from command line
        print('+++Please input the exected message and key with correct format')
        print('+++python caesar_cipher.py my_message key') 
        print('+++where no space in my_message, key needs to be an integer for caesar cipher')
        
        print('+++For example: ')
        print('+++python caesar_cipher.py my_secrete_message 3')

        exit()
        

    # tells the program to encrypt or decrypt
    mode = 'encrypt' # set to 'encrypt' or 'decrypt'
    ciphertext = caesar_cipher(message, mode, key)       

    mode = 'decrypt'
    decrypttext = caesar_cipher(ciphertext, mode, key)


    ### Note: don't change the following code in your own program for displaying program outputs!!!
    print('##############################################')
    print('Cipher with key: ', key)
    print('##############################################')   
    print('Plain message: ', message)      
    print('Ciphertext: ', ciphertext)      
    print('Decrypted text: ', decrypttext)

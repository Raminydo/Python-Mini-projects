

"""
Caesar Cipher
This is a simple encoder/decoder project to convert a text into a ciphered text and also decipher encoded texts.
This process is based on Caesar cipher. Each letter is changed with another letter regarding a fixed number for steps.

e.g.
    input text: hi
    code number: 2
    encoded text: jk
    process:
        h -> j  (2 letters next)
        i -> k  (2 letters next)

    input text: jk
    code number: 2
    decoded text: hi
    process:
        j -> h  (2 letters before)
        k -> i  (2 letters before)

"""


from string import ascii_uppercase, ascii_lowercase
from os import system


res = []
valid = True

#region get info
data = input('Enter your text: ')

num = int(input('Enter code number: '))
num %= 26
#endregion

while True:
    system('cls')

    option = input('Choose your option (1. Encoder / 2. Decoder): ')

    if option == '1':

        #region encoder
        for char in data:
            
            if char == ' ':
                res.append(' ')

            elif char in ascii_lowercase:

                index = ascii_lowercase.find(char) + num
                if index > 25:          # 26 chars (0-25)
                    index -= 26
                res.append(ascii_lowercase[index])

            elif char in ascii_uppercase:
                
                index = ascii_uppercase.find(char) + num
                if index > 25:
                    index -= 26
                res.append(ascii_uppercase[index])

            else:

                valid = False
                break
        #endregion
            
        break


    elif option == '2':

        #region decoder
        for char in data:
            
            if char == ' ':
                res.append(' ')

            elif char in ascii_lowercase:

                index = ascii_lowercase.find(char) - num
                if index > 25:
                    index -= 26
                res.append(ascii_lowercase[index])

            elif char in ascii_uppercase:
                
                index = ascii_uppercase.find(char) - num
                if index > 25:
                    index -= 26
                res.append(ascii_uppercase[index])

            else:

                valid = False
                break
        #endregion
        
        break


system('cls')

if not valid:
    print('ERROR! Your text contains invalid characters')

else:
    print('Result:')
    print(*res, sep='')
                

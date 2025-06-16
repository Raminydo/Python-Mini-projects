

"""
This project is for checking items related to making a valid password.

The password must contains:
    - 4-9 characters
    - numbers
    - uppercase letter
    - lowercase letter
    - signs(special characters) or space

"""


from os import system

#region valid list
valid_list = []

for i in range(32, 127):
    valid_list.append(chr(i))
#endregion
 
#region signs list
sign_list = []

for i in range(32, 48):
    sign_list.append(chr(i))

for i in range(58, 65):
    sign_list.append(chr(i))

for i in range(91, 97):
    sign_list.append(chr(i))

for i in range(123, 127):
    sign_list.append(chr(i))
#endregion
   
while True:

    #region print message
    print('\nYour password must contain: ')
    print('4-9 characters')
    print('number')
    print('uppercase letter')
    print('lowercase letter')
    print('sign or space')
    #endregion

    password = str(input('\nEnter your password: '))

    check = 0

    system('cls')
    
    # checking invalid characters
    invalid = False

    for char, index in enumerate(password, 0):
        if password[char] not in valid_list:
            invalid = True

        else:
            pass
    
    if invalid == True:
        print('\nError! Your password contains invalid characters.')
    
    # checking length
    elif len(password) not in range(4, 10):
        print('\n  -Your password must contain 4-9 characters!')
    
    
    else:
              
        #region checking digits
        num_exists = False

        for char, index in enumerate(password, 0):
            if password[char].isdigit() == True:
                num_exists = True
                check += 1
                break
                
            else:
                pass

        if num_exists == False:
            print('  -Your password must contain at least one number!')
        
        else:
            pass
        #endregion

        #region checking uppercase
        uppercase_exists = False

        for char, index in enumerate(password, 0):
            if password[char].isupper() == True:
                uppercase_exists = True
                check += 1
                break
                
            else:
                pass

        if uppercase_exists == False :
            print('  -Your password must contain at least one uppercase letter!')

        else:
            pass
        #endregion

        #region checking lowercase
        lowercase_exists = False

        for char, index in enumerate(password, 0):
            if password[char].islower() == True:
                lowercase_exists = True
                check += 1
                break
                
            else:
                pass

        if lowercase_exists == False :
            print('  -Your password must contain at least one lowercase letter!')

        else:
            pass
        #endregion
        
        #region checking signs
        sign_exists = False

        for char, index in enumerate(password, 0):
            if password[char] in sign_list:
                sign_exists = True
                check += 1
                break
                
            else:
                pass
                

        if sign_exists == False :
            print('  -Your password must contain at least one sign or space!')

        else:
            pass
        #endregion

    if check == 4:
        break

    else:
        pass

system('cls')

print('  -Your password is accepted.')


    
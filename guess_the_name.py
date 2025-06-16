

"""
This is a small guess-the-name game project.
The game starts after entering the right password which is 0000.
Some names are given and one of them is chosen randomly by system.
The goal is to find the right name.

- if you enter wrong password for 5 times, you'll get out of the game.
- at the end, the 'correct answer', 'game count' and 'play time' will be shown.

"""

from os import system
from random import randint
from datetime import datetime


#region password

count = 1
password = '0000'

input_pass = input('Enter the password: ')


while count < 5 and input_pass != password:
    
    system('cls')

    print('Wrong password! Please try again. ( ', count, '/ 5 )')

    input_pass = input('Enter the password: ')

    count += 1 

#endregion


    
if input_pass != password: 
    system('cls')
    print('Wrong password! Please try again. ( ', count, '/ 5 )')      


#region game

else:

    continue_ = True

    while continue_:

        system('cls')

        print('One name is chosen. Guess it!')
        print('\n   1. Morad   2. Shabnam   3. Siroos   4. Pedram   5. Kobra')
        print('   6. Keyvan   7. Bizhan   8. Mousa   9. Mina   10. Arghavan')

        #region pc input

        name = randint(1, 10)

        #endregion
        
        start_time = datetime.now()
        count = 0


        #region user input

        flag = True

        while flag:

            input_ = int(input('\nEnter your guess (Your input should be number): '))


            if input_ in range(1, 11) and input_ != name:

                print('Your answer is wrong.')

                count += 1


            elif input_ in range(1, 11) and input_ == name:

                system('cls')
                print("You won!")
                
                count += 1
                finish_time = datetime.now()
                flag = False

            
            else:
                print('ERROR!')

                count += 1


            #endregion


        #region result
            
        match name:

            case 1:
                print('Correct answer: 1. Morad')
            
            case 2:
                print('Correct answer: 2. Shabnam')
            
            case 3:
                print('Correct answer: 3. Siroos')
            
            case 4:
                print('Correct answer: 4. Pedram')
            
            case 5:
                print('Correct answer: 5. Kobra')
            
            case 6:
                print('Correct answer: 6. Keyvan')
            
            case 7:
                print('Correct answer: 7. Bizhan')
            
            case 8:
                print('Correct answer: 8. Mousa')
            
            case 9:
                print('Correct answer: 9. Mina')
            
            case 10:
                print('Correct answer: 10. Arghavan')

                
        print('Game Count: ', count)
        print('Time: ', finish_time - start_time)

        #endregion


        #region again

        check = True

        while check:
            answer = input('\nDo you want to play again? (yes / no): ')

            if answer == "no":
                continue_ = False
                check = False
            
            elif answer == 'yes':
                check = False

            else:
                system('cls')
                pass

        #endregion


#endregion


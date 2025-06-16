

"""
The goal of this project is to convert a numeric number into text form in Persian(Farsi).

"""

from os import system

#region scales
scales = ['', 'هزار', 'میلیون', 'میلیارد', 'بیلیون', 'بیلیارد', 'تریلیون', 'تریلیارد',
          'کوآدریلیون', 'کادریلیارد', 'کوینتیلیون', 'کوانتینیارد', 'سکستیلیون', 'سکستیلیارد',
          'سپتیلیون', 'سپتیلیارد', 'اکتیلیون', 'اکتیلیارد', 'نانیلیون', 'نانیلیارد', 'دسیلیون',
          'دسیلیارد', 'آندسیلیون', 'آندسیلیارد', 'دودسیلیون', 'دودسیلیارد', 'تریدسیلیون', 'تریدسیلیارد',
          'کوادردسیلیون', 'کوادردسیلیارد', 'کویندسیلیون', 'کویندسیلیارد', 'سیدسیلیون', 'سیدسیلیارد', 'گوگول']


scale = 0
#endregion

res =[]

num = int(input('Enter a number: '))

if num == 0:
    system('cls')

    print(f'\nYour number: {num}\n')
    print('صفر')

else:

    num = f"{num:,}"
    num_list = num.rsplit(',')

    num_list = num_list[::-1]


    for index in range(len(num_list)):
        
        digits = int(num_list[index])

        ones = digits % 10
        tens = digits // 10 % 10
        tens_ = digits % 100            # 11-19
        hundreds = digits // 100

        if digits != 0:
            res.append('و')
            res.append(scales[scale])
            scale += 1

        else:
            scale += 1

        if tens_ in range(11, 20):

            match tens_:

                case 11:
                    res.append('یازده')
                case 12:
                    res.append('دوازده')
                case 13:
                    res.append('سیزده')
                case 14:
                    res.append('چهارده')
                case 15:
                    res.append('پانزده')
                case 16:
                    res.append('شانزده')
                case 17:
                    res.append('هفده')
                case 18:
                    res.append('هجده')
                case 19:
                    res.append('نوزده')

        else:

            match ones:

                case 1:
                    res.append('یک')
                case 2:
                    res.append('دو')
                case 3:
                    res.append('سه')
                case 4:
                    res.append('چهار')
                case 5:
                    res.append('پنج')
                case 6:
                    res.append('شش')
                case 7:
                    res.append('هفت')
                case 8:
                    res.append('هشت')
                case 9:
                    res.append('نه')


            if tens != 0 and ones != 0:
                res.append('و')
            

            match tens:

                case 1:
                    res.append('ده')
                case 2:
                    res.append('بیست')
                case 3:
                    res.append('سی')
                case 4:
                    res.append('چهل')
                case 5:
                    res.append('پنجاه')
                case 6:
                    res.append('شصت')
                case 7:
                    res.append('هفتاد')
                case 8:
                    res.append('هشتاد')
                case 9:
                    res.append('نود')  

            
        if hundreds != 0 and digits % 100 != 0:
            res.append('و')


        match hundreds:

            case 1:
                res.append('صد')
            case 2:
                res.append('دویست')
            case 3:
                res.append('سیصد')
            case 4:
                res.append('چهارصد')
            case 5:
                res.append('پانصد')
            case 6:
                res.append('ششصد')
            case 7:
                res.append('هفتصد')
            case 8:
                res.append('هشتصد')
            case 9:
                res.append('نهصد') 

          
    res[0] = ''         # remove last 'و'
    res = res[::-1]  

    system('cls')

    print(f'\nYour number: {num}\n')
    print(*res, sep=' ')
        

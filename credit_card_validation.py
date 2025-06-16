

"""
Credit Card Number Validation

e.g.
    input:
        1234-1234-1234-1234
        or
        1234 1234 1234 1234
        or
        1234123412341234

    output:
        Valid or Invalid


"""


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# remove spaces
cc = input("Enter your Credit Card number: ")
cc = cc.replace(" ","")
cc = cc.replace("-","")
cc = cc[::-1] # reverse card number

# sum odd numbers
for x in cc[::2]:
    sum_odd_digits += int(x)

# double every second digit
for x in cc[1::2]:   # index 1 is for the first second digit
    x = int(x) * 2  # doubling every digit
    if x >= 10:
        sum_even_digits += (1 + (x % 10))        # if  it is 2digits # each digit should be separated and summed
    else:
        sum_even_digits += x                     # if not then just sum


# sum
total = sum_odd_digits + sum_even_digits

# check
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")

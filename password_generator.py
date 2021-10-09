import random
import string

print('\nWelcome to Password generator!')

length = int(input('\nEnter the desired length of password: '))

if (length>=10 and length<=25):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols
    temp = random.sample(all,length)

    password = "".join(temp)
    print(password)
    
else:
    print("Error! The password should between 10 and 25 characters long")

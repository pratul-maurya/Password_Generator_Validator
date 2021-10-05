def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%', ' ', '!', '&','?', '*', '/']
    val = True
    count =0
    count+=1
    temp1='\0'
    temp='\0'
    for char in passwd:
        temp2=temp1
        temp1=temp
        temp=char
        if char==temp2:
              print('More than 2 identical characters in a row')
              val = False

    if len(passwd) < 9:
        print('length should be at least 9')
        val = False
          
    if len(passwd) > 26:
        print('length should be not be greater than 26')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one number')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

def main():
    passwd = input("Enter your password ")
      
    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
                
if __name__ == '__main__':
    main()

#Task Five: File Handling and Exception Handling
import sys
#Question 1

def syntax_try():
    try:
        a = "1234" * "123"
        print(a)
    except:
        print('This is an incomplete string')
        

#Question 2
        
def open_file():
    
    try:
        
        filename = str(sys.argv[0])
        txt = open(filename, 'r')
        print(txt)
        
    except:
        
        filename = input('Please input the proper file name again:')
        txt = open(filename, 'r')
        print(txt)
        

#Question 3
        
def len_error():
    
    file = str(input('Please enter a username: '))
    
    while len(str(file)) > 4:
        file = str(input('Please length is too long!!! Please provide only four digits:'))
    
    return file
    

#Question 4

def login_backend():
    

    passwordcounter = 0
    
    
        
    username_inp = str(input('Please enter username: '))
    retype_username = str(input('Please re-enter username: '))
            
    while passwordcounter <= 3:
    
        if username_inp == retype_username:
            
            password_inp = str(input('Please enter password: '))
            retype_password = str(input('Please re-enter password: '))
            
            passwordcounter += 1
            
        if password_inp == retype_password:
            break
                
        elif password_inp != retype_password and passwordcounter <= 3:
            print('passwords do not match! Please try again')
            continue
        
        if username_inp != retype_username:
            print('Usernames do not match! Please try again')
            continue
    
    if passwordcounter > 3:
        print('Incorrect password entered too many times. Login failed.')
        
    else:
        print('Login Successful!')
                


                
#Question 6
                        

def open_even():
    
    file_even = open('doc.txt', 'r')
    read_file = file_even.readlines()
    for i in range(0, len(read_file)):
        
        if i%2 == 0:
            print(read_file[i])
        
            
        
    
        

    

        
        
        
    
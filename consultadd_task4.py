#Task 4: Higher Order Functions, Generators, List Comprehension and Decorator Questions


#Question 1

def notdiv3_mult7(input_list):
    input_list = filter(lambda x:x%3 != 0, input_list)
    input_list = filter(lambda x:x%7 == 0, input_list)
    
    return list(input_list)

#Question 2 come back to this

def mult_list(int_square):

    return(int_square**2) 

def map_list(list_a):
    return list(map(mult_list, list_a))


#Question 3

def find_upper(stringy):
    return [char for char in stringy if  char.isupper() == True]

#Question 4

Student = ['Smit', 'Jaya', 'Rayyan']
Capital = ['CSE', 'Networking', 'Operating System']

def into_dict(x, y):
    return dict(zip(x,y))

into_dict(Student, Capital)

#Question 5
#This isnt a question

#Question 6

input_string = 'Consultadd Training'

def rev_list_gen(inp_string):
    new_string = ''
    for i in range(len(inp_string)-1,  -1, -1):
        new_string = new_string + inp_string[i]
        yield new_string
    
def rev_string():
    for i in rev_list_gen(input_string):
        print(i)
    
rev_string()

#Question 7

def decorator_function(example_function):
    def another_func():
        print('Here is my decorator function.')
        
        example_function()
        
        if isinstance(example_function(), str) == True:
            print('The inserted function is a string')
            
        elif isinstance(example_function(), str) == False:
            print('The inserted function is not a string')
        
    return another_func()

def insert_func():
    a = 'I am a string'
    print(a)
    return a

insert_func = decorator_function(insert_func)

#Question 8
# 5 Front end technologies are HTML, CSS, Javascript, Bootstrap Framework, ReactJS
# Some companies which use these technologies are Jobot, Amazon, and BerkleyNet
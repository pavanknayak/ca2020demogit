#Weekend activity on functions
import functools
#Question 1

def rev_string(input_string):
    return input_string[-1::-1]

#Question 2

def upper_lower(input_string):
    num_upper = 0
    num_lower = 0
    
    for i in range(0, len(input_string)):
        if input_string[i].isupper() == True:
            num_upper +=1
        elif input_string[i].islower() == True:
            num_lower +=1
            
    print('No. of upper case characters: ', str(num_upper))
    print('No. of lower case characters: ', str(num_lower))
    


#Question 3
    
def unique_elem(input_list):
    return list(set(input_list))

#Question 4

def hyphen_sort(input_string):
    hyphen_list = input_string.split('-')
    hyphen_list = sorted(hyphen_list, key = str.lower)
    return(hyphen_list)

#Question 5

def uppercase(input_string):
    return input_string.upper()

#Question 6

def intstr_sum(str1, str2):
    return int(str1) + int(str2)

#Question 7

def max_len_str(str1, str2):
    
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    elif len(str1) == len(str2):
        print(str1)
        print(str2)
        
#Question 8

def tup_square():
    a = list(range(1, 21))
    
    for i in range(0, len(a)):
        a[i] = a[i]**2

    return tuple(a)
    
#Question 9

def showNumbers(limit):
    
    for i in range(0, limit+1):
        
        if i == 0:
            print(i, ' EVEN')
        
        elif i %2 == 0:
            print(i, ' EVEN')
            
        elif i%2 != 0:
            print(i, ' ODD')
            
#Question 10
            
def filt_list():
    
    elem_list = list(range(1, 21))
    
    return list(filter(lambda x: x%2 == 0, elem_list))
    
    
#Question 11

def map_filt():
    
    elem_list = list(range(1, 11))
    elem_list = list(filter(lambda x: x%2 == 0, elem_list))
    elem_list = list(map(lambda x: x**2, elem_list))
    return elem_list

#Question 12

def div_zero():
    
    try:
        print(5/0)
    except:
        print("dividing by zero is impossible")
        
#Question 13
        
def red():
    a = [[1,2,3],[4,5],[6,7,8]]
    a = functools.reduce(operator.concat, a)
    print(a)
    for x in range(0, len(a)):
        a[x] = str(a[x])
    
    return functools.reduce(operator.concat, a)

#Question 14

#first code will return 2
#second code will return 'after f' in the console once because the f function has not been defined
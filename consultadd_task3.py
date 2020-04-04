#Consultadd Task 3

import numpy as np
import random

#Question 1

data_type_element = [3, 4.1, -2**0.5, "this is a string", 5, 3.2, "string2", 4, 2, 1]

#Question 2

slice_list = [2, 4, 6, 8, 10, 12, 14]
slice1 = slice_list[:4]

#Question 3

def sum_and_multiply(inp_list):
    sum_list = sum(inp_list)
    mult_list = numpy.prod(inp_list)
    return sum_list, mult_list

#Question 4

max(slice_list)
min(slice_list)

#Question 5

new_list = list(range(1, 250))
new_list2 = []
for a in range(0, len(new_list)):
    if new_list[a] % 2 != 0:
        new_list2.append(new_list[a])
        

print(new_list2)

#Question 6


norm_list = list(np.array(range(1,31))**2)

#Question 7

def list_in_list(inputlist):
    another_list = random.sample(range(1,50), 8)
    inputlist[-1] = another_list
    return inputlist

#Question 8

def concat_dict():
    a = {1:10,2:20}
    b = {3:30,4:40}
    c = {}
    c.update(a)
    c.update(b)
    return c
    
#Question 9

def exp_dict(n):
    
    samp_dict = {}
    for i in range(0, n+1):
        samp_dict[i] = i**2
    
    return(samp_dict)

#Question 10

def list_tuple():
    
    csv = input("Input a list of comma separated values, with no spaces")
    
    return list(csv), tuple(csv)
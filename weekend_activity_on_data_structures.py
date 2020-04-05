#Weekend activity on data structures


#Question 1

data_type_element = [3, 4.1, -2**0.5, "this is a string", 5, 3.2, "string2", 4, 2, 1]

#Question 2

slice_list = [2, 4, 6, 8, 10, 12, 14]
slice1 = slice_list[:4]

#Question 3

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

list1 = x[5][:4]
list2 = x[6:8]
list3 = x[0::2]
list4 = x[::-1]
list5 = x[5][5][0]
list6 = []

#Question 4

thou_a = list(range(1, 1000))
thou_b = range(1,1000)
#In python 3, xrange does not exist. In python 2, xrange is more memory efficient than range

#Question 5

#Tuple is immutable, while list is mutable. Tuples can also be used as keys for dictionary. Tuples are also more memory efficient than lists


#Question 6

def div3mult2():
    thoub = range(1, 1001)
    thou_list = []
    for i in thoub:
        if i % 3 == 0 and i %2 == 0:
            thou_list.append(i)
            
    return thou_list


#Question 7

def rev_vowel(inp_str):
    vowel_list  = ['a', 'e', 'i', 'o', 'u']
    rev_str = inp_str[-1::-1]
    vowel_count = []
    vowel_str = ''
    for i in range(0, len(rev_str)):
        if rev_str[i] in vowel_list:
            vowel_count.append(i)
            vowel_str = vowel_str + rev_str[i]
            
    return vowel_count, vowel_str

#Question 8

def even_word():
    even_str = 'hello my name is abcde'
    even_split = even_str.split(' ')
    even_list = []
    for i in range(0, len(even_split)):
        if len(even_split[i]) %2 == 0:
            even_list.append(even_split[i])
    return even_list

#Question 9

def sum_8():
    x = [1,2,3,4,5,6,7,8,9,-1]
    pair_list = []
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            
            if x[i] + x[j] == 8:
                pair_tup = (x[i], x[j])
                pair_list.append(pair_tup)
    return pair_list

#Question 10

def odd_even():
    even_list = []
    odd_list = []
    
    while len(even_list)<= 5 or len(odd_list) <= 5:
        
        ask = int(input('Please input a number between 1 and 50:'))
        
        if ask %2 == 0:
            even_list.append(ask)
            
        elif ask %2 != 0:
            odd_list.append(ask)
            
        if len(even_list) == 5 or len(odd_list) == 5:
            break
        
    if len(even_list) == 5:
        print("The maximum even number was: ", max(even_list))
        print("The sum of even numbers was: ", sum(even_list))
    
    elif len(odd_list) == 5:
        print("The maximum odd number was: ", max(odd_list))
        print("The sum of odd numbers was: ", sum(odd_list))
   

#Question 11
        
def find_letters(alphanum_str):
    alpha_dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0,
                  'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0,
                  'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    
    alpha_list = []
    for i in range(0, len(alphanum_str)):
        if alphanum_str[i] in alpha_dict:
            alpha_dict[alphanum_str[i]] += 1
            
    for j in alpha_dict:
        if alpha_dict[j] > 0:
            alpha_list.append(str(j) + ' = ' + str(alpha_dict[j]))
    print(alpha_list)
            

#Question 12
    
def even_tuple():
    trial_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even_tup = []
    
    for i in range(0, len(trial_tup)):
        if trial_tup[i] %2 == 0:
            even_tup.append(trial_tup[i])
            
    even_tup = tuple(even_tup)
    
    return even_tup
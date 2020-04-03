#Consultadd Training Task 2

#Question 1
def divisible_by_three(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Consultadd Python Training")
    elif number % 3 == 0:
        print("Consultadd")
    elif number % 5 == 0:
        print("c")

#Question 2

def userenter(entry, first1, second2):
    if entry == 1:
        x = first1 + second2
        print(x, "\n")
        if x < 0:
            print("zsa")
    elif entry ==2:
        x = first1 - second2
        print(x, "\n")
        if x < 0:
            print("zsa")
    elif entry == 3:
        x = first1/second2
        print(x, "\n")
        if x < 0:
            print("zsa")
    elif entry == 4:
        x = first1*second2
        print(x, "\n")
        if x < 0:
            print("zsa")
    elif entry == 5:
        num1 = input("enter 3rd number for average:")
        num2 = input("enter 4th number for average:")
        num1 = float(num1)
        num2 = float(num2)
        x = (first1+second2+num1+num2)/4
        print(x, "\n")
        if x < 0:
            print("zsa")
        
#Question 3


def flowchart(a, b, c):
    avg = (a+b+c)/3
    print("avg =", avg)
    
    if avg > a and avg > b and avg > c:
        print("avg is higher than a, b, c")
    elif avg > a and avg > b and avg < c:
        print("avg is higher than a, b")
    elif avg > a and avg < b and avg > c:
        print("avg is higher than a, c")
    elif avg < a and avg > b and avg > c:
        print("avg is higher than b, c")
    elif avg > a and avg < b and avg < c:
        print("avg is just higher than a")
    elif avg < a and avg > b and avg < c:
        print("avg is just higher than b")
    elif avg <a and avg < b and avg > c:
        print("avg is just higher than c")

#Question 4

def break_cont(number):
    while number>0:
        print("Good Going")
        continue
    
    while number<0:
        break
    print("It's Over")
    
#Question 5
def div7mult5():
    listname = []
    for x in range(2000, 3201):
        if x % 7 == 0 and x % 5 !=0:
            listname.append(x)
    print(listname)

#Question 6
    
#part 1: you cannot iterate through int type object, needs to be list or string, etc..
#part 2: 0, 1, 2, 3
#part 3: 0, 1, 2, 3, 4, 5
    
#Question 7

def printnum():
    for x in range(0, 6):
        if x != 3 and x != 6:
            print(x)

#Question 8
def numdiglet(inputstring):
    digitcount = 0
    lettercount = 0
    for i in inputstring:
        if i.isdigit() == True:
            digitcount +=1
        else:
            lettercount += 1
    print("Letters" ,lettercount)
    print("Digits", digitcount)

#Question 9
def guesslucky():
    number = 12
    answer = input("Guess the lucky number:")
    if int(answer) == number:
        print("you guessed it")
        return
    
    while answer != number:
        print("no")
        folanswer = input("Guess again:")
        if folanswer.lower() == "no":
            break
        elif int(folanswer) == number:
            print("you guessed it")
            break
        else:
            continue
        

#Question 10

def guessluckycount():
    number = 12
    answer = input("Guess the lucky number:")
    counter = 0
    if int(answer) == number:
        print("Good Guess!")
        return
    
    while answer != number:
        counter +=1
        print("no")
        print("this is try number: ", counter)
        folanswer = input("Guess again:")
        if folanswer.lower() == "no":
            break
        elif int(folanswer) == number:
            print("Good Guess!")
            break
        if counter == 5:
            print("Game Over")
            break
        else:
            continue
        
#Question 11
#Same as Question 10        
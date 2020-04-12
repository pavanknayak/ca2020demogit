#Consultadd Task 6

#Question 1

def square_val(D):
    
    C = 50
    H = 30
    
    Q = ((2*C*D)/H)**0.5
    
    return Q

def map_square_val(D):
    
    return map(square_val, D)


#Question 2

class Shape:
    def shape_area(self, measurement):
        return 0
    
    class Square:
        
        def __init__(self, measurement):
            self.measurement = measurement
            
        def square_area(self):
            return self.measurement*self.measurement
        

#Question 3
        
class tri_element:
    def __init__(self, listofnums):
        self.listofnums = listofnums
        
    def sum_to_zero(self):
        
        sum_list_list = []
        for i in range(0, len(self.listofnums)-2):
            for j in range(i+1, len(self.listofnums)-1):
                for k in range(j+1, len(self.listofnums)):
                    
                    if self.listofnums[i] + self.listofnums[j] + self.listofnums[k] == 0:
                        sum_list = [self.listofnums[i], self.listofnums[j], self.listofnums[k]]
                        sum_list_list.append(sum_list)
                        
        print(sum_list_list)
        
    
#Question 4

#Part 1
#the code would return an error because the derived_test instance called b has no x attribute, only a y attribute

#Part 2
#The code would print 1 2 because the der class uses the super() function to inherit the init function from the A class. since x is 1 and y is 2
        
#Part 3
#The code would return 3 1 because the B class inherits the x value from the A init, but the new count function in the B class adds a count to y making it 1
        
#Part 4
#The code would return 30 because the new multiply function overwrites the inherited A multiply function and calling the new multiply function multiplies the input 15 by 2
        


#Question 5
        

class Time:
    
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        
    def DisplayMinute(self):
        
        totalmin = self.hours*60 + self.minutes
        
        print(str(totalmin) + ' minutes')
        
        return totalmin
    
    def DisplayTime(self):
        
        totaltime = str(self.hours) + ' hours and ' + str(self.minutes) + ' minutes'
        return totaltime
    
    def addTime(self, otherobj):
        
        totalmintime = self.DisplayMinute() + otherobj.DisplayMinute()
        
        totaltimetime = '(' + self.DisplayTime() + ')' + ' + ' + '(' + otherobj.DisplayTime() + ')' + ' is ' + str(int((totalmintime - totalmintime%60)/60)) + ' hours and ' + str(totalmintime%60) + ' minutes'
        
        return totaltimetime


#Question 6
    
class Person:
    
    def __init__(self, age):
        self.age = age
        
        if self.age <0:
            print('Age is not valid, setting age to 0.')
            
            self.age = 0
        
    def yearPasses(self):
        
        self.age += 1
        
    def amIOld(self):
        
        if self.age < 12:
            print('You are Young.')
            
        elif self.age > 12 and self.age < 20:
            print('You are a teenager.')
            
        elif self.age >= 20:
            print('You are Old.')
            

        

    
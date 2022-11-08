##Homework1 
## Shay Hahiashvili , id: 206423840
## Maxim Subotin , id: ?

#Task1





print("hello")



#Task2




#Task3

def sort_num(x):
   ''' return true if the given number's members are in accending order'''
   if x>0:
       if x%10 >= (x//10)%10: #if true we continue to next set of members 
           return sort_num(x//10)
       else:
           return False #if members aren't in the right order we return false
   else:
        return True #else it means we went through all members and we return true
        

#if sort_num(24889) == True: #check for sort_num func
#    print("Yes")
#else:
#    print("no")


#Task4





#Task5

def unique(x):
    '''func that checks if string's members are shown only once'''
    
    for i in range(0,len(x)): 
        temp = x[i] # saves temp to check with the rest of the members
        for j in range(i+1,len(x)):
              if x[j] == temp: #if true it means we found a member twice and we return false
                  return False

    return True #else we know we ran through all members and we return true


#if unique('32450') == True: #check for unique func
#    print("Yes")
#else:
#    print("no")


#Task6

def Xnor(x,y):
    '''Xnor func'''
    if (x == True and y == True) or (x == False and y == False): #checks if both values are same
        return True
    else:
        return False


print(Xnor(True,False)) #checks Xnor func

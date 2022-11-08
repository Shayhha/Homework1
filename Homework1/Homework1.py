##Homework1 
## Shay Hahiashvili , id: 206423840
## Maxim Subotin , id: 207695479

#Task1

def even_str(word):
    '''even_str gets a string, and returns the all the letters that are in the EVEN position, returns a string.'''
    return word[1::2] # 1 stands for starting on the second letter, and 2 stands for jumping 2 indexes.


#print(even_str('Python')) # checking that the function even_str works.



#Task2

def pattern(n):
    '''prints a pattern of stars with a gap in the middle. n represents the number of rows.'''
    # variable decleration
    i = 1
    word = '*'

    while i <= n: # outside loop is for printing rows.
        j = i*2 # j is the number of stars in row number i
        k = (n*2)-j # k is the number of spaces in row number i
        while j > 0: # first inner loop is for printing stars in each row.
            if j == i: # if we have allready printed exactly half of the stars for this row, go ahead and print all the spaces.
                while k > 0: # second inner loop is for printing all the spaces at ones in each row.
                    print(' ',end='')
                    k-=1
            print(word,end='')
            j-=1
        print()
        i+=1
        

#pattern(5) # testing that the pattern function works



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

def min_dig(n):
    '''min_dig gets a number and returns the lowest digit in that number.'''
    if n<10: # if the number is a single digit, return it as it is the lowest.
        return n
    else: # else, keep units digit in the variable m and the next digit in k.
        m = min_dig(n//10)
        k = n % 10
        if m < k: # then compare the two digits. returns m if its the min digit, other wise returns the current min digit which is k.
           return m 
        return k


#print(min_dig(93163)) # testing that the pattern function works



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


#print(Xnor(True,False)) #checks Xnor func
















#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

#####################
## -- SOLUTION 1 -- ##
#####################
def array_check(list) :
    for i in range(len(list) - 2):
        if list[i] == 1 and list[i+1] == 2 and list[i+2] == 3 : 
            print (True)

        print (False)
           
array_check([1, 1, 2, 3, 1])
# array_check([1, 1, 2, 4, 1])
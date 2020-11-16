###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

import random


guess = input("Enter 3 digits to find the correct number: ")
digits = list(range(10))
""" Generate 3 digits"""
digits = [str(nums) for nums in list(range(10))] 
digits = random.shuffle(digits)
print(digits)
# print(digits[:3])225
start = True
while(start) :
    for i in range(len(digits)) :
        if guess[i] == digits[:3][i] and guess[i+1] == digits[:3][i+1] and guess[i+2] == digits[:3][i+2] :
            print(" Match: You've guessed a correct number in the correct position")
            print(digits[:3])
            start = False
        elif guess[i] == digits[:3][i] and guess[i+1] == digits[:3][i+1] :
            print(" Match: You've guessed a correct number in the correct position")
        else :
            print("  Nope: You haven't guess any of the numbers correctly")

"""
Find the LCM of 24 and 36
PPCM
"""
x,y = 60, 168
count = True
i = 1
while count :
    if i % x == 0 and i % y == 0 :
       
        print ( "The LCM of {} and {} is {}".format(x, y, i) )
        
        count = False
    i= i+1
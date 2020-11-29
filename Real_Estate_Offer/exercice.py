print('Enter your first Offer on the house.')
offer = abs(int(input()))

print('Enter your best offer on the house')
best_offer = abs(int(input()))

print('How much more do you want to offer each time?')
increment = abs(int(input()))

offer_accepted = False

while offer <= best_offer :
    if offer >= 650000 :
        offer_accepted = True
        print("Your offer {} has been accepted ".format( offer ))
        break
    
    print("We \'re sorry, you\'re offer of {} has not been accepted.".format( offer ))
    
    offer += increment
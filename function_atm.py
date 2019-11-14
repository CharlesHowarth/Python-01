acc_pin = 1234
balance = 250

def withdraw( pin, amount):

    if pin != acc_pin:
        print("Incorrect Pin")
    elif amount > balance:
        print("You can only withdraw " + str(balance))
    else:
        new_balance = balance - amount
        print ("Prev Balance = {}. You have withdrawn {}. New balance is {}".format(balance,amount,new_balance))
    
withdraw(1234,100)

print("")

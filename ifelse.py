#write a program to calculate the amount left in the bank account after taking some amount 
bankbalance = 10000
amount = int(input("Enter the amount: "))
if (amount<=bankbalance):
    bankbalance = bankbalance - amount
    print("Withdrew has been successful, now your balance is ", bankbalance)
else:
    print("Can't ask for more than your bank balance", bankbalance)

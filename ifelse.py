bankbalance = 10000
amount = int(input("Enter the amount: "))
if (amount<=bankbalance):
    bankbalance = bankbalance - amount
    print("Withdrew has been successful, now your balance is ", bankbalance)
else:
    print("Can't ask for more than your bank balance", bankbalance)

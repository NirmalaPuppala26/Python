//Write a progam to calculate the current or power bill in India using python
pmr = int(input("Enter the PMR value: "))
cmr = int(input("Enter the CMR value: "))
unitsConsumed = cmr-pmr
if (unitsConsumed <=100):
    billAmount = unitsConsumed*2
    print("Amount: ",billAmount)
elif (unitsConsumed <=300):
    billAmount = unitsConsumed*3
    print("Amount: ",billAmount)
elif (unitsConsumed <=500):
    billAmount = unitsConsumed*5
    print("Amount: ",billAmount)
elif (unitsConsumed >500):
    billAmount = unitsConsumed*10
    print("Amount: ",billAmount)
    

height = int(input("Enter the height of the candidate in inches: "))
runtime = int(input("Enter the running time of the candidate in seconds: "))
marks = int(input("Enter the marks of the candidate out of 100: "))

if height >= 165:
    print("You have qualified for the height criteria.")
    
    if runtime <= 14:
        print("You have qualified for the running time criteria.")
        
        if marks >= 70:
            print("Congratulations! You are selected.")
        else:
            print("Sorry! Better luck next time. Your marks are too low.")
    else:
        print("Sorry! Better luck next time. Your running time is too high.")
else:
    print("Sorry! Better luck next time. You don't meet the height criteria.")

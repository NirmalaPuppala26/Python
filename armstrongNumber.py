n = int(input("Enter a number: "))
t=n
sum=0
while(n!=0):
    r = n%10
    sum = sum +(r*r*r)
    n = n//10
if(sum == t):
    print("The given number is a armstrong number")
else:
    print("The given number is not a armstrong number")

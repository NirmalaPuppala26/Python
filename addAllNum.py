#Write a program to find the sum of all the digits
n = int(input("Enter a number: "))
sum = 0
while(n!=0):
    r = n%10
    sum = sum + r
    n=n//10
print("Sum of all digits: ",sum)

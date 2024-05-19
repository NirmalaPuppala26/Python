#write a program which reads a number and finds the sum of it's first and last digits only.
n = int(input("Enter a number: "))
fd = n
ld = n%10
while (n>=10):
    n=n//10
sum = n+ld
print("Result: ",sum)

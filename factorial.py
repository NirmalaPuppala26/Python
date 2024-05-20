#Write a program to find the factorial of a number
n = int(input("Enter a number: "))

f = 1
for i in range (2,n+1):
    f = f*i
print("Factoial of %d: %d"%(n,f) )

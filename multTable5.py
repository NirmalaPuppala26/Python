#write a program to give multiplication tables from 1 to 5
import sys
n = int(input("Enter a number: "))

if (n>5):
    print("Enter a number which is <=5")
    sys.exit()
for i in range(1,21):
    for j in range(1,n+1):
        print("%d * %2d = %3d" %(j,i,i*j), end="\t")
    print()

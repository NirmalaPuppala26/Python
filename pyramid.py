#write a program to print a pyramid
n = int(input ("Enter input number: "))
for i in range(n,0,-1):
    for j in range (i,0,-1):
        print(j, end='')
    print()




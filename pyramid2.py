#write a porgram to print a pyramid
n = int(input("Enter number: "))
for i in range(0, -1):
    for j in range(1, n + 2 - i):
        print(j, end='')

    print()

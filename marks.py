#Write a program to see the students result in class when marks are entered
marks = int(input("Enter your marks: "))
if (marks >=60):
    print("Result- First Class")
elif (marks >=50):
    print ("Result-second class")
elif (marks >=35):
    print ("Result-Third class")
else:
    print("Failed")

a=int(input("Enter your Physics marks: "))
b=int(input("Enter your Chemistry marks: "))
c=int(input("Enter your Maths marks: "))
d=int(input("Enter your Hindi marks: "))
e=int(input("Enter your English marks: "))
Total_marks=a+b+c+d+e
Percentage=(Total_marks/500)*100
print(f"Your percentage is {Percentage}")
print("If you need your Result in grade so say yes/No")
message=input("Enter your answer YES/No:")
if (message=="YES"):
    if (Percentage>=91) or (Percentage<=100):
        print("Great!Your grade is A1.")
    elif (percentage>=81) or (Percentage<=90):
        print("Very good!Your grade is A2.")
    elif (Percentage>=71) or (Percentage<=80):
        print("Good!Your grade is B1.")
    elif(Percentage>=61) or (Percentage<=70):
        print("Better!Your garde is B2.")
    elif (Percentage>=51) or (Percentage<=60):
        print("Not Bed!But improve your self.Your grade is B2.")
    elif (Percentage>=41) or (Percentage<=50):
        print("Do Study Hard!.Your grade is C1.")
    elif (Percentage>=31) or (Percentage<=40):
        print("Fail!")
    else:
        print("By By")
else:
    print("Okay Thank You!")

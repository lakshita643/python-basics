print("CALCULATOR!")
a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
d=0
c=input("Enter Your Choice(+,-,/,*):")
if c=="+":
    d=a+b
    print(f"Addition is {d}.")
elif c=="-":
    d=a-b
    print(f"Substraction is {d}.")
elif (c==" \ "):
    d=a/b
    print(f"Division is {d}.")
elif (c=="*"):
    d=a*b
    print(f"Multiply is {d}.")
else:
    print("Okay!")
    

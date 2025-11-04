# calculator

a = int(input("enter first number"))
op = input("enter operator")
b = int(input("enter second number"))
        

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("invalid operator")


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b


x = int(input("Ënter the first number: "))
y = int(input("Enter the second number: "))
op = input("Enter an operator [+,-,X,/]: ")


if op == "x":
    res = add(x,y)
    print(f"{x} + {y} = {res}")
    
    
if op == "+":
    res = add(x,y)
    print(f"{x} + {y} = {res}")
    
    
elif op == "-":
    res = sub(x,y)
    print(f"{x} - {y} = {res}")
    
    
elif op == "x":
    res = mult(x,y)
    print(f"{x} x {y} = {res}")
    
    
elif op == "/":
    res = div(x,y)
    print(f"{x} / {y} = {res}")
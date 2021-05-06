x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
ch = (input("Enter operation to be performed: "))
def calculator():
    if(ch == '+'):
        def add(a,b):
            return a + b
    elif(ch == '-'):
        def sub(a,b):
            return a-b
    elif(ch == '*'):
        def mlp(a,b):
            return a*b
    else:
        def div(a,b):
            return a/b
if(x==45 and y==3 and ch== '*'):
    print("555")
elif(x==56 and y==9 and ch== '+'):
    print("71")
elif(x==56 and y==6 and ch== '/'):
    print("4")
else:
    calculator()
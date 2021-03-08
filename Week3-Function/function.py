#built-in functions
a = 100
b = 211
print(max(a, b))
print(min(a, b))

c = 10.45
d = int(c)
print(d)

e = "Python"
print(type(e))


#user defined function
def add(a, b):
    c = a + b
    return c

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
d=add(a,b)
print("The sum is", d)



#function with multiple parameters
def divisor(x,y,m):
    if x%m==0 and y%m==0:
        print("%d & %d are divisible by %d"%(x,y,m))
    elif x%m==0:
        print("only %d is divisible by %d"%(x,m))
    elif y%m==0:
        print("only %d is divisible by %d"%(y,m))
    else:
        print("none of %d & %d is divisible by %d"%(x,y,d))

divisor(10,20,5)
divisor(12,20,5)
divisor(10,22,5)
divisor(2,5,3)



#function without parameter
def summation():
    a=3+8
    return a

b=summation()
print(b)


#function with default parameter value
def check(a=0):
    if a==0:
        print("Zero")
    elif a>0:
        print("Positive")
    else:
        print("Negative")

check() #without parameter
check(-4) #with parameter


#local scope
def local_scope():
    x=7
    print(x)
local_scope()
print(x)


#local scope
def local_scope():
    x=7
    return x
a=local_scope()
print(a)
print(x)



#global scope
x=10
def global_scope():
    print(x)
print(x)
global_scope()


#global scope
def global_scope():
    global x
    x=10
global_scope()
print(x)


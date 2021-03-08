# The built-in input function requests and obtains user input:
name = input("What's your name?")
print(name)

#python takes input as a string we have to type cast the input
value1 = input("Enter first number: ")
value2 = input("Enter second number: ")

total = value1 + value2
print(total)
print(type(total)) 

#type casting to int format
total = int(value1) + int(value2)
print(total)

# Getting an Integer from the User by casting the input format
another_value = int(input("Enter another integer: "))
print(another_value)


# Taking multiple input from the user
a, b = input().split()
print(a, b)
print(type(a))


##########Solving Problem##########
# Determining the Minimum and Maximum with Built-In Functions min and max

number1 = int(input("Enter first intefer: "))
number2 = int(input("Enter second intefer: "))
number3 = int(input("Enter third intefer: "))

print(min(number1, number2, number3))
print(max(number1, number2, number3))

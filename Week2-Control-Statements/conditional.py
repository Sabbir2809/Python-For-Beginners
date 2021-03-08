# IF statement
grade = 85

if grade >= 60:
    print("Passed")
    
print("\n")   
# If else statement
grade = 55
if grade >= 60:
    print("Passed")
else:
    print("Fail")
 
    
print("\n")   
# Conditional expression
result = ("Passed" if grade >= 60 else "Failed")
print(result)


print("\n")
# IF...elif....else statement
grade = 77

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
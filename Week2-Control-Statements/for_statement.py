# For statement
for character in "Programming":
    print(character, end=" ")
    
    
# Built in Range Function
for counter in range(10):
    print(counter, end=" ")
   
    
total = 0
for number in range(1000001):
  total = total+number
print(total)

for number in range(5,10):
  print(number, end=" ")
  

for number in range(0,10,2):
  print(number, end=" ")
  
  
for number in range(10,0,-2):
  print(number, end=" ")
  
  
# Take an input from user and print the number table
number =  int(input())
for i in range(1,11):
  print(number,"X",i,"=",number*i)
 
  

# Nested For Loop
 
for left in range(7):
    for right in range(left,7):
        print("["+str(left)+"|"+str(right)+"]", end =" ")
    print()
    
 
# Break statement   
for number in range(10):
  if  number==5:
    break
  print(number, end=" ")
  
  
# Continue statement 
for number in range(10):
  if  number==5:
    continue
  print(number, end=" ")
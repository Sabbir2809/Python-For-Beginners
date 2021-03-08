# define stack 
stack = []

# Push operation using .append() method
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
stack.append("E")
print(stack)


# pop operation using .pop() method
stack.pop() #.pop() can only remove from last element. That's why called stack see the example E is remove first
print(stack)




# List Comprehensions
list1 = []
for item in range(1, 6):
  list1.append(item)
print(list1)


list2 = [item for item in range(1, 6)]
list2

list3 = list(range(1,6))
list3




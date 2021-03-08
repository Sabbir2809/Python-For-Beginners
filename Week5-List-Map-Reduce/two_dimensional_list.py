a = [[77, 68, 86, 73], # first student's grades
      [96, 87, 89, 81], # second student's grades
        [70, 90, 86, 81]] # third student's grades
print(a)


# Nested Loops
for row in a:
  for item in row:
    print(item,end=' ')
  print()
  
for i, row in enumerate(a):
  for j, item in enumerate(row):
    print(f'a[{i}][{j}]={item} ', end=' ')
  print()
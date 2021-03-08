# creating list
list_one = [1, 2, 3, 32, 2, 23, 43, 23, "Python", [2, 32, 3]]
print(list_one)

list_two = []
print(list_two)

list_two = list()
print(list_two)
print("\n")


# iterating list
list_one = [1, 2, 3, 32, 2, 23, 43, 23, "Python", [2, 32, 3]]
for i in list_one:
    print(i, end=" ")
print("\n")


# iterating list
list_one = [1, 2, 3, 32, 2, 23, 43, 23, "Python", [2, 32, 3]]
print(list_one[2])
print(list_one[6])
print(list_one[-2])
print(list_one[-10])
print("\n")


#List operations
lst0 = [1,2,3,32,2.23,43.23,"python",[2,32,3]]

print(len(lst0)) #len() gives the length of the list
lst0.append([12,2,12,2]) #append() inserts an element to the end of the list
print(lst0)
lst0.insert(2,"pandas") #insert() insertes an element on a given index
print(lst0)
lst0.remove(3)  #remove() removes first occurence of an element
print(lst0)
print(lst0.index("python")) #index() returns index of first occurence of an element
print(lst0.count('pandas')) #count() reuturns the number of occurence of an element
print(lst0.reverse()) #reverse() makes a reverse list
lst1=lst0.copy() #copy() makes a copy of list
print(lst1)
lst0.clear() #clear() makes the list empty
print(lst0)



#lsit slicing
lst0=[1,2,3,32,2.23,43.23,"python",[2,32,3]]

print(lst0[2:7])
print(lst0[2:])
print(lst0[:5])
print(lst0[:])



#list sorting
lst2=[1,2,4,2,4,2,4,2,5,6,7,4]

lst3=sorted(lst2)
print(lst3)
print(lst2)
lst2.sort()
print(lst2)




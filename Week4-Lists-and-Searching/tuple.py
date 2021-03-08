#creating tuple
tp0=(1,2,3,32,2.23,43.23,"python",[2,32,3])

print(tp0)
tp1=()
print(tp1)
tp2=tuple()
print(tp2)



#iterating tuple
tp0=(1,2,3,32,2.23,43.23,"python",[2,32,3])

for i in tp0:
    print(i,end=' ')
print('')


#iterating tuple
tp0=(1,2,3,32,2.23,43.23,"python",[2,32,3])

print(tp0[2])
print(tp0[6])


#inserting into tuple
tp0=(1,2,3,32,2.23,43.23,"python",[2,32,3])

tp0+=("pandas",232,3,232,3)
print(tp0)
#order,duplicates allow,mutable
l=[int(i)+2 for i in input().split(",")]  #list compreshion

l.append(9) # add at end
print(f"append 9 at end :{l}")
l.remove(2) # remove by value
print(f"removed 2  value :{l}")
l.pop() #remove last value
print(f"remove value at end :{l}")
l.pop(1) # remove element based on index
print(f"remove value based on index :{l}")
c=l.count(1) #counting the occurence
print(f"counting occurence of 1 :{c}")
l.sort() #ascending order
print(f"list in asc order :{l}")
l.sort(reverse=True)
print(f"list in desc order :{l}")
l.reverse()
print(l)
x=l.index(7) #index
print(x)
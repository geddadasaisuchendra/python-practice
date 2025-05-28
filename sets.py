set= {1,4,3,2}   # unorder,no duplicates allow, no indexing,mutable
print(set)

s={1} #we cant create empty set.
s.add(4)
s.update([2,4])
s.remove(2)        # Remove item (error if not found)
s.discard(10)
s.pop() #remove random  value
s.clear()
print(s)


a = {1, 2, 3}
b = {3, 4, 5}

c=a.union(b) #unioun
print(c)
r=a.intersection(b) #intersection
print(r)
re=a.difference(b)   #difference
print(re) 
result=a.symmetric_difference(b) #symmetric_difference
print(result) 
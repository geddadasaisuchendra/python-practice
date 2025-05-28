#print
print("hi")
x=input() # input() method takes only strings
print(f"hi {x}")

print(len(x)) #len

print(sorted(x)) #gives new sorted list

print(type(x)) #type

# int() , float(), str()
int("5")         # ➝ 5
float("2.5")     # ➝ 2.5
str(123)         # ➝ "123"

l=[1,2,3,4]
print(sum(l),min(l),max(l)) # sum,min,max

print(any(x),all(x)) #any , all

#filter
l=[1,2,3,4,5,6]

odd = list(filter(lambda x:x%2!=0,l))
print(odd)


#map 
double = list(map(lambda x:x*2,odd))
print(double)

#redue
from functools import reduce

r=reduce(lambda x,y: x+y ,double)
print(r)



l=["a","b"]
u=list(map(str.upper, l))  # ➝ ['A', 'B']
print(u)
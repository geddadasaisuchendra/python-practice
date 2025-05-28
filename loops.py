print("enter number:")
# input() function collects the input values in string format only.
a=int(input())
i=1
while(i<=a):
    print(i)
    i+=1
i=a
#reverse
print("reverse order: ")
while(i!=0):
    print(i)
    i-=1

#for loop

#range
range(5)    #end point. it excludes, rangee start from 0 defaultly.
range(1,5) #start point and end point.
range(1,5,2) # start ,end,step.

print("end point: ")
for  i in range(5):
    print(i)
print("start and end point: ")
for  j in range(1,5):
    print(j)
print("start,end,step: ")
for  k in range(1,5,2):
    print(k)

print("list values")
print("enter list: ")
l=input().split(",")
for i in l:
    print(i)

#to reverse list
l=[6,7,8,9] 
for k in range(len(l)-1,-1,-1):
    print(l[k])
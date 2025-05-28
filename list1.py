'''l = [int(i) for i in input().split(",")]
s=0
even=0
odd=0
for i in range(0,len(l)):
    if l[i]%2 == 0:
        even+=1
    else:
        odd+=1
    s+=l[i]
l.reverse()
print(s,max(l),min(l),l,even,odd)'''

'''l = [ int(i) for i in input().split(",")]
li=[]
k=0
for i in range(0,len(l)-1):
    if l[i] != l[i+1]:
        li.append(l[i])
         
li.append(l[i+1])   
print(li)'''
'''s=0
li=[]
l = [int(i) for i in input().split(",")]
for i in range(0,len(l)):
    if i%2==0:
        print(l[i])
    s=l[i]*l[i]
    li.append(s)
print(li)'''
#list palindrome
'''l = [int(i) for i in input().split(",")]
k=[]
for i in range(0,len(l)):
    k.append(l[i])
l.reverse()
if l==k:
    print(True)
else:
    print(False)'''

#string palindrome
'''st = input()
if st == st[::-1]:
    print(True)
else:
    print(False)'''



'''l = [int(i) for i in input().split(",")]
k = [int(i) for i in input().split(",")]
m=[]
for i in range(0,len(l)):
    m.append(l[i])
for j in range(0,len(k)):
    m.append(k[j])
print(m)
'''

#second largest
'''
l = [int(i) for i in input().split(",")]
l.sort(reverse= True)
print(l[1])'''


'''s=input()
l=sorted(s)
print(l)'''


'''l=[int(i) for i in input().split(",")]
l.pop(1)
print(l)'''
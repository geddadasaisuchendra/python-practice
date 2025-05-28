a= 5+2*9
b=5%2+5//1

a+=1
b-=1
print (a,b)
# if else lader
if a>=1 and a<=10:
    print("a inbetween 1 and 10")
elif b>1 or b!=1:
    print("b is greater than 1")
elif not b>a:
    print("b is less than a")
else:
    print("hi")


#if statements

if a>=1 and a<=10:
    print("a inbetween 1 and 10")
if b>1 or b!=1:
    print("b is greater than 1")
if not b>a:
    print("b is less than a")
else:
    print("hi")


#membership

l=[1,2,3,4]

if 1 in l:
    print("yes")
else:
    print("NO")

if 1 not in l:
    print("yes")
else:
    print("NO")


#match
str = "success"

match str:
    case "success":
        print("ok")
    case "fail":
        print("not ok")
    case _:
        print("dont no")
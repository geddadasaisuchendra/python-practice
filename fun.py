'''def fun(num):
    print(num)

fun(4)'''

def fun(a=1):
    print(f"num : {a}") #default value
fun()
# args
def fun(*n):
    print(type(n)) #tuple
fun(1,2,3,4)

def fun(**info):
    for key , value in info.items():
        print(f"key : {key} , value : {value}") # dic
fun(name="amith",age=20)


def fun(**info):
    for key in info:
        print(f"value : {info[key]}") # dic
fun(name="amith",age=20)


#lambda function

square = lambda x:x*x
print(square(5))


#recursive function 
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

factorial(5)

#decorators

def decorator_function(original_function):
    def wrapper_function():
        print("Before original function")
        original_function()
        print("After original function")
    return wrapper_function

@decorator_function
def greet():
    print("Hello!")

greet()
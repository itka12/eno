def a(a, b):
    return a + b

def s(a, b):
    return a - b

print(a(1, 2))
print(s(5, 4))

i = 0     #global variable
print(i)
i = 100
print(i)

def fun1():
    i = 1       #local variable
    print(i)

# black line after function definition
def fun2():
    i = 10
    print(i)

fun1() #function call
fun2()

def say_hi():  # lower case name
    print("hello")  # Must be intended


print("top")
say_hi()
print("bottom")


# 2 function with parameter
def f(name):
    print(name)


f("with parementer")


# 3 function with return
def return_value(a, b):
    print("returned " + str(a))
    return a * b  # you can not write any code after return, function is closed


print(return_value(2, 3))


def a(a):
    return a;
    print("aftter retrun" + str(a))  # Did not give error but did not print too


print(a(3))


# 4 Loop, Power example
def power(base,power):
    result=1
    for  i in range(power):
        result = result*base
    return result
print(power(3,4))  #  3*3*3*3 means 4 3.
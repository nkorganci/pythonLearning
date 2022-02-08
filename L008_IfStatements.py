# 1 If statement

a = 4
b = 5

if a > b and a > 0:
    print("a is bigger")
else:
    print("b is bigger")

# 2 and, or , not

# 3 if statements and comparisons
def max_num(num1,num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3
print("Biggest number is " + str(max_num(2,4,5)))


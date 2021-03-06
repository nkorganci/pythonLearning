# List can contain any kind of variable
# 1 How to find list items
name_mix = ["hi", 2, False]
name = ["Zero", "one", "two", "three"]
print(name[0])
print(name[1:])
print(name[1:2])  # return array ['one']
print(name[1])  # return a string one
print(name[-1])
print(name[1:-1])  # ['one', 'two']
print(name[1:3])  # ['one', 'two'] ,does same thing

# 2 List functions
l1 = [1, 2, 3, 3]
l2 = ["one", "two", 2, 2, 2, 2]
l1.extend(l2)  # adds l2 to end of l1
print(l1)
l1.append(l2[0])  # appends end of the list
print(l1)
l1.insert(2, "Inserted")  # need to write two variable, where and what
print(l1)
l1.remove("one")
print(l1)
l1.clear()
print(l1)  # return array []
l2.pop(len(l2) - 1)  # remove the one element and return it.
print(l2)
print(l2.count(2))  # return how many 2 are there
# sort int and string
l3 = [ 3, 1, 2, 2]
l4=["one","two","seven"]
l3.sort() # works only for numbers or strings
print(l3)
l4.sort()
print(l4)

l3.reverse()
print(l3)

l5=l4.copy(); # Just copied the information , no relationship
l5.append("l5")
print(l5)
print(l4)
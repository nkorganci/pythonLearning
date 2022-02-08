""""
List is a collection which is ordered and changeable. Allows duplicate members.
"""
coordinates = (1, 2, "one", "two")
print(coordinates)  # (1, 2, 'one', 'two')
print(coordinates[3])
#  coordinates[0]=33  tuples are immutable

coordinates1 = ((1, 2, "one", "two"), 2, "one", "two")
print(coordinates1[0])  # (1, 2, 'one', 'two')
print(coordinates1[0][1])  # you can print the inner element by double array

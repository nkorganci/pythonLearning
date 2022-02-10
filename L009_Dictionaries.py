# Dictionaries contain key value

# 1 Key-Value, any variable can be key or value.
monthConversion = {
    "Jan": 10,
    "Mar": "March",
    "isHarmony": True,
    4: 2,
    True: False,
    1: True,
    2: "One",
    'A': 'B'

}
print(monthConversion["isHarmony"])
print(monthConversion['A'])
print(monthConversion[2])

print(monthConversion.get(1))  # If there is no key , return none
print(monthConversion.get("sdf","There is no such key"))  #  If there is no such key

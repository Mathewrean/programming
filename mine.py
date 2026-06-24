# # Dictionaries and listed dictionary

# names = {
#     "name1": {
#         "nam": "john",
#         "age": 30,
#         "weight": 70
#     },

#     "name2": {
#         "nam": "jane",
#         "age": 25,
#         "weight": 60
#     },
# }

# # print single item
# print(names["name1"])

# # printing all dictionary items in table manner. (<dictionary name>[<iteratable value>[<dictionary key> | etc.]])
# for name in names:
#     print(f"{names[name]['nam']:<12} | {names[name]['age']:<3} | {names[name]['weight']:<3}")



# # List

# import random
# listy = ["apple", "banana", "cherry", "date"]
# print(listy)

# # using random library to print the above items with random strings
# for i in listy:
#     print(i + random.choice([" is mine", " is small", " is big", " is sweet", " is sour"]))


listy = ["apple", "banana", "cherry", "date"]
joined_string = ", ".join(listy)
print(joined_string)
print(listy[1:])























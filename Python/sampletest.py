my_list = ["apple", "banana", "cherry","date"]
my_list.sort(key=lambda x: x[::-1])
print(my_list[0])
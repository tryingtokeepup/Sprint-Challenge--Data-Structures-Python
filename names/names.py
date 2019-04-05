import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# we need to add the first list to a hash table

# so, make a dictionary out of them
# b = {a[i]: a[i+1] for i in range(0, len(a), 2)}
# { i : listOfStr[i] for i in range(0, len(listOfStr) ) }


# names1_dict = {i: names_1[i] for i in range(0, len(names_1))}

# # store the duplicates inside another list, return that list
# duplicates = [name for name in names_2 if name in names1_dict.values()]


# names1_dict = {name: None for name in names_1}
# # print(names1_dict)

# duplicates = [name for name in names_2 if name in names1_dict]
# print(duplicates)

# YO HUGE HUGE HUGE I FIGURED IT OUT YOU USE SETS
names1_set = set(names_1)
duplicates = [name for name in names_2 if name in names1_set]
#  for some reason, i cant make a static key and have the values just be something like 'lol'
# names1_dict = {'lol': name for name in names_1}

# duplicates = [name for name in names_2 if name in names1_dict.values()]

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

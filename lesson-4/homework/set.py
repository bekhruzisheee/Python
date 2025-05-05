# %%
my_dict = {"a": 3, "b": 1, "c": 2}

ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", ascending)

# %%
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)



# %%
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)



# %%
n = 5
squares = {x: x**2 for x in range(1, n+1)}
print(squares)



# %%
squares_15 = {x: x**2 for x in range(1, 16)}
print(squares_15)



# %%
my_set = {1, 2, 3}
print(my_set)



# %%
for item in my_set:
    print(item)


# %%
my_set.add(4)  
my_set.update([5, 6]) 
print(my_set)



# %%
my_set.remove(3)  
print(my_set)


# %%
my_set.discard(10)  
print(my_set)


# %%




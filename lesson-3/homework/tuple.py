# %%
fruits = ["olma", "banan", "anor", "shaftoli", "uzum"]


print(fruits[2])

# %%
list1 = [1, 2, 3]

list2 = [4, 5, 6]

combine = list1 + list2

print(combine)

# %%
numbers = [10, 20, 30, 40, 50, 60, 70]

first = numbers[0]

middle = numbers[len(numbers) // 2]

last = numbers[-1]

extracted = [first, middle, last]

print(extracted)

# %%
movies = ["avengers", "interstellar", "fight club", "blade runner", "american psycho"]
movies_tuple = tuple(movies)
print(movies_tuple)

# %%
cities = ["London", "Paris", "Torino", "Madrid", "Utophia", "Wakanda"]
print("Paris" in cities)

# %%
numbers = [1, 2, 3]
duplicate = numbers * 2
print(duplicate)

# %%
numbers = [10, 20, 30, 40]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers) 

# %%
numbers = tuple(range(1, 11))  
slice_part = numbers[3:8]
print(slice_part)  

# %%
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print(count_blue)

# %%
animals = ("dog", "cat", "lion", "tiger")
index_lion = animals.index("lion")
print(index_lion)

# %%
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print(merged)

# %%
list = [1, 2, 3, 4]
tuple = (5, 6, 7)
print(len(list))  
print(len(tuple)) 

# %%
my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
print(my_list)

# %%
numbers = (3, 8, 1, 6, 4)
print(max(numbers))  
print(min(numbers))  

# %%
words = ("hello", "world", "python", "rocks")
reversed_words = words[::-1]
print(reversed_words)

# %%




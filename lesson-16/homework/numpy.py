# %%
import numpy as np

original_list = [12.23, 13.32, 100, 36.32]
array = np.array(original_list)

print("Original List:", original_list)
print("One-dimensional NumPy array:", array)


# %%
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)


# %%
vector = np.zeros(10)
print("Null vector:", vector)

vector[6] = 11
print("After update:", vector)


# %%
arr = np.arange(12, 38)
print(arr)



# %%
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)

print("Original array:", int_array)
print("Array converted to float:", float_array)


# %%
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9/5) + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)


# %%
arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])

print("Original array:", arr)
print("After append:", new_arr)


# %%
arr = np.random.rand(10)  # 10 ta tasodifiy son
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))


# %%
arr = np.random.rand(10, 10)
print("Array:\n", arr)

print("Min value:", np.min(arr))
print("Max value:", np.max(arr))


# %%
arr = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", arr)


# %%



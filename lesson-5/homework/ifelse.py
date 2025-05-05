# %%
def is_leap(year):
    
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap(2020))  
print(is_leap(1900))  
print(is_leap(2000))  


# %%
n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


# %%
def even_numbers_if_else(a, b):
    return list(filter(lambda x: x % 2 == 0, range(a, b + 1))) if a <= b else list(filter(lambda x: x % 2 == 0, range(b, a + 1)))


print(even_numbers_if_else(3, 10))  


# %%
def even_numbers_no_if(a, b):
    return list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b) + 1)))


print(even_numbers_no_if(10, 3))  


# %%




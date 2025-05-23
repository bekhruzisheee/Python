# %% [markdown]
# ### 1

# %%
def modify_string(txt):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0

    while i < len(txt):
        result += txt[i]

        
        if (i + 1) % 3 == 0:
            if txt[i] not in vowels and (i + 1 >= len(txt) or txt[i + 1] != '_'):
                result += '_'

        i += 1

    return result


print(modify_string("hello"))      
print(modify_string("assalom"))     
print(modify_string("abcbcabccdeabcdefabcdefg"))  


# %% [markdown]
# ### 2

# %%
n = int(input())  
for b in range(n):  
    print(b * b)   

# %% [markdown]
# ### 3

# %%
i = 1
while i <= 11:
    print(i)
    i += 1


# %%
for i in range(1, 6):  
    for j in range(1, i + 1):  
        print(j, end=" ")
    print()


# %%
n = int(input("Enter number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)


# %%
number = 2
for i in range(1, 11):
    print(number * i)


# %%
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num >= 75:
        print(num)


# %%
num = 75869
count = 0
while num != 0:
    num //= 10
    count += 1
print(count)


# %%
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# %%
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)


# %%
for i in range(-10, 0):
    print(i)


# %%
for i in range(5):
    print(i)
else:
    print("Done!")


# %%
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# %%
n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# %%
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")


# %%
from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []

    for elem in count1:
        if elem not in count2:
            result.extend([elem] * count1[elem])
        else:
            diff = count1[elem] - count2[elem]
            if diff > 0:
                result.extend([elem] * diff)

    for elem in count2:
        if elem not in count1:
            result.extend([elem] * count2[elem])
        else:
            diff = count2[elem] - count1[elem]
            if diff > 0:
                result.extend([elem] * diff)

    return result


# %%
print(uncommon_elements([1, 1, 2], [2, 3, 4]))  

# %%




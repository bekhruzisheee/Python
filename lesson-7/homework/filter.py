# %%
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
        return False
    return True


print(is_prime(5))  #true
print(is_prime(8))  #false



# %%
def digit_sum(k):
  return sum(int(digit) for digit in str(k))

print(digit_sum(27))   
print(digit_sum(12))   



# %%
def powers_of_two(n):
    result = []
    power = 1
    while power <= n:
        result.append(power)
        power *= 2
    return result[1:]  

print(powers_of_two(10)) 


# %%

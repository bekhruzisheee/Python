# %%
try:
    x = int(input("Enter a number: "))
    result = x / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# %%
try:
    num = int(input("Enter an intager: "))
except ValueError:
    print("That's not a valid intager.")


# %%
try:
    with open("non_existing_file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")


# %%
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a + b)
except ValueError:
    print("TypeError: Only numbers are allowed.")


# %%
try:
    with open("C:/Windows/addins") as f:
        data = f.read()
except PermissionError:
    print("Permission denied.")


# %%
try:
    my_list = [1, 2, 3]
    print(my_list[1])
except IndexError:
    print("Error: Index isnt exist")


# %%
try:
    number = input("Son kiriting : ")
    print("Kiritilgan:", number)
except KeyboardInterrupt:
    print("Xatolik: Foydalanuvchi kiritishni bekor qildi")



# %%
try:
    a = 10
    b = 0
    print(a / b)
except ArithmeticError:
    print("Xatolik: Arifmetik xato")


# %%
try:
    with open("textfile.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Xatolik: Unicode muammosi")


# %%
try:
    my_list = [1, 2, 3]
    my_list.push(4)  
except AttributeError:
    print("Xatolik: Bu obyektda  xususiyat yo‘q.")


# %%
with open("C:\eula.1031.txt", "r") as file:
    content = file.read()
    print(content)


# %%
n = int(input("Nechta qator o‘qilsin: "))
with open("C:\eula.1031.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end='')


# %%
with open("C:\eula.1031.txt", "a") as file:
    file.write("\nYangi matn qo‘shildi.")

with open("C:\eula.1031.txt", "r") as file:
    print(file.read())


# %%
n = int(input("Oxiridan nechta qator o‘qilsin: "))
with open("C:\eula.1031.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line, end='')


# %%
with open("C:\eula.1031.txt", "r") as file:
    lines = file.readlines()

print(lines)  

# %%
text = ""
with open("C:\eula.1031.txt", "r") as file:
    for line in file:
        text += line

print(text)


# %%
lines = []
with open("C:\eula.1031.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

print(lines)


# %%
with open("C:\eula.1031.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Eng uzun so‘z:", longest)


# %%




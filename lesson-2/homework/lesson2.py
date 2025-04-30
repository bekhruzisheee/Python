# %%
name = input('Behruz')
born_y = int(input(2008))
now_y = 2025
age=  now_y - born_y
print(f"{name}, sen {age} yoshdasan")

# %%
letter = "I'am John. I am from London"
location = letter.split("from")[1].strip()
print(location)

# %%
text = input("Matn kiriting: ")
print("Teskari:", text[::-1])

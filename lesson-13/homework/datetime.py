# %%
from datetime import datetime

birthdate = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += 30
if months < 0:
    years -= 1
    months += 12

print(f"Siz {years} yil, {months} oy, {days} kunliksiz.")


# %%
from datetime import datetime, timedelta

birthdate = input("Tug‘ilgan kuningizni kiriting (MM-DD): ")
today = datetime.today()
current_year = today.year
birthday_this_year = datetime.strptime(f"{current_year}-{birthdate}", "%Y-%m-%d")

if birthday_this_year < today:
    birthday_next = birthday_this_year.replace(year=current_year + 1)
else:
    birthday_next = birthday_this_year

delta = birthday_next - today
print(f"Keyingi tug‘ilgan kuningizgacha {delta.days} kun qoldi.")


# %%
from datetime import datetime, timedelta

now_str = input("Hozirgi vaqtni kiriting (YYYY-MM-DD HH:MM): ")
duration_h = int(input("Uchrashuv davomiyligi - soat: "))
duration_m = int(input("Uchrashuv davomiyligi - daqiqa: "))

start = datetime.strptime(now_str, "%Y-%m-%d %H:%M")
end = start + timedelta(hours=duration_h, minutes=duration_m)

print(f"Uchrashuv {end.strftime('%Y-%m-%d %H:%M')} da tugaydi.")


# %%
from datetime import datetime
import pytz

datetime_str = input("Vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_tz = input("Hozirgi vaqt zonasi (masalan, Asia/Tashkent): ")
to_tz = input("Qaysi zonaga o‘girish kerak (masalan, US/Eastern): ")

naive_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
from_zone = pytz.timezone(from_tz)
to_zone = pytz.timezone(to_tz)

localized_time = from_zone.localize(naive_time)
converted_time = localized_time.astimezone(to_zone)

print("Konvertatsiya qilingan vaqt:", converted_time.strftime("%Y-%m-%d %H:%M"))


# %%
from datetime import datetime
import time

target_str = input("Ma'lum bir kelajak vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if target <= now:
        print("Vaqt tugadi!")
        break
    delta = target - now
    print(f"Qolgan vaqt: {delta}", end="\r")
    time.sleep(1)


# %%
number = input("Telefon raqamini kiriting (raqamlar faqat): ")

if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print("Noto‘g‘ri raqam.")


# %%
import re

password = input("Parolni kiriting: ")

if (len(password) >= 8 and 
    re.search(r'[A-Z]', password) and 
    re.search(r'[a-z]', password) and 
    re.search(r'\d', password)):
    print("Parol kuchli.")
else:
    print("Parol kuchsiz.")


# %%
text = "Bu yerda  matn mavjud. Bu matnda bir nechta so‘zlar bor."
word = input("Qidiriladigan so‘zni kiriting: ").lower()

matches = [m.start() for m in re.finditer(word, text.lower())]
print(f"{word} so‘zi {len(matches)} marta topildi. Joylashuvlari: {matches}")


# %%
import re

text = input("Matn kiriting: ")
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
print("Topilgan sanalar:", dates)


# %%




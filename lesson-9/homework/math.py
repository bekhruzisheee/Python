# %%
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Test
c = Circle(5)
print("yuza:", c.area())
print("Perimetr:", c.perimeter())


# %%
from datetime import datetime

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

p = Person("Behruz", "Uzbekistan", 2008)
print(f"Ismi: {p.name}")
print(f"Mamlakati: {p.country}")
print(f"Yoshi: {p.get_age()} yoshda")


# %%
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "0 ga bo‘lish mumkinmas!"
        return a / b


calc = Calculator()
print("Qo‘shish: 5 + 3 =", calc.add(5, 3))
print("Ayirish: 5 - 3 =", calc.subtract(5, 3))
print("Ko‘paytirish: 5 * 3 =", calc.multiply(5, 3))
print("Bo‘lish: 5 / 0 =", calc.divide(5, 0))


# %%
import math

class Shape:
    def area(self):
        raise NotImplementedError("area() metodi hali aniqlanmagan")

    def perimeter(self):
        raise NotImplementedError("perimeter() metodi hali aniqlanmagan")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c): 
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# %%
c = Circle(5)
print("Doira -> Maydon:", c.area(), "Perimetr:", c.perimeter())

t = Triangle(3, 4, 5)
print("Uchburchak -> Maydon:", t.area(), "Perimetr:", t.perimeter())

s = Square(4)
print("Kvadrat -> Maydon:", s.area(), "Perimetr:", s.perimeter())


# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)


# %%
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

print("40 bormi?", bst.search(40))  # True
print("25 bormi?", bst.search(25))  # False


# %%
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stek bo‘sh, olib bo‘lmaydi!"
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return "Stek bo‘sh!"
        return self.items[-1]

    def size(self):
        return len(self.items)


# %%
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Yuqoridagi element:", s.peek())     
print("Olib tashlandi:", s.pop())           
print("Hozirgi stek hajmi:", s.size())      
print("Stek bo‘shmi?", s.is_empty())        


# %%
# Har bir tugunni ifodalovchi klass
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List klassi
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, data):
        temp = self.head

        if temp is not None and temp.data == data:
            self.head = temp.next
            return

        prev = None
        while temp is not None and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"{data} topilmadi.")
            return

        prev.next = temp.next

    def display(self):
        temp = self.head
        if temp is None:
            print("Ro'yxat bo'sh.")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# %%
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked List:")
ll.display()

ll.delete(20)
print("20 o‘chirilgandan so‘ng:")
ll.display()

ll.delete(100)  # mavjud bo‘lmagan qiymat


# %%
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, price, quantity):
        if product in self.items:
            self.items[product]['quantity'] += quantity
        else:
            self.items[product] = {'price': price, 'quantity': quantity}

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
        else:
            print(f"{product} savatda topilmadi.")

    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total

    def display_cart(self):
        if not self.items:
            print("Savat bo'sh.")
        else:
            print("Savat tarkibi:")
            for product, info in self.items.items():
                print(f"{product} - {info['quantity']} dona - {info['price']} so‘m each")


# %%
cart = ShoppingCart()
cart.add_item("Olma", 3000, 3)
cart.add_item("Banan", 5000, 2)
cart.add_item("Olma", 3000, 1)  # miqdor oshiriladi

cart.display_cart()

print("Umumiy narx:", cart.total_price(), "so‘m")

cart.remove_item("Banan")
print("\nBanan o‘chirilgandan so‘ng:")
cart.display_cart()


# %%
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"{item} qo‘shildi.")

    def pop(self):
        if self.is_empty():
            return "Stek bo‘sh, olib bo‘lmaydi!"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stek bo‘sh!"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stek bo‘sh.")
        else:
            print("Stek tarkibi (pastdan yuqoriga):")
            for item in self.items:
                print(item)


# %%
s = Stack()
s.push("Kitob")
s.push("Daftar")
s.push("Ruchka")

s.display()

print("Yuqoridagi element:", s.peek())
print("Olib tashlandi:", s.pop())
s.display()


# %%
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} navbatga qo‘shildi.")

    def dequeue(self):
        if self.is_empty():
            return "Navbat bo‘sh, chiqarib bo‘lmaydi!"
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Navbat bo‘sh!"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Navbat bo‘sh.")
        else:
            print("Navbat (boshidan oxirigacha):")
            for item in self.items:
                print(item)


# %%
q = Queue()
q.enqueue("Ali")
q.enqueue("Vali")
q.enqueue("Guli")

q.display()

print("Boshidagi:", q.peek())
print("Navbatdan chiqarildi:", q.dequeue())

q.display()


# %%
class Bank:
    def __init__(self):
        self.accounts = {}  # ism: balans

    def create_account(self, name, initial_balance=0):
        if name in self.accounts:
            print(f"{name} nomli hisob allaqachon mavjud.")
        else:
            self.accounts[name] = initial_balance
            print(f"{name} uchun hisob ochildi. Boshlang‘ich balans: {initial_balance} so‘m.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            print(f"{amount} so‘m {name} hisobiga qo‘shildi.")
        else:
            print(f"{name} nomli hisob topilmadi.")

    def withdraw(self, name, amount):
        if name not in self.accounts:
            print(f"{name} nomli hisob topilmadi.")
        elif self.accounts[name] < amount:
            print(f"{name} hisobida yetarli mablag‘ yo‘q.")
        else:
            self.accounts[name] -= amount
            print(f"{amount} so‘m {name} hisobidan yechildi.")

    def check_balance(self, name):
        if name in self.accounts:
            print(f"{name} hisobi: {self.accounts[name]} so‘m")
        else:
            print(f"{name} nomli hisob mavjud emas.")


# %%
b = Bank()

b.create_account("Trevor", 100000)
b.deposit("Trevor", 50000)
b.withdraw("Trevor", 30000)
b.check_balance("Trevor")

b.withdraw("Shepim", 200000) 
b.create_account("Shepim")    
b.check_balance("Guli")      


# %%




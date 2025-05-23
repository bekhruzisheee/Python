# %%
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date  
        self.status = False  

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "Done" if self.status else "Pending"
        return f"{self.title} | Due: {self.due_date} | Status: {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.status:
                print(f"{i}. {task}")

def main():
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. Mark Task Complete\n3. List All Tasks\n4. List Incomplete Tasks\n5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due date (YYYY-MM-DD): ")
            todo.add_task(Task(title, desc, due))

        elif choice == "2":
            todo.list_all_tasks()
            idx = int(input("Task number to mark complete: "))
            todo.mark_task_complete(idx)

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.list_incomplete_tasks()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


# %%
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content[:30]}..."

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for i, post in enumerate(self.posts):
            print(f"{i}. {post.title} by {post.author}")

    def posts_by_author(self, author_name):
        filtered = [p for p in self.posts if p.author.lower() == author_name.lower()]
        for post in filtered:
            print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]

    def edit_post(self, index, new_title=None, new_content=None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content

def main():
    blog = Blog()
    while True:
        print("\n1. Add Post\n2. List All Posts\n3. List Posts by Author\n4. Delete Post\n5. Edit Post\n6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Author name: ")
            blog.posts_by_author(author)

        elif choice == "4":
            blog.list_posts()
            idx = int(input("Post number to delete: "))
            blog.delete_post(idx)

        elif choice == "5":
            blog.list_posts()
            idx = int(input("Post number to edit: "))
            new_title = input("New title (leave blank to keep old): ")
            new_content = input("New content (leave blank to keep old): ")
            blog.edit_post(idx, new_title or None, new_content or None)

        elif choice == "6":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

# %%
class Account:
    def __init__(self, acc_num, holder_name, balance=0):
        self.acc_num = acc_num
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return False
        self.balance -= amount
        return True

    def __str__(self):
        return f"Account {self.acc_num} | Holder: {self.holder_name} | Balance: ${self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, acc_num):
        for acc in self.accounts:
            if acc.acc_num == acc_num:
                return acc
        return None

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)
        if from_acc and to_acc:
            if from_acc.withdraw(amount):
                to_acc.deposit(amount)
                print("Transfer successful")
            else:
                print("Transfer failed: insufficient funds")
        else:
            print("Invalid account number(s)")

def main():
    bank = Bank()

    while True:
        print("\n1. Add Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Show Account Details\n7. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            acc_num = input("Account Number: ")
            holder = input("Account Holder Name: ")
            bank.add_account(Account(acc_num, holder))

        elif choice == "2":
            acc_num = input("Account Number: ")
            acc = bank.find_account(acc_num)
            if acc:
                print(f"Balance: ${acc.balance}")
            else:
                print("Account not found")

        elif choice == "3":
            acc_num = input("Account Number: ")
            amount = float(input("Deposit amount: "))
            acc = bank.find_account(acc_num)
            if acc:
                acc.deposit(amount)
                print("Deposit successful")
            else:
                print("Account not found")

        elif choice == "4":
            acc_num = input("Account Number: ")
            amount = float(input("Withdraw amount: "))
            acc = bank.find_account(acc_num)
            if acc:
                if acc.withdraw(amount):
                    print("Withdrawal successful")
            else:
                print("Account not found")

        elif choice == "5":
            from_acc = input("From Account Number: ")
            to_acc = input("To Account Number: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            acc_num = input("Account Number: ")
            acc = bank.find_account(acc_num)
            if acc:
                print(acc)
            else:
                print("Account not found")

        elif choice == "7":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




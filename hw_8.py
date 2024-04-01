import sqlite3

class Mentor:
    def __init__(self, name, surname, age, address, email, mentor_group, student_group, coins=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.email = email
        self.mentor_group = mentor_group
        self.student_group = student_group
        self.coins = coins

    def deposit_coins(self, amount):
        if amount > 0:
            self.coins += amount
            print(f"Вы успешно пополнили Geekcoin на {amount} монет.")
        else:
            print("Сумма Geekcoin для пополнения должна быть положительной.")

    def withdraw_coins(self, amount):
        if amount > 0:
            if amount <= self.coins:
                self.coins -= amount
                print(f"Вы успешно сняли {amount} Coin.")
            else:
                print("Недостаточно средств на балансе.")
        else:
            print("Сумма для снятия должна быть положительной.")

    def display_balance(self):
        print(f"Текущий баланс: {self.coins} Coin.")


def create_mentor_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS mentors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    surname TEXT,
                    age INTEGER,
                    address TEXT,
                    email TEXT,
                    mentor_group TEXT,
                    student_group TEXT,
                    coins INTEGER
                    )''')

def insert_mentor(cursor, mentor):
    cursor.execute('''INSERT INTO mentors (name, surname, age, address, email, mentor_group, student_group, coins)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (mentor.name, mentor.surname, mentor.age, mentor.address,
                    mentor.email, mentor.mentor_group, mentor.student_group, mentor.coins))

def main():
    conn = sqlite3.connect('mentors.db')
    cursor = conn.cursor()

    create_mentor_table(cursor)
    conn.commit()

    mentor = Mentor("Ислам", "Сидиков", 28, "ул. Ленина, д.233", "iышвшлщм96@gmaile.com", "Группа 12-1", "Группа 16-1", coins=100)
    insert_mentor(cursor, mentor)
    conn.commit()

    print("Приветствуем вас в программе для менторов!")
    print("Выберите действие:")
    print("1. Пополнить баланс")
    print("2. Снять с баланса")
    print("3. Проверить баланс")
    print("4. Выход")

    while True:
        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = float(input("Введите сумму для пополнения: "))
            mentor.deposit_coins(amount)
        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            mentor.withdraw_coins(amount)
        elif choice == "3":
            mentor.display_balance()
        elif choice == "4":
            print("Спасибо за использование программы!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите номер действия из списка.")

    conn.close()

if __name__ == "__main__":
    main()

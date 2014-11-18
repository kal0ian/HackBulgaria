import sqlite3

db = sqlite3.connect("company_users.db")

db.row_factory = sqlite3.Row
cursor = db.cursor()


class Company(object):

    def __init__(self, name):
        self.name = name

    def list_employees(self):
        result = cursor.execute('''SELECT name, position FROM users''')
        for user in result:
            print(user['name'], " - ", user['position'])

    def monthly_spending(self):
        result = cursor.execute('''SELECT monthly_salary FROM users''')
        sum = 0
        for user in result:
            sum += user['monthly_salary']
        print("The company is spending $", sum, "every month!")

    def yearly_spending(self):
        result = cursor.execute(
            '''SELECT monthly_salary,yearly_bonus FROM users''')
        sum = 0
        for user in result:
            sum += user["monthly_salary"] * 12
            sum += user['yearly_bonus']
        print("The company is spending $", sum, "every year!")

    def add_employee(self):
        info = input("<name> <monthly_salary> <yearly_bonus> <position>")
        info = info.split()
        name = info[0]
        monthly_salary = info[1]
        yearly_bonus = info[2]
        position = info[3]
        db.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
                   (name, monthly_salary, yearly_bonus, position))

    def delete_employee(self):
        employee_id = input("id: ")
        cursor.execute('''DELETE FROM users WHERE id = ? ''', (employee_id,))

    def update_employee(self):
        employee_id = input("id: ")
        field = input("Enter field: ")
        info = input("Field info: ")
        cursor.execute(
            '''UPDATE users SET {} = ? WHERE id = ? '''.format(field), (info, employee_id))

db.commit()
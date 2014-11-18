import sqlite3


db = sqlite3.connect('company_users.db')
cursor = db.cursor()
#db.row_factory=sqlite3.Row

cursor.execute('''CREATE TABLE IF NOT EXISTS
                      users(id INTEGER PRIMARY KEY, name TEXT, monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)''')

db.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
           ("Ivan Ivanov", 5000, 10000, "Software Developer"))
db.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
           ("Rado Rado", 500, 0, "Technical Support Intern"))
db.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
           ("Ivo Ivo", 10000, 100000, "CEO"))
db.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
           ("Petar Petrov", 3000, 1000, "Marketing Manager"))
db.execute('''INSERT INTO users(name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)''',
           ("Maria Georgieva", 8000, 10000, "COO"))
db.commit()
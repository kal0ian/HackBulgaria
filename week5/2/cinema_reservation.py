import sqlite3


cinema = sqlite3.connect('cinema_reservation.db')
cinema.execute("PRAGMA foreign_keys=ON")
cursor = cinema.cursor()

cursor.execute('''CREATE TABLE 
                      movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)''')
cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''',
               ("The Hunger Games: Catching Fire", 7.9))
cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''',
               ("Wreck-It Ralph", 7.8))
cursor.execute('''INSERT INTO movies(name, rating) VALUES(?,?)''',
               ("Her", 8.3))


cursor.execute('''CREATE TABLE 
                      projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, date TEXT, time TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))''')
cursor.execute('''INSERT INTO projections(movie_id, type, date, time ) VALUES(?,?,?,?)''',
               (1, "3D", "2014-04-01", "19:10"))
cursor.execute('''INSERT INTO projections(movie_id, type, date, time ) VALUES(?,?,?,?)''',
               (1, "2D",  "2014-04-01", "19:00"))
cursor.execute('''INSERT INTO projections(movie_id, type, date, time ) VALUES(?,?,?,?)''',
               (1, "4DX", "2014-04-02", "21:00"))
cursor.execute('''INSERT INTO projections(movie_id, type, date, time ) VALUES(?,?,?,?)''',
               (3, "2D", "2014-04-05", "20:20"))
cursor.execute('''INSERT INTO projections(movie_id, type, date, time ) VALUES(?,?,?,?)''',
               (2, "3D", "2014-04-02", "22:00"))
cursor.execute('''INSERT INTO projections(movie_id, type, date, time ) VALUES(?,?,?,?)''',
               (2, "2D", "2014-04-02", "19:30"))


cursor.execute('''CREATE TABLE 
                      reservations(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER, row INTEGER, col INTEGER, FOREIGN KEY(projection_id) REFERENCES projections(id))''')
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("RadoRado", 1, 2, 1))
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("RadoRado", 1, 3, 5))
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("RadoRado", 1, 7, 8))
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("Ivo", 3, 1, 1))
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("Ivo", 3, 1, 2))
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("Mysterious", 5, 2, 3))
cursor.execute('''INSERT INTO reservations(username, projection_id, row, col ) VALUES(?,?,?,?)''',
               ("Mysterious", 5, 2, 4))

cinema.commit()
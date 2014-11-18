import sqlite3

cinema = sqlite3.connect('cinema_reservation.db')
cinema.execute("PRAGMA foreign_keys=ON")
cinema.row_factory = sqlite3.Row
cursor = cinema.cursor()

seats = [["x", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ],
         [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ]]


def print_seats():
    print("Available seats (marked with a dot):")
    print("  1 2 3 4 5 6 7 8 9 10")
    for i, element in enumerate(seats):
        print (i + 1, ' '.join(element))


def show_movies():
    result = cursor.execute(
        '''SELECT id,name, rating FROM movies ORDER BY rating desc''')
    for movie in result:
        print("[", movie['id'], "]", " - ",
              movie["name"], "(", movie['rating'], ")")


def show_movie_projections(movieID):
    movie_name = cursor.execute(
        '''SELECT name FROM movies WHERE id=? ''', (movieID))
    name = ""
    for row in movie_name:
        name = row['name']
        break

    result = cursor.execute(
        '''SELECT projections.id, projections.date, projections.time,projections.type FROM projections INNER JOIN movies ON projections.movie_id = movies.id WHERE movies.id = ? ORDER BY projections.date, projections.time ''', (movieID) )
    print("Projections for movie", name)
    for movie in result:
        print ("[", movie['id'], "] ", "- ", movie['date'],
               movie['time'], "(", movie['type'], ")")


def make_reservation():
    name = input("Step 1 (User): Choose name>")
    tickets = input("Step 1 (User): Choose number of tickets>")
    print("Current movies:")
    show_movies()
    movieID = input("Step 2 (Movie): Choose a movie>")
    show_movie_projections(movieID)
    projection_id = input("Step 3 (Projection): Choose a projection>")
    print_seats()

    for i in range(0, int(tickets)):
        print("Choose a seat now!")
        row = input("row: ")
        col = input("col: ")
        if seats[int(row)][int(col)] != "x":
            seats[int(row)][int(col)] = "x"
            cursor.execute('''INSERT INTO reservations(username, projection_id, row, col)
                VALUES(?,?,?,?)''', (name, show_movie_projections(movieID), row, col))
        else:
            print("Seat already taken!")

    print("This is your reservation:")
    show_movie_projections(movieID)
    print("Seats:", seats)
    finalize = input("Step 5 (Confirm - type 'finalize') >")
    if finalize == "finalize":
        print("Thanks.")
    else:
        print("your reservation was rejected")

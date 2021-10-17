import mysql.connector
print("Database connectivity")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="dbassign"
)

#Defining cursor object

mycursor = mydb.cursor(buffered = True)

#Creating table

mycursor.execute("CREATE TABLE movies (name VARCHAR(255), actor VARCHAR(255), actress VARCHAR(255), director VARCHAR(255), year int)");

# Inserting values in table

sql = "INSERT INTO movies (name, actor, actress, director, year) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Inception', 'Leonard', 'Ken', ' Marion', 2010),
  ('Parasite', 'Kang', 'Sung', 'Dam', 2020),
  ('Joker', 'Joaquin', 'zazie', 'Robert', 2019),
  ('Avengers', 'Robert', 'Evans', 'Ruffalo', 2019),
  ('Spiderman', 'Liev', 'Luna', 'Glenn', 2019),
]

mycursor.executemany(sql, val)

mydb.commit()

#Fetching all records from table

mycursor.execute("SELECT * FROM movies")
records = mycursor.fetchall()
print("Total number of rows in table: ", mycursor.rowcount)

print("\nPrinting each row")
for row in records:
    print("Movie Name = ", row[0], )
    print("Lead Actor = ", row[1])
    print("Actress  = ", row[2])
    print("Director  = ", row[3])
    print("Year of Release  = ", row[4], "\n\n\n")




#Fetching records from table where Lead actor name is Robert

mycursor.execute("SELECT * FROM movies where actor = 'Robert'")
# get all records
records = mycursor.fetchall()
print("Total number of rows in table: ", mycursor.rowcount)

print("\nPrinting row where actor is Robert")
for row in records:
    print("Movie Name = ", row[0], )
    print("Lead Actor = ", row[1])
    print("Actress  = ", row[2])
    print("Director  = ", row[3])
    print("Year of Release  = ", row[4], "\n")

import psycopg2


# connect to "chinook" db
connection = psycopg2.connect(database = "chinook", password="1234", user="postgres")

# Kinda like a table or the stuff in the db
cursor = connection.cursor()

# Query #1: select all records from 'Artist' table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s',["Quesen"])

# fetch multiple results
# results = cursor.fetchall()

# fetch one result
results = cursor.fetchone()

# close connection
connection.close()

# print results
for result in results:
    print(result)
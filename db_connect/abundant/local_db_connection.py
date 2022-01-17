import mysql.connector

# database connection
connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="voeding_database")

cursor = connection.cursor()

query = ("SELECT * FROM bmi_men")

cursor.execute(query)

for (entity, code, year, mean) in cursor:
    print("{}, {}, {}, {}".format(entity, code, year, mean))

cursor.close()
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="regexgen"
)

cursor = conn.cursor()

print("Database Connected")
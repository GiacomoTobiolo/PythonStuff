import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "test1",
  password = "Testingthistoseeifitworks",
  database = "library",
  buffered = True
)
import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="cnc_data"
    )

mycursor = mydb.cursor()
mycursor.execute("SELECT Speed FROM Spindle;")
data = mycursor.fetchall()

speed_data = [row[0] for row in data]

time_data = range(len(speed_data))
#ну и насрали же
plt.plot(time_data, speed_data)
plt.xlabel('ID')
plt.ylabel('Скорость')
plt.title('График скорости')
plt.show()

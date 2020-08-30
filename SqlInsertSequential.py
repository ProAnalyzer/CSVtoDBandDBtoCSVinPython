import psycopg2
import csv
import time


conn = psycopg2.connect(host="localhost",database="myDB", user="postgres", password="12345")
if(conn is not None):
    print("Connected to DataBase ! ")

cursor = conn.cursor()

start = time.time()
with open('C:/Users/User/Desktop/R.S/EmpFinal.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV,None)
    for row in readCSV:
        if row:
            Age_of_Emp = int(row[3])
            Salary = float(row[4])
            Phone_Number = int(row[6])
            
            cursor.execute("INSERT INTO employeeengineerPython (First_Name,Middle_Name,Last_Name,Age_of_Emp,Salary,Email,Phone_Number,Address,Description,Country)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[row[0],row[1],row[2],Age_of_Emp,Salary,row[5],Phone_Number,row[7],row[8],row[9]])
    conn.commit()
cursor.close()
conn.close()
print("Time Taken for insertion in sequentially : " +str((time.time() - start)))

#Time Taken for insertion in sequentially : 1.9094038009643555 sec
import psycopg2
import csv
import concurrent.futures
import time



file_name = 'C:/Users/User/Desktop/R.S/EmpFinal.csv'
    
conn = psycopg2.connect(host="localhost",database="myDB", user="postgres", password="12345")
if(conn is not None):
    print("Connected to DataBase ! ")

def process_file(file_name):

    cursor = conn.cursor()
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV,None)
        for row in readCSV:
            if row:
                Age_of_Emp = int(row[3])
                Salary = float(row[4])
                Phone_Number = int(row[6])
                
                cursor.execute("INSERT INTO EmployeeEngineerPYTHON (First_Name,Middle_Name,Last_Name,Age_of_Emp,Salary,Email,Phone_Number,Address,Description,Country)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[row[0],row[1],row[2],Age_of_Emp,Salary,row[5],Phone_Number,row[7],row[8],row[9]])
        conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(process_file(file_name))
        #executor.map(process_file(file_name),range(4),chunksize = 1000) 
    print("Time Taken for insertion in parallelly : " +str((time.time() - start)))

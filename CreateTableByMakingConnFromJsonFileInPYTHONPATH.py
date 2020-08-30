import json
import os
import pandas as pd

python_path_dir = os.environ['PYTHONPATH'].split(os.pathsep)

def listToString(s):
    str1 = " "
    return (str1.join(s))
def remove(string): 
    return string.replace(" ", "")

path = listToString(python_path_dir)
file_path = remove(os.path.join(path,'DBconn.json'))

print("This is the absolute python path which is in a list  :  "+str(python_path_dir))
print("This is my python path where is coverted list to String  : "+path)
print("This is the absolute file path where is our json located  : "+file_path)

json_file = open(file_path, "r", encoding= "utf-8")
data = json.load(json_file)

def read_json(data, filename = file_path):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

import psycopg2

def connect():
    conn = None
    try:
        params = read_json(data)

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)
        
        cur.execute("CREATE TABLE EmployeeEngineerPy (Emp_ID SERIAL PRIMARY KEY , First_Name TEXT,  Middle_Name TEXT,  Last_Name TEXT,  Age_of_Emp INT,  Salary FLOAT,  Email VARCHAR(50),  Phone_Number BIGINT,  Address VARCHAR(80),  Description TEXT,  Country VARCHAR(50))")
        conn.commit()
        

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # closing database connection.
        if (conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")



if __name__ == '__main__':
    connect()
    
    
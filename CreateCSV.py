

import csv
with open("EmpFinal.csv", "w") as csvFile:
    fieldnames = ["First_Name",
                  "Middle_Name",
                  "Last_Name",
                  "Age_of_Emp",
                  "Salary",
                  "Email",
                  "Phone_Number",
                  "Address",
                  "Description",
                  "Country"]
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(0,10000):
        writer.writerow({"First_Name" : "Pronay",
                  "Middle_Name" : "Kumar",
                  "Last_Name" : "Ghosh",
                  "Age_of_Emp" : "22",
                  "Salary" : "1111",
                  "Email" : "kumarpronayghosh@gmail.com",
                  "Phone_Number" : "629108728",
                  "Address" : "Dunlop",
                  "Description" : "Software_Engineer",
                  "Country" : "India"})

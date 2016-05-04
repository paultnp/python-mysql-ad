import csv      # imports the csv module
from projectModules import executeSql
from tkinter import filedialog

# function for importing data from csv-file to mysql db
def importFromCsv():
    # get users choice for selecting a csv file
    filepathstring = filedialog.askopenfilename()
    f = open(filepathstring, 'r') # opens the csv file
    try:
        reader = csv.reader(f)  # creates the reader object
        for row in reader:      # iterates the rows of the file in orders
            rowDir = {
                'name' : row[0],
                'firstname': row[1],
                'password': row[2],
                'class': row[3]
            }
            executeSql.executeMysqlInsert('user', rowDir)
    finally:
        f.close()               # closing file reader

# function for save all data from mysql db to .csv file
def exportToCsv():
    path = filedialog.asksaveasfilename()
    rows = executeSql.executeMysqlShow('*', 'user')
    headrow = ['Nutzer-Id', 'Name', 'Vorname', 'Password', 'Klasse']
    with open(path, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(headrow)
        for row in rows:
            writer.writerow(row)
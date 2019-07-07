import os
import csv
float (grams_of_fiber) = 0
path=os.getcwd()

cereal_csv = os.path.join("../Resources", "cereal.csv")
with open(path, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if (float(row[7]) =>5)
            print(row)
next(csv_reader, None)
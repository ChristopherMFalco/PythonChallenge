# Modules - imports the operatnig system and the type of file (CSV)
import os
import csv

unique = []

# Set path for file
csvpath = os.path.join("Resources", "test.csv")

# Open first CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if row[0] not in unique:
            unique.append(row[0])
            
print (unique) 

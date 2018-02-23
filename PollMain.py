# Modules - imports the operatnig system and the type of file (CSV)
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data_1.csv")

# Open first CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skips the header
    next(csvreader)
    
    numVoters = []
    candidates = []

    for row in csvreader:
        # Adding the voters to the list
        numVoters.append(row[0])    
        # Create a list of candidates you received votes
        if row[2] not in candidates:
            candidates.append(row[2])
    
    # Output results                    
    print("Election Results ")
    print("-------------------------")
    print("Total Votes:", len(numVoters))
    print("-------------------------")
    

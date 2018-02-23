import os
import csv
#Set path for file
csvpath = os.path.join("Resources", "budget_data_1.csv")
csvpath2 = os.path.join("Resources", "budget_data_2.csv")
# Function that accepts the CSV files and runs the code
def read_csv(fileName):
    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skips the header
        next(csvreader)
        # Defines the lists
        revenue = []
        date = []
        revChange = []
        # Loops through the csv file
        for row in csvreader:
            #Adding the dates to the list
            date.append(row[0])
            #Adding the revenue to the list
            revenue.append(float(row[1]))
        # Outputs length and sum
        print("Financial Analysis")
        print("----------------------------")
        print("Total Months:", len(date))
        print("Total Revenue: $", sum(revenue))
        # For loop to calculate the average difference, max change, and min change
        for i in range(1,len(revenue)):
            # Comparing the value for the row with the value of the pervious row
            revChange.append(revenue[i] - revenue[i-1])
            # Calculates the average revenue change
            avgRevChange = sum(revChange)/len(revChange)
            # Finds the max revenue change
            maxRevChange = max(revChange)
            # Finds the min revenue change
            minRevChange = min(revChange)
            # Finds the dates that correspond to the max and mi
            maxRevChangeDate = str(date[revChange.index(max(revChange))])
            minRevChangeDate = str(date[revChange.index(min(revChange))])
    # Outputs Calculations
    print("Avereage Revenue Change: $", round(avgRevChange))
    print("Greatest Increase in Revenue:", maxRevChangeDate,"($", round(maxRevChange),")")
    print("Greatest Decrease in Revenue:", minRevChangeDate,"($", round(minRevChange),")")
#Calls the data sets through the functions            
read_csv("budget_data_1.csv")
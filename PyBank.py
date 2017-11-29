import os
import csv

# input files to load
budget_csv = os.path.join("/Users/manoranjanpemmaka/Downloads", "budget_data_1.csv")

# Read the csv and convert it into a list of dictionaries
with open(budget_csv, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None) # Skip the headers
    csvreader = list(csvreader)

    # intializing variable names as lists
    revenue = []
    date = []
    Percent_rev_change = []

    for row in csvreader:
        revenue.append(float(row[1])) # Sum of values in the column1
        date.append(row[0]) # Reading list of Date values
    
    print("Budget Analysis:")
    print("-----------------")
    print("Total Months: ", len(date))
    print("Total Revenue: ", sum(revenue))

    for i in range(0, len(revenue)):
        Percent_rev_change.append((revenue[i] - revenue[i-1])/revenue[i]*100) #Calculating percentage revenue change for 'revenue' column
        Avg_per_rev_change = sum(Percent_rev_change)/len(Percent_rev_change) #Calculating avg percentage revenue change
        max_per_rev_change = max(Percent_rev_change) #Calculating max percentage revenue change
        min_per_rev_change = min(Percent_rev_change) #Calculating min percentage revenue change
        max_per_rev_change_date = str(date[Percent_rev_change.index(max(Percent_rev_change))]) #Retrieving max percentage revenue change date
        min_per_rev_change_date = str(date[Percent_rev_change.index(min(Percent_rev_change))]) #Retrieving min percentage revenue change date
    print("Greatest Increase in Revenue: ", max_per_rev_change_date, "($", max_per_rev_change,")")
    print("Greatest Decrease in Revenue", min_per_rev_change_date, "($", min_per_rev_change,")")
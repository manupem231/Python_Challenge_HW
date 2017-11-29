import os
import csv
import collections
from collections import defaultdict

# input files to load
budget_csv1 = os.path.join("/Users/manoranjanpemmaka/Downloads", "election_data_1.csv")
budget_csv2 = os.path.join("/Users/manoranjanpemmaka/Downloads", "election_data_2.csv")
csvlist = [budget_csv1] # Reading one of the input file as list item

for file in csvlist:
# Read the csv and convert it into a list of dictionaries
    with open(file, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None) # Skip the headers
        csvreader = list(csvreader)

        # intializing variable names as lists
        VoterID = []
        CandidateList = []
        Candidate_Votes = defaultdict(int) # Defining 'Candidate_Votes' as default dictionary
        Votes = []
        Can_Name = []
        percent_votes = []
        candidate = []
        
        for row in csvreader:
            VoterID.append(row[0]) # Appending list of 'VoterID' column values
            Candidate_Votes[row[2]] += 1 # Incrementing 'Candidate' row count by 1
            Can_Votes = dict(Candidate_Votes) # Reading Candidate votes as Dictionary: Key, Values
            Can_Name = list(Can_Votes) # Reading dictionary as a list
        for i in range(0,len(Can_Name)):
            percent_votes.append(Can_Votes[Can_Name[i]]/len(VoterID)*100) # Calculating percentage votes
            candidate.append(Can_Name[i]) # Appending list of unique candidate names
            final_winner = str(candidate[percent_votes.index(max(percent_votes))]) # Retrieving final winner name based on the max percentage votes
        

    print("Election Results:")
    print("-----------------")
    if row[0] != "": # If row value is NOT empty
        print("Total Votes: ", len(VoterID)) # Printing total number of votes
    print("-----------------")
    for i in range(0,len(Can_Name)):
        print(Can_Name[i]+": ", str(percent_votes[i])+"%", "("+str(Can_Votes[Can_Name[i]])+")") # Printing 'number' & 'percentage' of votes for each candidate
    print("-----------------")
    print("Winner: ", final_winner)
    print("-----------------")
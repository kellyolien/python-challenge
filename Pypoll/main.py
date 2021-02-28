import os
import csv

#Read the CSV file

pypollcsv = os.path.join('Resources', 'election_data.csv')

#Assign variables
candidate = []
vote_count =[]
percentage = []

total_votes = 0

#Open CSV file

with open(pypollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

for row in csvreader:
    total_votes =+ 1
    if row[2] in candidate and row[2] not in "Candidate":
        vote_count[row[2]] = vote_count[row[2]] +1

    else:
        candidate.append(row[2])
        vote_count[row[2]] =1

#Calculate percentage
for key, value in vote_count.items():
    percentage[key] = str(round)
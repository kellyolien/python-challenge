import os
import csv

#Read the CSV file

pypollcsv = os.path.join('Resources', 'election_data.csv')

#Assign variables
candidates = []
vote_count =[]

total_votes = 0

#Open CSV file

with open(pypollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    row = next(csvreader,None)


    for row in csvreader:
        total_votes = total_votes + 1
    
        candidate = row[2]

        if candidate in candidates: 
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_count.append(1)


    # results = []
    # results.append("Election Results/n------------------------")
    # results.append(f"Total Votes: {total_votes}/n--------------------------")
    


#Calculate percentage
percentages = []
max_votes = vote_count[0]
max_index = 0

#find the percentage fo votes for each candiddate
for count in range(len(candidates)):
    vote_percent = vote_count[count]/total_votes*100
    percentages.append(vote_percent)

    if vote_count[count] > max_votes:
        max_votes = vote_count[count]
        print(max_votes)
        max_index = count

winner = candidates[max_index]

#Print results
print("Election Results")
print('\n')
print('-------------------')
print(f"Total Votes: {total_votes}")
print('\n')
print('-------------------')
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print('\n')
print('-------------------')
print(f"Winner: {winner}")
print('\n')
print('-------------------')

#Export a text file with results

output_file = os.path.join('analysis','Election_Analysis.txt')

with open(output_file, 'w') as file:

    file.write("Election Results")
    file.write('\n')
    file.write('-------------------')
    file.write('\n')
    file.write(f"Total Votes: {total_votes}")
    file.write('\n')
    for count in range(len(candidates)):
        file.write(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
    file.write('\n')
    file.write(f"Winner: {winner}") 
 


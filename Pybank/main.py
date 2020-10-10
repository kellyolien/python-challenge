import os
import csv

#Read the CSV file

budgetcsv = os.path.join('.', 'Resources', 'budget_data.csv')

#Assign variables

months = []
profit_loss_change = []

count_months = 0
net_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
profit_loss_change = 0

#Open CSV file

with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

for row in csvreader:
    count_months += 1

    current_profit_loss = int(row[1])
    net_profit_loss += current_profit_loss

    if (count_months == 1):
        previous_profit_loss = current_profit_loss

    else:
        profit_loss_change = current_profit_loss - previous_profit_loss

        months.append(row[0])

        profit_loss_change.append(profit_loss_change)

        previous_profit_loss = current_profit_loss







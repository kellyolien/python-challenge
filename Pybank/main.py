import os
import csv

#Read the CSV file

budgetcsv = os.path.join('Resources', 'budget_data.csv')

#Assign variables

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
profit_loss_change = 0

#Open CSV file

with open(budgetcsv, 'r') as csvfile:
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

            profit_loss_changes.append(profit_loss_change)

            previous_profit_loss = current_profit_loss

#Net total amount of changes in "Profits/Losses"

net_profit_loss = sum(profit_loss_changes)

#Average changes in "Profits/Losses"

avg_profit_loss = round(net_profit_loss/(count_months-1), 2)

#Greatest Increase and Greatest Decrease
greatest_increase = max(profit_loss_changes)
max_increase_month = profit_loss_changes.index(greatest_increase)
best_month = months[greatest_increase]

greatest_decrease = min(profit_loss_changes)
min_increase_month = profit_loss_changes.index(greatest_decrease)
worst_month = months[greatest_decrease]

#Export a text file with results

output_file = os.path.join('Analysis','Financial_Analysis.txt')

#Print analysis
print("Financial Analysis")
print('\n')
print('-------------------')
print('\n')
print(f"Total Months: {count_months}")
print('\n')
print(f"Total:  ${net_profit_loss}")
print('\n')
print(f"Average Change: ${avg_profit_loss}") 
print('\n')
print(f"Greatest Increase in Profits:  {best_month},'$',{greatest_increase}")
print('\n')
print(f"Greatest Decrease in Profits: {worst_month},'$', {greatest_decrease}")


with open(output_file, 'w') as file:

    file.write("Financial Analysis")
    file.write('\n')
    file.write('-------------------')
    file.write('\n')
    file.write(f"Total Months: {count_months}")
    file.write('\n')
    file.write(f"Total:  ${net_profit_loss}")
    file.write('\n')
    file.write(f"Average Change: ${avg_profit_loss}") 
    file.write('\n')
    file.write(f"Greatest Increase in Profits:  {best_month},'$',{greatest_increase}")
    file.write('\n')
    file.write(f"Greatest Decrease in Profits: {worst_month},'$', {greatest_decrease}")



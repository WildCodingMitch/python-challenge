# Modules
import os
import csv

# create path to csv data/prepare "output.txt"
csvpath = os.path.join("Resources", "budget_data.csv")
output_file = "output.txt"

# declare variables
profit = []
net_total = 0
months = []
profit_change = []
profit_avg = 0
total_months = 0
greatest_increase = 0
greatest_decrease = 0

with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile)

    # read in header
    header = next(csv_reader)
    
    # read through row by row, appending profit & month data
    for rows in csv_reader:

        profit.append(int(rows[1])) # skip header row
        months.append(rows[0])

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(1, len(profit)):

        profit_change.append((int(profit[i]) - int(profit[i - 1])))
    
    profit_avg = sum(profit_change) / len(profit_change)
    
    # The total number of months included in the dataset
    total_months = len(months)

    # The greatest increase in profits (amount) over the entire period
    greatest_increase = max(profit_change)

    # The greatest decrease in profits (amount) over the entire period
    greatest_decrease = min(profit_change)

    # The net total amount of "Profit/Losses" over the entire period
    net_total = str(sum(profit))

    # The greatest increase in profits (date) over the entire period
    greatest_inc_date = str(months[profit_change.index(greatest_increase)+1])

    # The greatest decrease in profits (date) over the entire period
    greatest_dec_date = str(months[profit_change.index(greatest_decrease)+1])


# Print output to terminal
print("Financial Analysis\n")
print("----------------------------\n")
print("Total Months: " + str(total_months) + "\n")
print("Total: $" + str(net_total) + "\n")
print("Average Change: $" + str(round(profit_avg, 2)) + "\n")
print("Greatest Increase in Profits: " + str(greatest_inc_date) +  " ($" + str(greatest_increase) + ")\n")
print("Greatest Decrease in Profits: " + str(greatest_dec_date) +  " ($" + str(greatest_decrease) + ")\n")


# Print output to "output.txt"
with open(os.path.join("analysis", output_file), 'w') as file:

    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("Average Change: $" + str(round(profit_avg, 2)) + "\n")
    file.write("Greatest Increase in Profits: " + str(greatest_inc_date) +  " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(greatest_dec_date) +  " ($" + str(greatest_decrease) + ")\n")

# end main.py (PyBank)

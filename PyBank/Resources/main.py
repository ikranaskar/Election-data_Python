import os
csvpath = os.path.join('/Users/ikran/OneDrive/Documents/Desktop/Python_challenge/PyBank/Resources/budget_data.csv')

import csv
count = 0
total = 0
monthly_profit = []



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(csvreader)

# Each row is read as a row
    for row in csvreader:
        print(row)
        #The total number of months included in the dataset
        count = count + 1
         #The net total amount of "Profit/Losses" over the entire periodtotal =
        total = total + int(row[1])
        monthly_profit.append(int(row[1]))
        #The greatest increase in profits (date and amount) over the entire period
    max_increase_value = max(monthly_profit)
        #The greatest decrease in profits (date and amount) over the entire period
    min_increase_value = min(monthly_profit)
    print(max_increase_value)
    print(min_increase_value)

    
    
    print(count)
    print(total)
average = total/count
print(average)


print("Financial Analysis")
print('--------------------')
print(f"Total Months: {total}")
print(f"Total: ${round(count)}")
print(f"Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
print(f"Greatest Increase in Profits: (${max_increase_value})")
print(f"Greatest Decrease in Profits: (${min_increase_value})")

output_file = Path(C:\Users\ikran\OneDrive\Documents\Desktop\Python_challenge\PyBank\Resources\Analysis.txt)
with open(output_file, "w") as file
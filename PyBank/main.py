import os
import csv
import pprint

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as file:
    csv_reader = csv.reader(file)

    totals = 0
    for row in csv_reader:
        totals += int(row[1])
    print(totals)

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    print(len(list(csv_reader)))

with open(path, "r") as file:
    csv_reader = csv.reader(file)

    data = list(csv_reader)

    changes = []
    change_total = 0
    total_months = 0
    for i in range(1, len(data)):
        last_period_row = data[i-1][1]
        current_period_row = data[i][1]
        change = float(current_period_row) - float(last_period_row)
        change_total += change
        total_months += 1
        month = data[i][0]
        change_row = month, change
        
        # print(last_period_row, current_period_row, change, month)
        changes.append(change_row)

    average_change = change_total / total_months
    
    print(average_change)
            # print(item[1])   
    print(changes) 
    print(max(changes[1]))
    print(min(changes[1]))

#     change = ???
#     changes.append(change)
# average_change = ???
# greatest_change = ???
    



    # dict_reader = csv.DictReader(file)
    # print([dict(ordered_dict) for ordered_dict in dict_reader])
    

# dict_reader = csv.DictReader(file)

# For row in dict_reader:
# 	if row['Date'] not in unique_months:
# 		unique_months.append(row['Date']


# start at 1 because on the first period, there is no last period
# changes = []
# for i in range(1, len(data)):
    
#     last_period_row = data[i-1]
#     current_period_row = data[i]
    
#     change = ???
#     changes.append(change)
# average_change = ???
# greatest_change = ???

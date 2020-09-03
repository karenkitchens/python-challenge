import os
import csv

OUT_PATH = "vote_data.csv"
OUT_HEADER = [

]

path = os.path.join("Resources", "election_data.csv")


with open(path, "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    votes = len(list(csv_reader))
    print(votes)

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    # start with an empty list
    candidates = []   
    for row in csv_reader: 
        # check if exists in unique_list or not 
        if row[2] not in candidates: 
            candidates.append(row[2])
    print(candidates)

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    count = 0
    header = next(csv_reader)
    votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in csv_reader:
        count += 1
        if row[2] == "Khan":
            khan_votes += 1
        if row[2] == "Correy":
            correy_votes += 1
        if row[2] == "Li":
            li_votes += 1
        if row[2] == "O'Tooley":
            otooley_votes += 1
    
    khan_perc = float(khan_votes) / float(count) * 100
    correy_perc = float(correy_votes) / float(count) * 100
    li_perc = float(li_votes) / float(count) * 100
    otooley_perc = float(otooley_votes) / float(count) * 100

    print(khan_votes)
    print(khan_perc)
    print(correy_votes)
    print(correy_perc)
    print(li_votes)
    print(li_perc)
    print(otooley_votes)
    print(otooley_perc)
            


import os
import csv

# write a text file
TEXT_FILE = "vote_results.txt"

# use the path module to call this file
path = os.path.join("Resources", "election_data.csv")

# open the vote data as a readable file   
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    #skip the header
    header = next(csv_reader)
    votes = len(list(csv_reader))
    print(votes)

# open the vote data as a readable file   
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    #skip the header
    header = next(csv_reader)
    # start with an empty list
    candidates = []   

    #loop through the data
    for row in csv_reader: 
        # check if exists in unique_list or not 
        if row[2] not in candidates: 
            candidates.append(row[2])
    print(candidates)

# open the vote data as a readable file   
with open(path, "r") as file:
    csv_reader = csv.reader(file)
    #skip the header
    header = next(csv_reader)
    #set an empty lists and variables for 0 and get ready for iteration
    count = 0
    votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    #loop through the data
    for row in csv_reader:
        count += 1
        #collect khan votes
        if row[2] == "Khan":
            khan_votes += 1
        #collect correy votes
        if row[2] == "Correy":
            correy_votes += 1
        #collect li votes
        if row[2] == "Li":
            li_votes += 1
        #collect otooley votes
        if row[2] == "O'Tooley":
            otooley_votes += 1
    
    #calculate percentages of votes
    khan_perc = float(khan_votes) / float(count) * 100
    khan_perc = round(khan_perc, 2)
    correy_perc = float(correy_votes) / float(count) * 100
    correy_perc = round(correy_perc, 2)
    li_perc = float(li_votes) / float(count) * 100
    li_perc = round(li_perc, 2)
    otooley_perc = float(otooley_votes) / float(count) * 100
    otooley_perc = round(otooley_perc, 2)

    #print results to the terminal
    print('\n' + 'Election Results \n' + '-' * 20 + '\n')
    print('TOTAL VOTES: '+ repr(count) + '\n' + '-' * 20 + '\n' )
    print('Khan = ' + repr(khan_perc) + '% (' + repr(khan_votes) + ') \n')
    print('Correy = ' + repr(correy_perc) + '% (' + repr(correy_votes) + ') \n')
    print('Li = ' + repr(li_perc) + '% (' + repr(li_votes) + ') \n')
    print('Otooley = ' + repr(otooley_perc) + '% (' + repr(otooley_votes) + ') \n')    
    print('-' * 20 + '\n' + 'Khan is the winner \n')

    #write results to a file
    with open(TEXT_FILE, "w+") as file:
        file.write('Election Results \n' + '-' * 20 + '\n')
        file.write('TOTAL VOTES: '+ repr(count) + '\n' + '-' * 20 + '\n' )
        file.write('Khan = ' + repr(khan_perc) + '% (' + repr(khan_votes) + ') \n')
        file.write('Correy = ' + repr(correy_perc) + '% (' + repr(correy_votes) + ') \n')
        file.write('Li = ' + repr(li_perc) + '% (' + repr(li_votes) + ') \n')
        file.write('Otooley = ' + repr(otooley_perc) + '% (' + repr(otooley_votes) + ') \n')    
        file.write('-' * 20 + '\n' + 'Khan is the winner \n')
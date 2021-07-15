import os
import csv

# setup path to data resource
csvpath = os.path.join('Resources', 'election_data.csv')

# working variables - lists
candidates = []
votes = []
tallies = []
sorted_tallies = []
file_out = []
# working variables - set
candidate_set = set()
# working variables - counters
count = 0
total_votes = 0
x = 0
# working variables - generic string
uline = 30 * "-"

# read from resource file
with open(csvpath, newline='') as csvfile:
    # process file
    csvreader = csv.reader(csvfile, delimiter=',')

    # create list from data
    votes = list(csvreader)
    # don't need header row
    votes.pop(0)

    # get total number of votes
    total_votes = len(votes)

    # output to terminal
    heading = "Election Results"
    print(heading)
    print(uline)
    file_out.append(heading)
    file_out.append(uline)
    vote_count = "Total Votes: " + str(total_votes)
    print(vote_count)
    print(uline)
    file_out.append(vote_count)
    file_out.append(uline)

    # get list of just candidate names
    candidates = votes

    # strip unwanted columns - note this affects original list also...
    [i.pop(0) for i in candidates]
    [i.pop(0) for i in candidates]

    # set up list of distinct candidates
    for candidate in candidates:
        candidate_set.add(candidate[0])

    # build list of results by candidate
    for name in candidate_set:
        # count of occurences i.e. votes for each candidate
        count = candidates.count([name])
        # win percentage
        won = 100 * count / total_votes
        tally = ([name], won, count)
        tallies.append(tally)

# sort from highest percentage to lowest
    sorted_tallies = sorted(tallies, key=lambda x: x[1], reverse=True)

# print vote count totals
    for tally in sorted_tallies:
        line = list(tally)  
        name = line[0]
        name = str(name)
        name = name.strip("[]")
        name = name.strip("'")
        name = name.strip('"')
        won = line[1]
        won = "{0:.3f}".format(won)
        line_out = f"{name}: {won}%  ({line[2]})"
        print(line_out)
        file_out.append(line_out)

    winner = str(sorted_tallies[0][0])
    winner = winner.strip("[]")
    winner = winner.strip("'")
    winner = winner.strip('"')
# print winner 
    result = "Winner:" + " " + winner
    print(uline)
    print(result)
    print(uline)
    file_out.append(uline)
    file_out.append(result)
    file_out.append(uline)

# setup path to output directory
destfile = os.path.join('analysis', "PyPoll.txt")

# output to file
with open(destfile, "w") as output:
    for line in file_out:
        output.write(line)
        output.write('\n')

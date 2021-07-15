import os
import csv

# setup path to data resource
csvpath = os.path.join('Resources', 'budget_data.csv')

# create the working lists and some variables
periods = []
deltas = []
total_months = 0
total_dollars = 0
delta_avg = 0
last = 0
curr_chng = 0
max_incr = 0
max_decr = 0
# read from resource file
with open(csvpath, newline='') as csvfile:

    # process file
    csvreader = csv.reader(csvfile, delimiter=',')
    # create list from data
    periods = list(csvreader)
    # don't need header row
    periods.pop(0)
    # get total number of financial periods
    total_months = len(periods)
    # get total dollar amount of all periods
    for period in periods:
      total_dollars += int(period[1])

    # get list of changes from period to period
    for period in periods:
        if last != 0:
          deltas.append(int(period[1]) - int(last))
          curr_chng = int(period[1]) - int(last) 
          if curr_chng > 0 and curr_chng > max_incr:
              max_incr = curr_chng
              max_incr_line = period[0] + " " + "($" + str(curr_chng) + ")"
          if curr_chng < 0 and curr_chng < max_decr:
              max_decr = curr_chng
              max_decr_line = period[0] + " " + "($" + str(curr_chng) + ")"
        last = period[1]

    # get average of period-to-period changes
    delta_avg = round((sum(deltas) / len(deltas)), 2)


# output to terminal
print("Financial Analysis")
print("Number of months: " + str(total_months))
print("Total: $" + str(total_dollars))
print("Average Change: $" + str(delta_avg))
print("Greatest Increase in Profits: " + max_incr_line)
print("Greatest Decrease in Profits: " + max_decr_line)

# setup path to output directory
destfile = os.path.join('analysis', "PyBank.txt")

# output to file
with open(destfile, "w") as output:
    output.write("Financial Analysis\n")
    output.write("Number of months: " + str(total_months) + "\n")
    output.write("Total: $" + str(total_dollars)+ "\n")
    output.write("Average Change: $" + str(delta_avg)+ "\n")
    output.write("Greatest Increase in Profits: " + max_incr_line + "\n")
    output.write("Greatest Decrease in Profits: " + max_decr_line + "\n")

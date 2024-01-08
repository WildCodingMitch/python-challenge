# Modules
import os
import csv

# create path to csv data/prepare "output.txt"
csvpath = os.path.join("Resources", "election_data.csv")
output_file = "output.txt"

# declare variables
votes = []
total_votes = 0
candidates = []
candidate_name = " "
candidate_votes = {}
candidate_info = {}
vote_percent = 0
winner_count = 0
winner = " "

with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile)

    # read in header
    header = next(csv_reader)
    
    # read through row by row, appending profit & month data
    for rows in csv_reader:

        votes.append(int(rows[0])) # skip header row
        
        candidate_name = rows[2]

        # If candidate has not been added to list (append list and add one vote)
        if candidate_name not in candidates: 
            # A complete list of candidates who received votes
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 1

        # If candidate has already been added to the list (add one vote)
        else: 
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    # The total number of votes cast
    total_votes = len(votes)

    for candidate_name in candidate_votes:

        # The percentage of votes each candidate won
        vote_percent = (candidate_votes[candidate_name] / total_votes) * 100

        # create variable to include 1.)The total number of votes each candidate won 2.)The percentage of votes each candidate won
        candidate_info[candidate_name] = (candidate_name + ": " + str(round(vote_percent, 3)) + "% (" + str(candidate_votes[candidate_name]) + ")\n")

        # Determine the winner of the election based on popular vote
        if (candidate_votes[candidate_name] > winner_count):
            winner_count = candidate_votes[candidate_name]
            winner = candidate_name


# Print output to terminal
print("Election Results\n")
print("-------------------------\n")
print("Total Votes: " + str(total_votes) + "\n")
print("-------------------------\n")
print(candidate_info["Charles Casper Stockham"])
print(candidate_info["Diana DeGette"])
print(candidate_info["Raymon Anthony Doane"])
print("-------------------------\n")
print("Winner: " + winner + "\n")
print("-------------------------\n")

# Print output to "output.txt"
with open(os.path.join("analysis", output_file), 'w') as file:

    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------\n")
    file.write(candidate_info["Charles Casper Stockham"])
    file.write(candidate_info["Diana DeGette"])
    file.write(candidate_info["Raymon Anthony Doane"])
    file.write("-------------------------\n")
    file.write("Winner: " + winner + "\n")
    file.write("-------------------------\n")


# end main.py (PyPoll)

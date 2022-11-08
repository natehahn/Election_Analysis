# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the elction based on popular vote

import csv

import os

# Assign a variable for the path to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save a file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_vote = 0 

# Initialize a candidate list
candidate_options = []

# Candidate Votes
candidate_votes = {}

# Winning candidate variables
winning_candidate= ""
winning_count = 0
winning_percentage = 0

# Open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_vote += 1

        # Identify candidates
        candidate_name = row[2]

        # Adding the candidate to the list
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Save results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: 369,711\n"
        f"------------------------------\n")
    
    print(election_results, end="")
    # Save the final vote count to text file
    txt_file.write(election_results)

    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
         # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_vote) * 100
        # 4. Create veriable to store results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # Print voting results
        print(candidate_results)

        # Save to file
        txt_file.write(candidate_results)


        #Determine the winning candidate and vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # Set variables
            winning_count = votes
            winning_percentage = vote_percentage
        # Winning candidate
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-----------------------------------=\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------------")

    print(winning_candidate_summary)

    # Save winning candidate summary to file
    txt_file.write(winning_candidate_summary)









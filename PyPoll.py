import csv
import os
file_to_load=os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize the vote counter
total_votes=0
#Candidate Options
candidate_options =[]
candidate_votes={}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
   
    #read the headers row
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        #add candidate_name to list if not already on
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
            #creates Key with cadidate names
        candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage = float(votes) / float (total_votes) *100
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    print(f"{winning_candidate} is the winner with {winning_percentage:.1f}% of the {total_votes} cast!")
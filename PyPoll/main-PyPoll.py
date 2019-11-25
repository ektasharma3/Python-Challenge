
import os
import csv


totalVotes = 0
candidates = []
candidate_voteCount = {}
candidate_votePercent = {}

in_filepath = os.path.join('Input & Output', 'election_data.csv')
out_filepath = os.path.join('Input & Output', 'election_data_analysis.csv')


with open(in_filepath, 'r', newline = '') as in_text:

    reader = csv.reader(in_text, delimiter = ',')

    header = next(reader)
    
    
    # Calculating total votes casted and candidate list
    for row in reader:
        
        totalVotes = totalVotes + 1        

        if row[2] not in candidates:

            candidates.append(row[2])
            candidate_voteCount[row[2]] = 1 
                         
        elif row[2] in candidates:

            candidate_voteCount[row[2]] += 1


# Calculating the Winner
winner = max(candidate_voteCount, key=(lambda k: candidate_voteCount[k]))
 

#Sorting the candidate list in descending order of number of candidate votes  
results_list = [[key,candidate_voteCount[key]] for key in candidate_voteCount]
results_list = sorted(results_list, key=lambda row: row[1], reverse=True)


# Calculating candidate vote percentage
for row in results_list:
    key, value = row
    proportion = value / totalVotes
    candidate_votePercent[key] = f"{proportion:.3%} ({value})"
    

# Preparing summary of output to be printed 
output1 = (f"Election Results\n" f"--------------------------\n" f"Total Votes: {totalVotes}\n" f"--------------------------")
output2 = (f"--------------------------\n" f"Winner: {winner}\n" f"--------------------------\n")


# Printing output to the terminal
print(output1)
for key, value in candidate_votePercent.items():
    print(key, ':', value)
print(output2)


# Writing output to the file
with open(out_filepath, 'w+', newline = '') as out_text:

    out_text.write((output1 + '\n'))

    for key, value in candidate_votePercent.items():
        out_text.write((key + ':' + value + '\n'))

    out_text.write(output2)
  
   
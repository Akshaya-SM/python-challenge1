import os
import csv

#Set path for csv file
csvpath = os.path.join('Resources','election_data.csv')
print(csvpath)

# Initialize the variables 
total_votes = 0
candidates_list = []
candidate_votes = { }
percentage_votes = 0.000
winner_count = 0
winner = " "

# To open the (election_data)csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csv_reader)

    csv_header = next(csv_reader)

  # Loops through the given dataset   
    for row in csv_reader:

      # To calculate the Total number of votes casted
        total_votes += 1
     
        candidate = row[2]
        # If statement to find all the list of candidates from the dataset 
        if candidate not in candidates_list:
            candidates_list.append(candidate)          
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1      
  
  # To Prints the results of the Analysis 
    print("\nElection Results")
    print("-----------------------------------")
    print(f"Total Votes : {total_votes}")
    print("-----------------------------------")    
    
  # To caculate total number of votes each candidate recieved
    for candidate in candidate_votes:
        votes =  candidate_votes[candidate]  

     # To calculate percentage of votes each candidate won  
     
        percentage_votes = float(votes/total_votes) * 100    
        print(f"{candidate}: {percentage_votes:.3f}% ({candidate_votes[candidate]})\n")        
        
     # To calculate the winner candidate

        if(votes > winner_count):
            winner_count = votes
            winner = candidate
    print("-----------------------------------") 
    print("Winner : " + winner)
    print("-----------------------------------")  
        
''' 
            candidate_list[] =
            candidate_list[2]=["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"] 
          #  Charles_Casper_Stockham = 1
          #  Diana_DeGette = 2
          #  Raymon_Anthony_Doane = 3

        if(candidate_list[0] > (candidate_list[1] & candidate_list[2])):
            winner = candidate_list[0]
        elif(candidate_list[1] > (votes_of_candidate[2])):
            winner = candidate_list[1]
        else:   
            winner = candidate_list[2]
        #print(f"candidate: " + percentage_votes[candidate] " %   " "(" + candidate_votes[candidate] +")")
        
        with open(txt_path, 'w') as textfile:
        #    textfile.writelines(any)

'''        

# Export the results to a text file
txt_path= os.path.join("Analysis","poll_output.txt")

with open(txt_path, 'w') as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-----------------------------------\n")
    textfile.write(f"Total Votes : {total_votes}\n")
    textfile.write(f"-----------------------------------\n")
    for candidate in candidates_list:
            percentage_votes = float(votes/total_votes) * 100 
            textfile.write(f"{candidate}: {percentage_votes:.3f} % ({candidate_votes[candidate]})\n")        
    textfile.write(f"-----------------------------------\n")
    textfile.write(f"Winner : " + winner)
    textfile.write(f"\n-----------------------------------\n")


#Poll data: three columns- voter ID, County, Candidate
#Analyze votes and calculate:
#total number of votes casted
#complete list of candidates who received votes

#percentage of votes each candidate won
#total number of votes each candidate won
#the winner of the election based on popular vote

#CSV file management
import os
import csv
#file path
csvpath = os.path.join("Resources", "PollData.csv") 
#open file
csvFile =  open(csvpath)
csvRead = csv.reader(csvFile, delimiter=",")
#skip first row of file (headers)
header = next(csvRead)

#count total number of votes casted (number of rows not counting the first)
FileList = list(csvRead) #lists column 1 and 2

totalVotes = len(FileList)

#make a list of the third column, candidates who received votes
candList = []
for col in FileList:
    candList.append(col[2])

#list candidates who received votes (non-repeating)
Unq_candSet = set(candList)
Unq_candList = (list(Unq_candSet))

#totalCand = len(Unq_candList) #used for prepping candidate vote-count calculations

#variables for each candidate's vote-count
voteCand1 = candList.count('Khan')

voteCand2 = candList.count('Correy')

voteCand3 = candList.count('Li')

voteCand4 = candList.count("O'Tooley")


#make a list containing all vote counts
voteCountGroup = [ int(voteCand1), int(voteCand2), int(voteCand3), int(voteCand4) ]

#calculate % of votes won by each candidate

percCand1 = (voteCand1 / totalVotes) * 100

percCand2 = (voteCand2 / totalVotes) * 100

percCand3 = (voteCand3 / totalVotes) * 100

percCand4 = (voteCand4 / totalVotes) * 100


#assign winner
voteCount_dict = { int(voteCand1) : 'Khan', int(voteCand2) : 'Correy', int(voteCand3) : 'Li', int(voteCand4) : "O'Tooley"}

maxVote = max(voteCount_dict.keys())

winner = voteCount_dict[maxVote]


#Print analysis in terminal 

print("Election Results")
print("---------------------------------")
print(f"Total Votes: {totalVotes} ")
print("---------------------------------")
print(f"Candidate: Khan , {round(percCand1,2)} % ({voteCand1})")
print(f"Candidate: Correy , {round(percCand2,2)} % ({voteCand2})")
print(f"Candidate: Li , {round(percCand3,2)} % ({voteCand3})")
print(f"Candidate: O'Tooley , {round(percCand4,2)} % ({voteCand4})")
print("---------------------------------")
print(f"Winner: {winner}" ) 
print(f"--------------------------------")


#print analysis to Poll-Analysis.txt

f = open("Poll-Analysis.txt","w")
f.write("Election Results" + "\n")
f.write("--------------------------------" + "\n")
f.write(f"Total Votes: {totalVotes} " + "\n")
f.write("--------------------------------" + "\n")
f.write(f"Candidate: Khan , {percCand1} % ({voteCand1})" + "\n")
f.write(f"Candidate: Correy , {percCand2} % ({voteCand2})" + "\n")
f.write(f"Candidate: Li , {percCand3} % ({voteCand3}))" + "\n")
f.write(f"Candidate: O'Tooley , {percCand4} % ({voteCand4})" + "\n")
f.write("--------------------------------" + "\n")
f.write("Winner: " + winner + "\n")
f.write("--------------------------------" + "\n")
f.close()
#Allow us to create file path across operating systems 
import os 

#Allow us to read csv file
import csv

# open(budget_data.csv)

#Dictionary to hold the canidiate votes 
Canidate_votes = {}

#Contain the total votes
Ballot = []

#Initalize count 
Charles_Casper_Stockham = 0
Raymon_Anthony_Doane = 0
Diana_DeGette = 0


output_path = os.path.join("analysis","election_result.txt")
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    for csvrow in csvreader:
            Ballot.append(csvrow[1])
            votes = len(Ballot)
    # print(votes)  

        #Add to count, if value is located in column [2]
            if csvrow[2] == "Charles Casper Stockham":
                Charles_Casper_Stockham += 1
    #print(Charles_Casper_Stockham)

            elif csvrow[2] == "Diana DeGette":
                Diana_DeGette +=1
    #print(Diana_DeGette)

            elif csvrow[2] == "Raymon Anthony Doane":
                Raymon_Anthony_Doane +=1
    #print(Raymon_Anthony_Doane)

    #Canidate Calaulation
    Canidate1 = round((Charles_Casper_Stockham/votes)*100,3)
    Canidate2 = round((Diana_DeGette/votes)*100,3)
    Canidate3 = round((Raymon_Anthony_Doane/votes)*100,3)

    #Dictionary to hold the number of votes
    Canidate_votes = {"Charles Casper Stockham": Charles_Casper_Stockham, "Diana DeGette": Diana_DeGette, "Raymon Anthony Doane": Raymon_Anthony_Doane }  

    Election_winner = max(Canidate_votes, key=Canidate_votes.get)
    #print(Election_winner)   


#Write to text file

with  open(output_path, 'w') as fileoutput:
     


    fileoutput.write("Election Results\n")
    fileoutput.write("----------------------------\n")
    fileoutput.write(f"Total Votes: {votes}\n")
    fileoutput.write("----------------------------\n")
    fileoutput.write(f"Charles Casper Stockham: {Canidate1}% ({Charles_Casper_Stockham})\n")
    fileoutput.write(f"Diana DeGette: {Canidate2}% ({Diana_DeGette})\n")
    fileoutput.write(f"Raymon Anthony Doane: {Canidate3}% ({Raymon_Anthony_Doane}) \n")
    fileoutput.write("----------------------------\n")
    fileoutput.write(f"Winner: {Election_winner}\n")

    print("Election Results\n")
    print("----------------------------\n")
    print(f"Total Votes: {votes}\n")
    print("----------------------------\n")
    print(f"Charles Casper Stockham: {Canidate1}% ({Charles_Casper_Stockham})\n")
    print(f"Diana DeGette: {Canidate2}% ({Diana_DeGette})\n")
    print(f"Raymon Anthony Doane: {Canidate3}% ({Raymon_Anthony_Doane}) \n")
    print("----------------------------\n")
    print(f"Winner: {Election_winner}\n")



    
   



    
    
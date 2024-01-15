#Allow us to create file path across operating systems 
import os 

#Allow us to read csv file
import csv


totalmonths = 0
total = 0
change = []
profitloss=[]
month= []

csvpath = os.path.join("Resources","budget_data.csv")
txtpath = os.path.join("analysis","budget_analysis.txt")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)


    for csvrow in csvreader:

    #Number of lines present
        totalmonths+=1
        #print(totalmonths)

    #Profit/Loss Net total 
        total+=int(csvrow[1])
        #print(total)

    #Append Date Column to new list
        month.append(csvrow[0])

    #Append Row Column to new list
        profitloss.append(int(csvrow[1])) 

    #Calculate the profit and loss differences 
        change.append(profitloss[totalmonths-1]-profitloss[totalmonths-2])
        # print(profitloss)

    #Sum the difference
    totalchange = sum(change)

    #Calculate the average and dived by the total  rows **round to the second decimal place**
    averagechange = round(totalchange/(len(change)-1), 2)
    #print(averagechange)

    #Greatest increase in profit
    inc_profit = max(change)
    grt_increase = change.index(inc_profit)
  
    
    #Greatest decrease in profit
    dec_profit = min(change)
    grt_decrease = change.index(dec_profit)
  
    

#Write to text file

with open(txtpath, 'w') as outfile:


    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {totalmonths}\n")
    outfile.write(f"Total: ${total} \n")
    outfile.write(f"Average Change: ${averagechange}\n")
    outfile.write(f"Greatest Increase in Profits: {month[grt_increase]} (${inc_profit}) \n")
    outfile.write(f"Dreatest Decrease in Profits: {month[grt_decrease]} (${ dec_profit})\n")



    print("Financial Analysis\n")
    print("----------------------------\n")
    print(f"Total Months: {totalmonths}\n")
    print(f"Total: ${total} \n")
    print(f"Average Change: ${averagechange}\n")
    print(f"Greatest Increase in Profits: {month[grt_increase]} (${inc_profit}) \n")
    print(f"Dreatest Decrease in Profits: {month[grt_decrease]} (${ dec_profit})\n")
   





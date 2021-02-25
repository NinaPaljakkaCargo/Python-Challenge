#create python script that will analyze financial records
#data set: budget_data.csv - two columns, date and profit/losses

#analyze the records to calculate:
#total number months included in dataset
#net total profit/losses over entire period
#calc changes in profit/losses over entire period
#average changes in profit/losses over entire period
#greatest increase in profits (date and amount) over entire period
#greatest decrease in losses (date and amount) over entire period

#final script should print analysis to the terminal and export a text file with the results


#CSV file management
import os
import csv
#file path
csvpath = os.path.join("Resources", "PyBank.csv") 
#open file
csvFile =  open(csvpath)
csvRead = csv.reader(csvFile, delimiter=",")
#skip first row of file (headers)
header = next(csvRead)

#count total number of months (number of rows not counting the first)
FileList = list(csvRead) #lists column 1 and 2

totalMonths = len(FileList)

#make a list of the second column
colList = []
for col in FileList:
    colList.append([col[0],col[1]])
    
#switch to integers from strings
colProfit = []
for recordList in colList:
    colProfit.append(int(recordList[1]))
    

#sum profit/loss values
netTot = sum(colProfit)

#calculate the average changes in profit/losses over all months
avgChange = (netTot / (totalMonths -1))

#find max profit (record date and amount)
greatestProfit = max(colProfit)

indexProfmax = colProfit.index(greatestProfit)


dateProfit = colList[indexProfmax][0]

#find min losses (record date and amount)
greatestLoss = min(colProfit)

indexProfmin = colProfit.index(greatestLoss)

dateLoss = colList[indexProfmin][0]

#formatting .txt output
netTotal = "${:,.2f}".format(netTot)
greatestProfit = "${:,.2f}".format(greatestProfit)
greatestLoss = "${:,.2f}".format(greatestLoss)

#Final Analysis--> print to terminal
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {totalMonths} ")
print(f"Net Total: {netTotal}")
print(f"Average Change: $ {round(avgChange,2)}")
print(f"Greatest Increase in Profits: {dateProfit} , {greatestProfit}")
print(f"Greatest Decrease in Losses: {dateLoss} , {greatestLoss}")

#print analysis to Bank-Analysis.txt
f = open("Bank-Analysis.txt","w")
f.write("Financial Analysis" + "\n")
f.write("--------------------------------" + "\n")
f.write(f"Total Months: {totalMonths} " + "\n")
f.write(f"Net Total: {netTotal}" + "\n")
f.write(f"Average Change: $ {round(avgChange,2)}" + "\n")
f.write(f"Greatest Increase in Profits: {dateProfit} , {greatestProfit}" + "\n")
f.write(f"Greatest Decrease in Losses: {dateLoss} , {greatestLoss}")
f.close()


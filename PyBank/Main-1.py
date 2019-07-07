#Bank Python Code
#import os and CSV
import os
import csv

with open("budget_data.csv",newline='') as csvFile:
    csvReader=csv.reader(csvFile, delimiter=',')
    next(csvReader)

    csvReaderAsList=list(csvReader)
    print(csvReaderAsList)

    Number_of_Months = len(csvReaderAsList)
    print(Number_of_Months)

    #Only monthly profits
    Second_Cloumn = [row[1] for row in csvReaderAsList]
    #Only Months and Year
    print(Second_Cloumn)
    First_Column = [row[0] for row in csvReaderAsList]
    
    # Change list of strings as integers
    SecondColasInt = map(int,Second_Cloumn)
    print(SecondColasInt)

    SecodColIntList = list(SecondColasInt)
    print(SecodColIntList)

    #Caluclate monthly change in profit
    Subtrac = [SecodColIntList[i+1] - SecodColIntList[i] for i in range(len(SecodColIntList)-1)]
    print(Subtrac)
    
    print(sum(Subtrac))
    #Total of all monthly changes
    TotalRevenue=sum(SecodColIntList)
    print(TotalRevenue)
    #Average monthly change
    AvgChange=sum(Subtrac) / len(Subtrac)
    print(AvgChange)
    #Find greatest increase month to month
    GIncrease = max(Subtrac)
    print(GIncrease)
    #Find greatest decrease month to month
    GDecrease = min(Subtrac)
    print(GDecrease)
    #Locate index of greatest increase
    MaxIndex = Subtrac.index(GIncrease)
    print(MaxIndex)
    #Locate index of greatest decrease
    MinIndex=Subtrac.index(GDecrease)
    print(MinIndex)
    
    IncreaseDate=(First_Column[MaxIndex+1])
    DecreaseDate=(First_Column[MinIndex+1])

          
    with open('financial_analysis_report_' + str(Number_of_Months+1) + '.txt', 'w') as text:
        text.write("Financial Analysis for file 'budget_data_"+ str(Number_of_Months+1) + ".csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("    Total Months: " + str(Number_of_Months) + "\n")
        text.write("    Total Revenue: " + "$" + str(TotalRevenue) +"\n")
        text.write("    Average Revenue Change: " + '$' + str(int(AvgChange)) +'\n')
        text.write("    Greatest Increase in Revenue: " + str(IncreaseDate) + " ($" + str(GIncrease) + ")\n")
        text.write("    Greatest Decrease in Revenue: " + str(DecreaseDate) + " ($" + str(GDecrease) + ")\n\n") 



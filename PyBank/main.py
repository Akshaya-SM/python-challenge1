import os
import csv

# Set path for csv file
csvpath = os.path.join("Resources","budget_data.csv")
print(csvpath)
# C:\Users\aksha\git\datanalysisBC\python-challenge1\PyBank\Resources\budget_data.csv

# Initialize the Variables
TotalMonths = 0
Total_revenue = 0

revenue_change = 0
current_revenue = 0
revenue_sum =0
average_revenue_change = 0

revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",0]

# To open the (budget_data)csv file'

with open(csvpath,"r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # print(csv_reader)
    
    csv_header = next(csv_reader)

    # Loops through the given dataset   
    for row in csv_reader:
        print(row)
   
     # To Calculate Total number of Months in the given Dataset    
        TotalMonths += 1
    
     # To calculate Net Total Amount of "Profit/Losses" over the entire period
        Total_revenue += int(row[1])
     
     # The average change in "Profit/Losses" between months over the entire period
     # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if TotalMonths>1:   
            revenue_change = float(row[1]) - current_revenue
            #revenue_change_list = revenue_change_list + [revenue_change]
            revenue_change_list.append(revenue_change)
        #print(revenue_change)
        current_revenue = float(row[1])
        #print(current_revenue)
        
     # To calulate Average of revenue we need to store it in a [list] and use them.
        #revenue_change_list= []
        
            
        revenue_sum += revenue_change 
        print(revenue_change)
        
        print(revenue_change_list)
        print(len(revenue_change_list))

    
        #average_revenue_change = revenue_change_list.sum()/len(revenue_change_list)

     # The greatest increase in profits (date and amount) over the entire period
        if revenue_change > greatest_increase[1]:
          
            greatest_increase = [row[0],revenue_change]
            #greatest_increase[1] = revenue_change
            #greatest_increase[0]= row[0]

     # The greatest decrease in profits (date and amount) over the entire period

        if revenue_change < greatest_decrease[1]:
            greatest_decrease = [row[0],revenue_change]
            #greatest_decrease[1] = revenue_change
            #greatest_decrease[0]= row[0]

    average_revenue_change = revenue_sum/len(revenue_change_list)

output=[]
#output.append(str(revenue_sum) )
output.append("Financial Analysis")
output.append("--------------------------------")  
output.append("Total Months : " + str(TotalMonths))
output.append("Total : $" + str(Total_revenue))
output.append("Average Revenue Change : $" + str(average_revenue_change))
output.append("Greatest Increase in Revenue: " + greatest_increase[0] +"   $ " + str(greatest_increase[1]))
output.append("Greatest Decrease in Revenue: " + greatest_decrease[0] +"   $ " + str(greatest_decrease[1]))

#x=["a","b","c","d","e"]

print("\n".join(output))

# Write the Analysis results to the textfile

txt_path= os.path.join("Analysis","pyBank_output.txt")

with open(txt_path, 'w') as textfile:
    textfile.write("\n".join(output))
'''
    textfile.write("Financial Analysis\n")
    textfile.write("--------------------------------\n")  
    textfile.write("\nTotal Months : " +str(TotalMonths))
    textfile.write("\nTotal : $" +str(Total_revenue))
    textfile.write("Average Revenue Change : $" +str(average_revenue_change))
    textfile.write("Greatest Increase in Revenue: $" + greatest_increase[0] + greatest_increase[1])
    textfile.writelines("Greatest Decrease in Revenue: $" + greatest_decrease[0] + greatest_decrease[1])
'''



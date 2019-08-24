import os
import csv

def greatest(liste):
    return max(liste)

def lowest(liste):
    return min(liste)

file=os.path.join("..","PyBank","budget_data.csv")
sum=0
profit=[]
with open(file, newline="",encoding="utf-8") as budget:
    reader=list(csv.reader(budget))
    
    for i in range(1,len(reader)):
        profit.append(int(reader[i][1]))
            
    for i in range(1,len(reader)):
        sum+=int(reader[i][1])
    
budget.close()
greatest_month=reader[1+profit.index(greatest(profit))][0]
lowest_month=reader[1+profit.index(lowest(profit))][0]

print(f"Financial Analysis\n-----------------------------------------\nTotal Months: {len(reader)-1}\nTotal: {sum}\nAverage Change: ${sum/(len(reader)-1)}\nGreatest Increase in Profits: {greatest_month} (${greatest(profit)})\nGreatest Decrease in Profits: {lowest_month} (${lowest(profit)})")


f=open("text.txt","a+")
f.write(f"Financial Analysis\n-----------------------------------------\nTotal Months: {len(reader)-1}\nTotal: {sum}\nAverage Change: ${sum/(len(reader)-1)}\nGreatest Increase in Profits: {greatest_month} (${greatest(profit)})\nGreatest Decrease in Profits: {lowest_month} (${lowest(profit)})")
f.close()
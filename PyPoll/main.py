import os
import csv

def vote_per(liste,total):
    return round(len(liste)/total*100,4)

def winner(liste):
    max=0
    winner=""
    for i in range(len(liste)):
        if max<liste[i][1]:
            max=liste[i][1]
            winner=liste[i][0]
        return winner


    

file=os.path.join("..","PyPoll","election_data.csv")
sum=0
Khan=[]
Correy=[]
Li=[]
OTooley=[]
with open(file, newline="",encoding="utf-8") as election:
    reader=list(csv.reader(election))
    
    for i in range(1,len(reader)):
        if reader[i][2]=='Khan':
            Khan.append(reader[i])
        elif reader[i][2]=='Correy':
            Correy.append(reader[i])
        elif reader[i][2]=='Li':
            Li.append(reader[i])
        else:
            OTooley.append(reader[i])
            
            
    sum=len(Khan)+len(Correy)+len(Li)+len(OTooley)
    
    election.close()
    
Results=[]
Results.append(["Khan",len(Khan)])
Results.append(["Correy",len(Correy)])
Results.append(["Li",len(Li)])
Results.append(["O'Tooley",len(OTooley)])    
print(Results)

    
print(f"Election Results\n-----------------------\nTotal Votes: {sum}\n--------------------------------\nKhan:{vote_per(Khan,sum)}% ({len(Khan)})\nCorrey: {vote_per(Correy,sum)}% ({len(Correy)})\nLi: {vote_per(Li,sum)}% ({len(Li)})\nO'Tooley: {vote_per(OTooley,sum)}% ({len(OTooley)})\n-------------------------------\nWinner: {winner(Results)}\n---------------------------")
    
f=open("text.txt","a+")
f.write(f"Election Results\n-----------------------\nTotal Votes: {sum}\n--------------------------------\nKhan:{vote_per(Khan,sum)}% ({len(Khan)})\nCorrey: {vote_per(Correy,sum)}% ({len(Correy)})\nLi: {vote_per(Li,sum)}% ({len(Li)})\nO'Tooley: {vote_per(OTooley,sum)}% ({len(OTooley)})\n-------------------------------\nWinner: {winner(Results)}\n---------------------------")
f.close()
#Taking input and checking if input is not valid recalling the function
def player1move():
    s=input().split(":")
    # Is that character alive
    if s[0] in d1:
        if(s[1] in "FLRB"):
            
            if(s[1]=="F"):
                temp=d1[s[0]]
                if(temp[1]>0 and temp[1]<=4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0],temp[1]-1]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player1move()

            elif(s[1]=="B"):
                temp=d1[s[0]]
                if(temp[1]>=0 and temp[1]<4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0],temp[1]+1]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player1move()

            elif(s[1]=="L"):
                temp=d1[s[0]]
                if(temp[0]>0 and temp[0]<=4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0]-1,temp[1]]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player1move()

            elif(s[1]=="R"):
                temp=d1[s[0]]
                if(temp[0]>=0 and temp[0]<4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0]+1,temp[1]]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player1move()
            else:
                print("Invalid Move")
                player2move()
        else:
            print("Invalid Move")
            player1move()
    else:
        print("Invalid Move")
        player1move()

def player2move():
    s=input().split(":")
    # Is that character alive
    if s[0] in d1:
        if(s[1] in "FLRB"):
            
            if(s[1]=="B"):
                temp=d1[s[0]]
                if(temp[1]>0 and temp[1]<=4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0],temp[1]-1]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player2move()

            elif(s[1]=="F"):
                temp=d1[s[0]]
                if(temp[1]>=0 and temp[1]<4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0],temp[1]+1]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player2move()

            elif(s[1]=="R"):
                temp=d1[s[0]]
                if(temp[0]>0 and temp[0]<=4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0]-1,temp[1]]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player2move()

            elif(s[1]=="L"):
                temp=d1[s[0]]
                if(temp[0]>=0 and temp[0]<4):
                    op=checkkill(temp,s[1])
                    if(op!=-1):
                        d1[s[0]]=d2[op]
                        del(d2[op])
                    else:
                        d1[s[0]]=[temp[0]+1,temp[1]]
                    board[temp[0]][temp[1]],board[d1[s[0]][0]][d1[s[0]][1]]=board[d1[s[0]][0]][d1[s[0]][1]],board[temp[0]][temp[1]]
                    print(board)
                else:
                    print("Invalid Move")
                    player2move()

            else:
                print("Invalid Move")
                player2move()
                    
        else:
            print("Invalid Move")
            player2move()
    else:
        print("Invalid Move")
        player2move()

def checkinput(a):#Checking Input
    q=0
    for j in a:
        if((j[0]=="P" and (j[1]=="1" or j[1]=="2" or j[1]=="3" or j[1]=="4" or j[1]=="5")) or (j[0]=="H" and (j[1]=="1" or j[1]=="2" or j[1]=="3"))):
            q=0    
        else:
            return(-1)
    return(0)

def checkkill(temp,q):#Check if any character is killed or not
    for i in d2:
        if(q=="F"):
            if(d2[i][0]==temp[0] and d2[i][1]==temp[1]-1):
                return(i)
        elif(q=="B"):
            if(d2[i][0]==temp[0] and d2[i][1]==temp[1]+1):
                return(i)
        elif(q=="L"):
            if(d2[i][0]==temp[0]-1 and d2[i][1]==temp[1]):
                return(i)
        elif(q=="R"):
            if(d2[i][0]==temp[0]+1 and d2[i][1]==temp[1]):
                return(i)
    return(-1)

def winner():
    if(len(d1)==0):
        print("Player 2 wins")
        return(0)
    if(len(d2)==0):
        print("Player 1 wins")
        return(0)
    return(1)
d1={"P1":[],"P2":[],"P3":[],"P4":[],"P5":[]}
#Positions of player 1
d2={"P1":[],"P2":[],"P3":[],"P4":[],"P5":[]}
#Positions of player 2
board=[["-" for k in range(0,5)]for j in range(0,5)]
#Positions of board at any time

a=input().split(",")
while(checkinput(a)==-1):
    print("Invalid input format")
    a=list(map(input().split()))
for j in range(0,5):
    d1[a[j]]=[4,j]
    board[4][j]="A-"+a[j]
print(board)

b=input().split(",")
while(checkinput(b)==-1):
    print("Invalid input format")
    b=list(map(input().split()))
for j in range(0,5):
    d2[b[j]]=[0,j]
    board[0][j]="B-"+b[j]
print(board)

k=0 #which player is moving 0-A || 1-B
while(True):
    if(k==0):
        player1move(1)
    else:
        player2move(1)
    if(winner()==0):
        break

        

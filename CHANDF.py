def checkinput(a):
    for j in a:
        if(j[0]=="P" and (j[1]=="1" or j[1]=="2" or j[1]=="3" or j[1]=="4" or j[1]=="5")):
            1=1
        else:
            return(-1)
    return(0)

def checkkillF(temp):
    for k in d1:
        if(d1[k][0]==temp[0] and d1[k][1]==temp[1]-1):
            return(k)
    return(-1)
def deadlock():    

    
d1={"P1":[],"P2":[],"P3":[],"P4":[],"P5":[]}
d2={"P1":[],"P2":[],"P3":[],"P4":[],"P5":[]}
board=[["-" for k in range(0,5)]for j in range(0,5)]
a=input().split(",")
while(if(checkinput(a)==-1)):
    print("Invalid input format")
    a=list(map(input().split()))
for j in range(0,5):
    d1[a[j]]=[4,j]
    board[4][j]="A-"+a[j]
print(board)
b=input().split(",")
while(if(checkinput(b)==-1)):
    print("Invalid input format")
    b=list(map(input().split()))
for j in range(0,5):
    d2[b[j]]=[0,j]
    board[0][j]="B-"+b[j]
print(board)
k=0 #which player is moving 0-A || 1-B
while(True):
    if(k==0):
        s=input().split(":")
        if s[0] in d1:
            if(s[1] in "FLRB"):
                if(s[1]=="F"):
                    temp=d1[s[0]]
                    if(temp[1]>0 and temp1<=4):
                        if(checkkill(temp)==1):
                            
                        else:
                            
                        board[temp[0]][temp[1]]
                    else:
                        print("Invalid Move")
            else:
                print("Invalid Move")
        else:
            print("Invalid Move")

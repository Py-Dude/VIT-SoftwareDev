d1={"P1":[],"P2":[],"P3":[],"P4":[],"P5":[]}
d2={"P1":[],"P2":[],"P3":[],"P4":[],"P5":[]}
board=[["-" for k in range(0,5)]for j in range(0,5)]
a=input().split(",")
for j in range(0,5):
    d1[a[j]]=[4,j]
    board[4][j]="A-"+a[j]
print(board)
b=input().split(",")
for j in range(0,5):
    d2[b[j]]=[0,j]
    board[0][j]="B-"+b[j]
print(board)
print(d1,d2)

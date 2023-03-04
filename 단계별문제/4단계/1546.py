import sys
N=int(input())
score=list(map(int,input().split()))
maxscore=max(score)
sum=0
for i in range(N):
    score[i]=(score[i]/maxscore)*100
    sum+=score[i]

print(sum/N)
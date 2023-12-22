count=int(input())
score=list(map(int,input().split())) #리스트 형식으로 입력받기
new_score=[]

M=max(score) #MAX 값 변수 

for i in score:
    new_score.append(i/M*100) #새로운 리스트에 새로운 점수 값 넣기 

avg=sum(new_score)/count #새로운 리스트에 값 다 더하고 카운트로 나누기 
print(avg) #평균 출력 

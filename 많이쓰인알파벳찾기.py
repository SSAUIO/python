word=input()

U_word=list(set(word)) #set함수 사용 중복값 제거 

cnt_list=[]

for i in U_word: # 중복값 제거된 U_word 값을 뽑아 
    cnt=word.count(i) # word에 몇개가 존재하는지 cnt에 저장 
    cnt_list.append(cnt)# cnt 값을 리스트에 저장 

if cnt_list.count(max(cnt_list))>1: # 리스트의 맥스값이 여러개일 경우 
    print('?')

else:
    print(U_word[cnt_list.index(max(cnt_list))])
    #리스트의 맥스값의 인덱스 U_word에 해당하는 값


total=20
subscore,gradescore,totalscore,result=0.0,0.0,0.0,0.0


for i in range(20):
    sub,score,grade=input().split()
    score=float(score)

    if grade=='A+':
        gradescore=4.5
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='A0':
        gradescore=4.0
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='B+':
        gradescore=3.5
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='B0':
        gradescore=3.0
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='C+':
        gradescore=2.5
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='C0':
        gradescore=2.0
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='D+':
        gradescore=1.5
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='D0':
        gradescore=1.0
        subscore+=score*gradescore
        totalscore+=score
    elif grade=='F':
        gradescore=0.0
        subscore+=score*gradescore
        totalscore+=score

result=subscore/totalscore
print(round(result,7))

    

    
    
    

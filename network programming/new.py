l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,20,53]
d={}
sum=0
name =input('enter your name ')
for i in range (0,len(l1)):
    d[l1[i]]=l2[i]
    question=l1[i]
    if question in d:
        ans=d[question]
        print('what the port of '+question)
        answer=int(input('enter your answer'))
        if answer==ans:
                  sum=sum+1
print(
name , 'you solved ' +str(sum),'from '+str(len(l1)))
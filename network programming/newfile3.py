num=(input('input your binary number'))
sum=0
count=len(num)-1

for i in num:
   sum =sum+int(i)*2**count
   count = count -1
print(sum) 
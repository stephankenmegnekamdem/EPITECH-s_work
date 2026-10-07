num=123456789
num1=112233445566778899
num4=123456789*987654321
ans=0
while num > 0:
   ans=ans + num%10
   num=num//10
print (ans)
ans=0
while num1 > 0:
   ans=ans + num1%10
   num1=num1//10
print (ans)
ans=0
while num4 > 0:
   ans=ans + num4%10
   num4=num4//10
print (ans)
 

def sum(n):
 num1 = 0
 for i in range(n):
     for j in range(i):
        num1=num1+pow(10,j)
 return num1
def power(n, i):
    for j in range(1, i):
      print(pow(n,j+1))
ans1=sum(10)
print(ans1)
power(ans1, 5)
ans2=sum(11)
print(ans2)
power(ans2, 5)
ans3=sum(12)
print(ans3)
power(ans3, 5)






n=5000000
d=-1
pi=0
flag=0
for i in range(n):
  if i%2==0:
   pi =pi+(1/(d+(2*(i+1))))
  else:
   pi =pi-(1/(d+(2*(i+1))))
pi=4*pi
print(f"{pi:.6f}")


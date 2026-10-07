n=5000000
d=6
pi=1

while n>=0:

  d=6+pow(3+(n*2),2)/d
  n=n-1
pi=3+1/d

print(f"{pi:.6f}")
print(f"{pi:.6}")
print(f"{pi:.7}")

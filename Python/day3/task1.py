var = "My name is Stephan. I am 55 yrs old"
print("task1.1:", var)

print("task1.2:", var[0])

l=len(var)
print("task1.3:", var[l-1])

print("task1.4:", var[5:(l-1)])

print("task1.5:", str.lower(var))

def replace_tu_to_ta(wor):
    ans=wor.replace("tu","ta")
    return ans

var1="tutu on the tuki-kata"
var2=replace_tu_to_ta(var1)
print("task1.6:", var2)

print("task1.7:")
print("I think that the code finds the letter 'a' in string, then prints its index") 
string = "Hello world!"
position = string.find("a")
print(position)

print ("task1.8:")
p = "abcdefghij"
print(p[::-2][:5][::-1][3:])

print("task1.9:")
print("p[::-2], reverses the string jumping a letter each time(2)")
print("[:5], now gives the 5 first ltters( till index5")
print("[::-1], reverses jumping no letter")
print("[3:], prints after third letter")

print("task1.10:")
def print10x(wor):
  for i in range(9):
     print(wor)

print("task1.11:print("hello" + "42")")


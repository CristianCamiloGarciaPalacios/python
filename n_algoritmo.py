import math

t = 3.1536*(10**15)
n = 219882720000000
while n*math.log(n,10) < t:
    n+=1
n-=1
print(f"{n} da t={n*math.log(n,10)} < {t}")
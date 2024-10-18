import math

def combo(m,n):
    return math.factorial(m) / (math.factorial(n) * math.factorial((m-n)))

n = 1798
m = 844
res = 0
c = 0
for k in range(m, n+1):
    c += math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print("The sum of combinations: {}".format(c))
print("The sum of combinations (modulo 1,000,000): {}".format(c%1000000))

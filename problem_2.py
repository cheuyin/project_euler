n1 = 1
n2 = 2
res = 2

while n2 <= 4000000:
    temp = n1 + n2
    n1 = n2
    n2 = temp
    if temp % 2 == 0:
        res += temp

print(res)
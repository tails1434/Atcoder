n = int(input())
a = [0,0,1]

for i in range(3,n):
    if n <= 3:
        break
    else:
        a.append((a[i-3] + a[i-2] + a[i-1]) % 10007)

print(a[n-1])
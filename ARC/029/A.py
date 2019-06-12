N = int(input())

t = [0] * N

for i in range(N):
    t[i] = int(input())

ans = float('inf')

for i in range(1<<N):
    a = []
    b = []
    for j in range(N):
        if (i >> j) & 1 == 1:
            a.append(t[j])
        else:
            b.append(t[j])
    sum_a = sum(a)
    sum_b = sum(b)
    if ans > max(sum_a,sum_b):
        ans = max(sum_a,sum_b)
    
print(ans)
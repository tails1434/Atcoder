K, S = map(int, input().split())

count = 0
for i in range(K+1):
    for j in range(K+1):
        z = S - i - j
        if 0 <= z <= K:
            count += 1

print(count)
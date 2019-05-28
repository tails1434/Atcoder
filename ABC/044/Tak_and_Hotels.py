N = int(input())
K = int(input())
X = int(input())
Y = int(input())
sum = 0
for i in range(1, N+1):
    if i <= K:
        sum += X
    else:
        sum += Y

print(sum)

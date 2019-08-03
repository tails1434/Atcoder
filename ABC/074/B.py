N = int(input())
K = int(input())
x = list(map(int, input().split()))

sum = 0
for i in x:
    sum += 2 * min(i,abs(i-K))

print(sum)
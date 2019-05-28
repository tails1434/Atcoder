N = int(input())
value = 0
for i in range(1, N+1):
    value += (i * 10000) / N

print(int(value))
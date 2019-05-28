N, A, B = map(int, input().split())

def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

total = 0

for i in range(N+1):
    sum = findSumOfDigits(i)
    if (A <= sum <= B):
        total += i

print(total)
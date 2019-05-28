N = int(input())

def sumOfDegits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

min_sum = float('inf')

for i in range (1, N):
    a = sumOfDegits(i)
    b = sumOfDegits(N-i)
    if min_sum > a + b:
        min_sum = a + b

print(min_sum)
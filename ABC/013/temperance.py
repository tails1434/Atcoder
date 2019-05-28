import math

N,H = map(int, input().split())
A,B,C,D,E = map(int, input().split())

money = float('inf')

for i in range(N+1):
    # +1するのは Ba + D b + H - E *(N - a - b) > 0
    # の関係式から考えると自明
    y = (E * N - E * i - H - B * i )//(E + D) + 1
    y = max(0,y)
    if i + y <= N:
        money = min(money, (A * i + C * y))

print(money)
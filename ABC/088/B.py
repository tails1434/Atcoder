N = int(input())
a = list(map(int, input().split()))

sort_a = sorted(a, reverse=True)

cnt = 0
Alice = 0
Bob = 0
for i in sort_a:
    if cnt % 2 == 0:
        Alice += i
    else:
        Bob += i
    cnt += 1

print(Alice - Bob)
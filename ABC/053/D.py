N = int(input())
A = list(map(int, input().split()))

set_A = set(A)

if len(set_A) % 2 == 0:
    print(len(set_A) - 1)
else:
    print(len(set_A))
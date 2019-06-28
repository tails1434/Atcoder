# 前の回答が気に食わなかったのでもう一回

N = int(input())
A = list(map(int, input().split()))
A.sort()

for i, a in enumerate(A):
    if N % 2 == 0:
        if a != i // 2 * 2 + 1:
            print(0)
            exit()
    else:
        if a != (i + 1) // 2 * 2:
            print(0)
            exit()

print(pow(2, N // 2, 10 ** 9 + 7))
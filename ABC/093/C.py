# 方針 貪欲法で+2できるまで+2をする
# できなくなったら、A,Bを+1してソートする
# A = B = Cとなるまで実行する

A, B, C = map(int, input().split())

ans = 0
while not (A == B == C):
    A, B, C = sorted([A, B, C])
    if A + 2 <= C:
        A += 2
    else:
        A += 1
        B += 1
    ans += 1

print(ans)
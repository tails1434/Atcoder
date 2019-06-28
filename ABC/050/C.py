N = int(input())
A = list(map(int, input().split()))

#if N % 2 == 0:
#    for i in range(1, N, 2):
#        if A.count(i) != 2:
#            print(0)
#            exit()
#    print(int((2 ** (N/2)) % (10*9 + 7)))
#else:
#    for j in range(0, N, 2):
#        if j == 0:
#            if int(A.count(j)) != 1:
#                print(0)
#                exit()
#        else:
#            if A.count(j) != 2:
#                print(0)
#                exit() 
#    print(int(2 ** ((N-1)/2) % (10*9 + 7)))

# 全探索でやると間に合わなかったので正しい場合の和の値を求めてそれを配列の和と比較する

K = N if N % 2 == 0 else N + 1
S = N // 2
if sum(A) == K * S:
    ans = 2 ** S % (10 ** 9 + 7)
else:
    ans = 0

print(ans)
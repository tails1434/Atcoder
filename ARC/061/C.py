S = input()
op_cnt = len(S) - 1
ans = 0
for i in range((2 ** op_cnt)):
    k = 0
    for j in range(op_cnt):
        if ((i >> j) & 1):
            ans += int(S[k:j+1])
            k = j+1
    ans += int(S[k:])

print(ans)
def main():
    S = list(input())

    print(min(S.count('0'),S.count('1'))*2)

    # 当たり前だけど全探索はTLEでアウト
    # ans = 0
    # while True:
    #    cnt = 0
    #    for i in range(1,len(S)):
    #        if S[i] != S[i-1]:
    #            S.pop(i)
    #            S.pop(i-1)
    #            cnt += 2
    #            break
    #    if cnt == 0:
    #        break
    #    ans += cnt

    #print(ans)



main()
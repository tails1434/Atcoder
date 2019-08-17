def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D

    for i in range(D):
        p[i], c[i] = map(int, input().split())

    ans = float('inf')
    for i in range(1 << D):
        cnt = 0
        score = 0
        tmp = 0
        for j in range(D):
            if (i >> j) & 1:
                score += c[j] + 100 * (j + 1) * p[j]
                cnt += p[j]
            else:
                # jが大きいほど得点が高くなるので
                # 何もせず最後のjを考えれば良い
                tmp = j
                
        if score < G:
            for k in range(1,p[tmp]):
                score += 100 * (tmp + 1)
                cnt += 1
                if score >= G:
                    break
        
        if score >= G:
            ans = min(ans,cnt)
    
    print(ans)


main()
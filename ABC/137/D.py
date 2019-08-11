from collections import defaultdict
def main():
    N, M = map(int,input().split())

    # C = [[int(i) for i in input().split()] for i in range(N)]
    C = defaultdict(list)

    for _ in range(N):
        A, B = map(int, input().split())

        if A <= M:
            C[A].append(B)
    cnt = M
    ans = 0
    while cnt > 0:
        tmp = 0
        tmp_k = 0
        tmp_v = 0
        for k,v in list(C.items()):
            if k <= cnt:
                if v:
                    v_max = max(v)
                    if v_max and tmp <= v_max:
                        tmp = v_max
                        tmp_k = k
        if tmp_k:
            tmp_v = C.pop(tmp_k)
            tmp_v.remove(tmp)
            for j in tmp_v:
                C[tmp_k].append(j)
        ans += tmp
        cnt -= 1
    
    print(ans)

    
  
main()
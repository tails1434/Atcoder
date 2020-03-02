from collections import defaultdict

def main():
    N, M = map(int, input().split())
    d = defaultdict(int)
    for _ in range(M):
        s, c = map(int, input().split())
        if d[s]:
            if d[s] != c:
                print(-1)
                exit()
        d[s] = c

    ans = [-1] * N
    for i, j in d.items():
        ans[i-1] = j

    if N != 1 and ans[0] == 0:
        print(-1)
        exit()
    
    if N == 1 and (ans[0] == -1 or ans[0] == 0):
        print(0)
        exit()
    str_ans = ''
    for i in range(N):
        if ans[i] == -1:
            if i == 0:
                str_ans += '1'
            else:
                str_ans += '0'
        else:
            str_ans += str(ans[i])



    print(str_ans)



if __name__ == "__main__":
    main()
import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    num = [-1] * (N + 1)
    table = [0] * (N+1)
    for i in range(1,N+1):
        table[i] = i
    
    for _ in range(Q):
        f, t, x = map(int, input().split())
        a = table[f] + 0
        b = table[t] + 0
        c = num[x] + 0
        table[f] = c
        num[x] = b
        table[t] = a

    ans = [-1] * (N+1)
    for i in range(1,N+1):
        if table[i] == -1:
            continue
        ans[table[i]] = i
        tmp = num[table[i]]
        while tmp != -1:
            ans[tmp] = i
            tmp = num[tmp]

    for i in range(1,N+1):
        print(ans[i])




if __name__ == "__main__":
    main()
def dfs(s,N):
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for i in '753':
        ret += dfs(s+i,N)
    return ret

def main():
    N = int(input())

    print(dfs('0',N))
main()
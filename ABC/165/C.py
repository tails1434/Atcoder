N, M, Q = map(int, input().split())

def dfs(n,i,s,A):
    if n == N:
        #A.append(s)
        #return
        return s

    for j in range(i,M+1):
        tmp = s + [j]
        return dfs(n+1,j,tmp,A)

def main():
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i],b[i],c[i],d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    
    A = []
    ans = 0
    #dfs(0,1,[],A)
    #for B in A:
    for B in dfs(0,1,[],A):
        print(B)
        tmp = 0
        for j in range(Q):
            if B[b[j]] - B[a[j]] == c[j]:
               tmp += d[j]

        ans = max(ans, tmp)

    print(ans) 



if __name__ == "__main__":
    main()
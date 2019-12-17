def find_negative_loop(n, w, edges):
    d = [float('inf')] * n
    d[0] = 0
    for i in range(n):
        for (u, v, c) in edges:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                if i == n - 1 and v == n - 1:
                    return None
    return d[n-1]

def main():
    N, M = map(int, input().split())
    edges = [None] * M
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges[i] = (a, b, -c)


    ans = find_negative_loop(N, M, edges)

    if ans:
        print(-1 * ans)
    else:
        print('inf')

    
    

if __name__ == "__main__":
    main()
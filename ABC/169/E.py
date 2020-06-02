from collections import defaultdict

def main():
    N = int(input())
    X = []
    for i in range(N):
        A, B = map(int, input().split())
        X.append([A,B])
    d = defaultdict(list)
    X.sort()

    for i, x in enumerate(X):
        d[i+1].append(x[0])
    X.sort(key=lambda x: x[1])

    for i, x in enumerate(X):
        d[i+1].append(x[1])
    if N % 2 == 1:
        ans = d[(N+1)//2][1] - d[(N+1)//2][0] + 1
        print(ans)
    else:
        ans = (d[N//2][1] + d[N//2 + 1][1]) - (d[N//2][0] + d[N//2 + 1][0]) + 1
        print(ans)


    
    
    
    


if __name__ == "__main__":
    main()
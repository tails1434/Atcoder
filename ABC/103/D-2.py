def main():
    N, M = map(int, input().split())
    X = []
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        X.append([a,b])
    
    X.sort(key=lambda x: x[1])
    cnt = 1
    now = X[0][1]
    for a, b in X:
        if now <= a:
            cnt += 1
            now = b

    print(cnt)



if __name__ == "__main__":
    main()
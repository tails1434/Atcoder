def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    cnt = X // D
    if cnt >= K:
        print(X - (K * D))
        exit()
    
    if cnt % 2 == K % 2:
        print(X - (cnt * D))
    else:
        print(abs(X - ((cnt + 1) * D)))




if __name__ == "__main__":
    main()
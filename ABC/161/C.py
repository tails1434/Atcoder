def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
        exit()
    
    mod = N % K
    ans = min(mod, K - mod)
    print(ans)
    


if __name__ == "__main__":
    main()
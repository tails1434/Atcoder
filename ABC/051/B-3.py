def main():
    K, S = map(int, input().split())
    ans = 0
    for i in range(K+1):
        for j in range(K+1):
            tmp = i + j
            if 0 <= S - tmp <= K:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
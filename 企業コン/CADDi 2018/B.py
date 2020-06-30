def main():
    N, H, W = map(int, input().split())
    cnt = 0
    for _ in range(N):
        A, B = map(int, input().split())
        if A >= H and B >= W:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
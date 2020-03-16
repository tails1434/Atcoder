def main():
    N, A, B = map(int, input().split())
    C = A + B
    ans = (N // C) * A
    ans += min(A, N % C)
    print(ans)


if __name__ == "__main__":
    main()
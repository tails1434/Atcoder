def main():
    N = int(input())
    ans = set()
    for _ in range(N):
        S = input()
        ans.add(S)

    print(len(ans))
    


if __name__ == "__main__":
    main()
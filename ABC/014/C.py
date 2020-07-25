def main():
    n = int(input())
    ans = [0] * 1000002
    for _ in range(n):
        a, b = map(int, input().split())
        ans[a] += 1
        ans[b+1] -= 1

    C = [0] * 1000003
    for i in range(1000002):
        C[i+1] = ans[i] + C[i]

    print(max(C))

if __name__ == "__main__":
    main()
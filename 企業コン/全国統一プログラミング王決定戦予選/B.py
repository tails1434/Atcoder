def main():
    N = int(input())
    A = input()
    B = input()
    C = input()
    ans = 0
    for i in range(N):
        ans += len(set([A[i],B[i],C[i]])) - 1


    print(ans)


if __name__ == "__main__":
    main()
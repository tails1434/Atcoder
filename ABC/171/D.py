def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    D = [0] * (10**5+1)
    for i in range(N):
        D[A[i]] += 1

    ans = sum(A)
    for _ in range(Q):
        B, C = map(int, input().split())
        if D[B] != 0:
            ans -= B * D[B]
            ans += D[B] * C
            D[C] += D[B]
            D[B] = 0
            print(ans)
        else:
            print(ans)




if __name__ == "__main__":
    main()
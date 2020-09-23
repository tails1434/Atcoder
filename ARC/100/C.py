import statistics

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] -= i + 1
    B = statistics.median_low(A)
    ans = 0
    for a in A:
        ans += abs(a - B)

    print(ans)



if __name__ == "__main__":
    main()
def main():
    N = int(input())
    A = [0] * 5
    for i in range(5):
        A[i] = int(input())

    ans = 4 + (N // min(A) + (1 if N % min(A) > 0 else 0))
    print(ans)

main()
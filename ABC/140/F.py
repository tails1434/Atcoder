def main():
    N = int(input())
    S = list(map(int, input().split()))
    S_sort = sorted(S, reverse=True)

    A = [max(S)]
    for _ in range(2**N):
        A.append(d - 1 for d in A)

    print(A)



main()
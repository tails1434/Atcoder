def main():
    S = input()
    N = len(S)
    idx_a = ((N - 1) // 2)
    idx_b = ((N + 3) // 2) - 1
    A = S[:idx_a]
    B = S[idx_b:]
    if S == S[::-1] and A == A[::-1] and B == B[::-1]:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
from collections import defaultdict
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sort_A = sorted(A)
    sort_B = sorted(B)
    for i in range(N):
        if sort_A[i] > sort_B[i]:
            print('No')
            exit()
    


if __name__ == "__main__":
    main()
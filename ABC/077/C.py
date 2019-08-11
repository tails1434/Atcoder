import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    sort_A = sorted(A)
    sort_B = sorted(B)
    sort_C = sorted(C)
    cnt = 0
    for b in sort_B:
        a = bisect.bisect_left(sort_A, b)
        c = N - bisect.bisect_right(sort_C, b)
        cnt += a * c

    print(cnt)

main()
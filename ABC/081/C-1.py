import collections
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    TMP = [0] * N

    for i in A:
        TMP[i-1] += 1
    
    sort_TMP = sorted(TMP, reverse=True)
    max_ball = 0
    cnt = 1

    for a in sort_TMP:
        if cnt <= K:
            cnt += 1
            max_ball += a
        else:
            break
    
    print(N-max_ball)


main()
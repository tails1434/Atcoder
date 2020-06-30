def main():
    N = int(input())
    R = list(map(int, input().split()))
    if N <= 2:
        print(0)
        exit()

    for i in range(N-1):
        if not (R[i] > R[i+1]):
            break
    else:
        print(0)
        exit()

    for i in range(N-1):
        if not (R[i] < R[i+1]):
            break
    else:
        print(0)
        exit()

    cnt = 1
    now = R[0]
    for i in range(1,N):
        if cnt % 2 == 1:
            if now > R[i]:
                cnt += 1
                now = R[i]
            else:
                now = max(now, R[i])
        else:
            if now < R[i]:
                cnt += 1
                now = R[i]
            else:
                now = min(now, R[i])

    cnt1 = 1
    now1 = R[0]
    for i in range(1,N):
        if cnt1 % 2 == 0:
            if now1 > R[i]:
                cnt1 += 1
                now1 = R[i]
            else:
                now1 = max(now1, R[i])
        else:
            if now1 < R[i]:
                cnt1 += 1
                now1 = R[i]
            else:
                now1 = min(now1, R[i])
    ans = max(cnt, cnt1)
    if ans <= 2:
        print(0)
    else:
        print(ans)
if __name__ == "__main__":
    main()
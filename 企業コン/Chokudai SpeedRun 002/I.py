from collections import deque

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    que = [i for i in range(N)]
    Q = deque(que)
    while len(Q) > 1:
        one = Q.popleft()
        two = Q.popleft()

        cnt1 = (A[one] + (B[two] - 1)) // B[two]
        cnt2 = (A[two] + (B[one] - 1)) // B[one]
        
        if cnt1 >= cnt2:
            Q.append(one)
        if cnt1 < cnt2:
            Q.append(two)

    ans = Q.pop()
    for i in range(N):
        if i == ans:
            continue

        cnt1 = (A[i] + (B[ans] - 1)) // B[ans]
        cnt2 = (A[ans] + (B[i] - 1)) // B[i]

        if cnt1 >= cnt2:
            print(-1)
            exit()

    print(ans+1)

main()
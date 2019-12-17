import sys
input = sys.stdin.readline

def main():
    N, H = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    cnt = 0
    max_A = max(A)
    sort_B = sorted(B, reverse=True)
    for b in sort_B:
        if b > max_A:
            cnt += 1
            H -= b
        else:
            break

        if H <= 0:
            break
    
    if H > 0:
        cnt += H // max_A if H % max_A == 0 else H // max_A + 1
    print(cnt)



if __name__ == "__main__":
    main()
from collections import defaultdict

def s_int(s):
    return ord(s) - 97

def i_str(i):
    return chr(i+97)

def main():
    N = int(input())
    A = list(input() for _ in range(N))
    B = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            B[i][s_int(A[i][j])] += 1
    ans = [0] * N
    for i in range(N//2):
        a = B[i]
        b = B[-i-1]
        tmp = ''
        for j in range(26):
            if a[j] and b[j]:
                tmp = i_str(j)
                break
        else:
            print(-1)
            exit()
        ans[i] = tmp
        ans[-i-1] = tmp
        
    if N % 2 == 1:
        ans[N//2] = A[N//2][0]

    for a in ans:
        print(a, end="")

if __name__ == "__main__":
    main()
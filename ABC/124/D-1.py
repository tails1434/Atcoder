from itertools import accumulate

def length(S):
    cnt = 1
    A = []
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            A.append(cnt)
            cnt = 1
    else:
        A.append(cnt)

    return A

def main():
    N, K = map(int, input().split())
    S = input()
    lens = length(S)
    A = [0] + list(accumulate(lens))
    ans = 0
    if S[0] == '0':
        A = [0] + A
        for i in range(1,len(A)+1,2):
            right = i + 2 * K
            if right >= len(A):
                right = len(A) - 1
            tmp = A[right] - A[i-1]
            ans = max(ans, tmp)
    else:
        for i in range(1,len(A)+1,2):
            right = i + 2 * K
            if right >= len(A):
                right = len(A) - 1
            tmp = A[right] - A[i-1]
            ans = max(ans, tmp)

    print(ans)



if __name__ == "__main__":
    main()
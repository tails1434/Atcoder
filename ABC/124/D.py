import itertools

def main():
    N, K = map(int, input().split())
    S = input()

    A = []
    tmp = S[0]
    cnt = 0
    for i in range(len(S)):
        if S[i] == tmp:
            cnt += 1
        else:
            A.append(cnt)
            tmp = S[i]
            cnt = 1
    else:
        A.append(cnt)

    B = list(itertools.accumulate([0] + A))
    ans = 0
    if S[0] == '1':
        for i in range(1,len(B)+1,2):
            right = i + 2 * K
            if right >= len(B):
                right = len(B) - 1
            tmp = B[right]-B[i-1]
            ans = max(ans, B[right]-B[i-1])
    if S[0] == '0':
        C = [0] + B
        for i in range(1,len(C)+1,2):
            right = i + 2 * K
            if right >= len(C):
                right = len(C) - 1
            tmp = C[right]-C[i-1]
            ans = max(ans, C[right]-C[i-1])

    print(ans)

    
main()
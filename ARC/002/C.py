from itertools import combinations

def main():
    N = int(input())
    if N == 1:
        print(1)
        exit()
    C = list(input())
    cand = set()
    for a in ['A','B','X','Y']:
        for b in ['A','B','X','Y']:
            cand.add(a+b)
    cand = list(cand)
    ans = float('inf')
    for A in combinations(cand,2):
        cnt = 0
        flag = False
        for i in range(N-1):
            if flag:
                flag = False
                continue
            if C[i] + C[i+1] in A:
                cnt += 1
                flag = True

        ans = min(ans, N - cnt)

        flag = False
        cnt = 0
        for i in range(N-1,0,-1):
            if flag:
                flag = False
                continue
            if C[i] + C[i-1] in A:
                cnt += 1
                flag = True

        ans = min(ans, N - cnt)

    print(ans)

if __name__ == "__main__":
    main()
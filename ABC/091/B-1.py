import collections

def main():
    N = int(input())

    S = collections.defaultdict(int)
    for i in range(N):
        s = input()
        S[s] += 1
    
    M = int(input())
    for j in range(M):
        t = input()
        S[t] -= 1
    
    if max(S.values()) > 0:
        print(max(S.values()))
    else:
        print(0)

main()
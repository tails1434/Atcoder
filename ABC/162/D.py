from collections import defaultdict

def main():
    N = int(input())
    S = list(input())
    d = []
    c = [0,0,0]
    R = 0
    G = 0
    B = 0
    for i in range(N-1,-1,-1):
        if S[i] == 'R':
            R += 1
        if S[i] == 'G':
            G += 1
        if S[i] == 'B':
            B += 1
        d.append([R,G,B])
            
    d.reverse()
    ans = 0
    for i in range(N):
        if S[i] == 'R':
            ans += d[i][1] * d[i][2]
        if S[i] == 'G':
            ans += d[i][0] * d[i][2]
        if S[i] == 'B':
            ans += d[i][0] * d[i][1]
        for k in range(N):
            if i + 2 * k >= N:
                break
            if S[i] == 'R':
                if S[i + k] == 'G' and S[i + 2 * k] == 'B':
                    ans -= 1
                if S[i + k] == 'B' and S[i + 2 * k] == 'G':
                    ans -= 1 
            if S[i] == 'G':
                if S[i + k] == 'R' and S[i + 2 * k] == 'B':
                    ans -= 1
                if S[i + k] == 'B' and S[i + 2 * k] == 'R':
                    ans -= 1 
            if S[i] == 'B':
                if S[i + k] == 'R' and S[i + 2 * k] == 'G':
                    ans -= 1
                if S[i + k] == 'G' and S[i + 2 * k] == 'R':
                    ans -= 1 

    print(ans)
if __name__ == "__main__":
    main()
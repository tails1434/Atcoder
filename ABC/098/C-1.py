def main():
    N = int(input())
    S = input()
    W = [0] * (N + 1)
    E = [0] * (N + 1)

    for i in range(N):
        if S[i] == 'W':
            W[i + 1] = W[i] + 1
            E[i + 1] = E[i]
        else:
            W[i + 1] = W[i]
            E[i + 1] = E[i] + 1

    ans = float('inf')
    for i in range(N):
        ans = min(ans, W[i] + E[N] - E[i+1])
    
    print(ans)
        

main()
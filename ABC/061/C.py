def main():
    N, K = map(int, input().split())
    ans = [0] * (10 ** 5 + 1) 
    for i in range(N):
        a, b = map(int, input().split())
        ans[a] += b
    for i in range(10 ** 5 + 1):
        if K <= ans[i]:
            print(i)
            exit()
        else:
            K -= ans[i]
    
main()

    
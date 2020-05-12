def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K+1):
        cand = []
        for left in range(i+1):
            cand = V[:left]
            right = i - left
            cand += V[max(left,N-right):N]

            cnt = K - i
            n = len(cand)
            tmp = sum(cand)
            cand.sort()
            for c in range(min(cnt,n)):
                if cand[c] < 0:
                    tmp -= cand[c]
                else:
                    break
            ans = max(ans, tmp)


    print(ans)




        

if __name__ == "__main__":
    main()
def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0

    for left in range(K+1):
        for right in range(K+1):
            if left + right > K:
                continue
            tmp = []
            for i in range(min(N, left)):
                tmp.append(V[i])

            for j in range(max(left,N-right),N,1):
                tmp.append(V[j])

            nokori = K - left - right
            tmp.sort()
            tmp_sum = sum(tmp)
            for k in range(min(nokori, len(tmp))):
                if tmp[k] < 0:
                    tmp_sum -= tmp[k]

            ans = max(ans, tmp_sum)

    print(ans)





if __name__ == "__main__":
    main()
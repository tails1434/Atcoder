def main():
    N, K = map(int, input().split())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
        
    ans = float('inf')

    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if x[i] < x[j] and y[k] < y[l]:
                        right = x[j]
                        left = x[i]
                        bottom = y[k]
                        top = y[l]

                        cnt = 0

                        for n in range(N):
                            if left <= x[n] <= right and bottom <= y[n] <= top:
                                cnt += 1

                        if cnt >= K:
                            ans = min(ans, (top - bottom) * (right - left))
    print(ans)



if __name__ == "__main__":
    main()
N, K = map(int, input().split())

cnt = K * (K - 1) ** (N-1)
print(cnt)
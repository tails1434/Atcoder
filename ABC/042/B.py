N, L = map(int, input().split())
S = [input() for i in range(N)]

sort_S = sorted(S)

for s in sort_S:
  print(s, end ="")
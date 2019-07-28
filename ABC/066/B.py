S = list(input())

for i in range(len(S)):
  S.pop()
  if S[:(len(S) // 2)] == S[len(S) // 2:]:
    print(len(S))
    break
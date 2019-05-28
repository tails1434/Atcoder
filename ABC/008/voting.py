import collections

N = int(input())
S = [int(input()) for i in range(N)] 

c = collections.Counter(S)

max_k = max(c, key=c.get)
print(max_k)
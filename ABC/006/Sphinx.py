import itertools
import sys

N,M = map(int, input().split())

list1 = [2,3,4]

for v in itertools.combinations_with_replacement(list1, N):
    if sum(v) == M:
        a = [str(v.count(2)), str(v.count(3)), str(v.count(4))]
        result = ' '.join(a)
        print(a)
        sys.exit()

print('-1 -1 -1')
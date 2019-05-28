N = int(input())

T = 0

for i in range(1,10):
    for j in range(1,10):
        T += i * j

diff = T - N

for k in range(1,10):
    if diff % k == 0 and (diff // k) < 10:
        print("%d x %d"%(k,diff//k))


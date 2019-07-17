# ダメ元で全探索を実施
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

N, Ma, Mb = map(int, input().split())

a = [0] * N
b = [0] * N
c = [0] * N

for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

ans = float('inf')
for i in range(1 << N):
    tmp_a = 0
    tmp_b = 0
    tmp_c = 0
    for j in range(N):
        if ((i >> j) & 1) == 1:
            tmp_a += a[j]
            tmp_b += b[j]
            tmp_c += c[j]
    if tmp_a == 0 or tmp_b == 0:
        continue
    gcd_ab = gcd(tmp_a, tmp_b)
    if tmp_a / gcd_ab == Ma and tmp_b / gcd_ab == Mb:
        if ans > tmp_c:
            ans = tmp_c

if ans == float('inf'):
    print(-1)
else:
    print(ans)
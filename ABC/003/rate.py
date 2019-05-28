N,K = map(int, input().split())

R = list(map(int, input().split()))
R.sort()
len_R = len(R)

Rate = 0

for i in range((len_R - K), len_R):
    Rate = ( Rate + R[i] ) / 2

print(Rate)
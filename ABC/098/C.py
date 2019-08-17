N = int(input())
S = input()

ans = float('inf')
sum_E = [0]
sum_W = [0]
cnt_e = 0
cnt_w = 0

for i in range(N):
	if S[i] == 'E':
		cnt_e += 1
	else:
		cnt_w += 1
	sum_E.append(cnt_e)
	sum_W.append(cnt_w)


for i in range(N):
	ans = min(ans, sum_W[i] + sum_E[-1] - sum_E[i+1])

print(ans)
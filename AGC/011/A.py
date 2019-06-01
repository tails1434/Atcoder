N,C,K = map(int, input().split())

T = [int(input()) for i in range(N)]
sort_T = sorted(T)
a = 1 #バスの乗車人数
cnt = 1 #バスの台数
t = sort_T[0] + K #バスの一人目の到着時刻

for i in range(1,N):
    if a < C and sort_T[i] <= t:
        a +=1
    else:
        a = 1
        cnt += 1
        t = sort_T[i] + K

print(cnt)
A, B = map(int, input().split())

cnt = 0
for i in range (A, B+1):
    a = (i // 10000) % 10 #5桁目
    b = (i // 1000) % 10 #4桁目
    c = (i // 10) % 10 #2桁目
    d = i % 10 #1桁目
    if a == d and b == c:
        cnt += 1

print(cnt)

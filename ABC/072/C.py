# 辞書を用意して最大値を取得する

N = int(input())
a = list(map(int, input().split()))

cnt = {}

for i in a:
    for j in [-1,0,1]:
        cnt.setdefault(i+j, 0)
        cnt[i+j] += 1

print(max(cnt.values()))
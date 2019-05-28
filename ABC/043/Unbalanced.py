s = input()
len_s = len(s)
set_s =list(set(s))
cnt_s = 0
indexes = []
for i in set_s:
    cnt_s = s.count(i)
    if cnt_s >= len_s / 2:
        indexes = [j for j, x in enumerate(s) if x == i]

if indexes == []:
    print("-1","-1")
else: 
    print(min(indexes)+1, max(indexes)+1)


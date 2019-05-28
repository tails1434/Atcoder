N, K = map(int, input().split(" "))
list_num = ["0","1","2","3","4","5","6","7","8","9"]
D =  input().split(" ")

use_num = list(set(list_num) - set(D))
ok = []

for a in use_num:
    ok.append(a)
    for b in use_num:
        ok.append(a+b)
        for c in use_num:
            ok.append(a+b+c)
            for d in use_num:
                ok.append(a+b+c+d)
                for e in use_num:
                    ok.append(a+b+c+d+e)
ans = []
for i in ok:
    if int(i) >= N:
        ans.append(int(i))

print(min(ans))
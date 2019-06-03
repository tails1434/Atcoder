# 要素であるかの確認は配列じゃなくsetを使う
# setはハッシュで実装されているため

N = int(input())
s = set()
 
for i in range(N):
    a=int(input())
    if a in s:
        s.remove(a)
    else:
        s.add(a)
 
print(len(s))
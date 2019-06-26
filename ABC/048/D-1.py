s = list(input())
cnt = 0
while(1):
    tmp = 0
    for i in range(1,len(s)-1):
        if s[i-1] != s[i+1]:
            cnt += 1
            tmp = 1
            s.pop(i)
            break
    if tmp == 0:
        break

if cnt % 2 == 0:
    print("Second")
else:
    print("First")
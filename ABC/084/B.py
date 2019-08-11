A, B = map(int, input().split())
S = input()

if S.count('-') != 1:
    print('No')
else:
    f,s = S.split('-')
    if len(f) == A and len(s) == B:
        print('Yes')
    else:
        print('No')
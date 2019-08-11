C1 = input()
C2 = input()

if C1 == C2[::-1] and C1[::-1] == C2:
    print('YES')
else:
    print('NO')

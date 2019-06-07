A,B,C,D = map(int, input())

pattern1 = A + B + C + D
pattern2 = A + B + C - D
pattern3 = A + B - C + D
pattern4 = A + B - C - D
pattern5 = A - B - C + D
pattern6 = A - B - C - D
pattern7 = A - B + C + D
pattern8 = A - B + C - D

if pattern1 == 7:
    print(str(A)+'+'+str(B)+'+'+str(C)+'+'+str(D)+'='+str(pattern1))
    exit()

if pattern2 == 7:
    print(str(A)+'+'+str(B)+'+'+str(C)+'-'+str(D)+'='+str(pattern2))
    exit()

if pattern3 == 7:
    print(str(A)+'+'+str(B)+'-'+str(C)+'+'+str(D)+'='+str(pattern3))
    exit()

if pattern4 == 7:
    print(str(A)+'+'+str(B)+'-'+str(C)+'-'+str(D)+'='+str(pattern4))
    exit()

if pattern5 == 7:
    print(str(A)+'-'+str(B)+'-'+str(C)+'+'+str(D)+'='+str(pattern5))
    exit()

if pattern6 == 7:
    print(str(A)+'-'+str(B)+'-'+str(C)+'-'+str(D)+'='+str(pattern6))
    exit()

if pattern7 == 7:
    print(str(A)+'-'+str(B)+'+'+str(C)+'+'+str(D)+'='+str(pattern7))
    exit()

if pattern8 == 7:
    print(str(A)+'-'+str(B)+'+'+str(C)+'-'+str(D)+'='+str(pattern8))
    exit()
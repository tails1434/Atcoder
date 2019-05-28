N = int(input())

hh = N // 3600
mm1 = N % 3600
mm = mm1 // 60
ss = mm1 % 60

print(str(hh).zfill(2) + ':' + str(mm).zfill(2) + ':' + str(ss).zfill(2))
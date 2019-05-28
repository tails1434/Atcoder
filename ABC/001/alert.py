m = int(input())
 
km = m / 1000
a = 0
vv = ""
if km < 0.1:
    vv = "00"
elif 0.1 <= km <= 5:
    a = 10 * km
    vv = str(int(a))
    vv = vv.zfill(2)
elif 6 <= km <= 30:
    vv = str(int(km + 50))
    vv = vv.zfill(2)
elif 35 <= km <= 70:
    a = (km - 30) / 5 + 80
    vv = str(int(a))
    vv = vv.zfill(2)
elif km > 70:
    vv = "89"
 
print(vv)
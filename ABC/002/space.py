xa,ya,xb,yb,xc,yc = map(int, input().split())

a = xb - xa
b = yb - ya
c = xc - xa
d = yc - ya

space = abs(( a * d ) - ( b * c )) / 2
print(space)
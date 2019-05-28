s = input()
t = input()

sort_s = sorted(s)
sort_t = sorted(t, reverse=True)
if sort_s < sort_t:
    print('Yes')
else:
    print('No')
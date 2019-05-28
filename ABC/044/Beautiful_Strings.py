import sys
W = input()

set_w = set(W)

for i in set_w:
    if W.count(i) % 2 != 0:
        print("No")
        sys.exit()

print("Yes")
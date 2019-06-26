import re

S = input()

# 正規表現を用いて後ろからマッチするか考える

if re.match('dream|dreamer|erase|eraser+$', S):
    print('YES')
else:
    print('NO')
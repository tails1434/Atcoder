S = input()

S = S[::-1]

word_list1 = "dream"
word_list2 = "dreamer"
word_list3 = "erase"
word_list4 = "eraser"

s = ""
ans = ""

word_list = [word_list1[::-1],word_list2[::-1],word_list3[::-1],word_list4[::-1]]

for i in S:
    s += i
    if s in word_list:
        ans += s
        s = ""

if S == ans:
    print('YES')
else:
    print('NO')
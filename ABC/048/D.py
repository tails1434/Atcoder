s = input()

if len(s) % 2 == 0: # 偶数
    if s[0] == s[-1]: # 奇数
        print("First")
    else: # 偶数
        print("Second")
else: # 奇数
    if s[0] == s[-1]: # 奇数 
        print("Second")
    else: # 偶数
        print("First")
S = input()
T = input()

list1 = ['a','t','c','o','d','e','r']
flag = 0

for i in range(len(S)):
    if S[i] != T[i] and not ((S[i] == '@' and T[i] in list1) or (T[i] == '@' and S[i] in list1)):
        flag =+ 1
        break

if flag == 0:
    print('You can win')
else:
    print('You will lose')

A, B = map(int, input().split())
diff = A - B
if diff == -12:
    print('Alice')
elif -11 <= diff <= -1:
    print('Bob')
elif diff == 0:
    print('Draw')
elif 1 <= diff <= 11:
    print('Alice')
elif diff == 12:
    print('Bob')
def main():
    A, B = map(int, input().split())

    cnt = 0
    for i in range(A,B+1):
        str_i = str(i)
        if str_i[0] == str_i[4] and str_i[1] == str_i[3]:
            cnt += 1

    print(cnt)
    
main()
def main():
    S = 'T' + input()
    odd = ['R','U','D']
    even = ['L','U','D']
    for i in range(1,len(S)):
        if i % 2 == 0:
            if S[i] not in even:
                print('No')
                exit()
        if i % 2 == 1:
            if S[i] not in odd:
                print('No')
                exit()

    print('Yes')


main()
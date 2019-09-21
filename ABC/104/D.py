def main():
    S = input()
    MOD = 10 ** 9 + 7
    a = 0
    ab = 0
    abc = 0
    # ?によって分岐する文字列の総数
    total = 1
    for s in S:
        if s == 'A':
            a += total
        elif s == 'B':
            ab += a
        elif s == 'C':
            abc += ab
        else:
            # abcから実施しないと、足し算がおかしくなる
            abc = abc * 3 + ab
            ab = ab * 3 + a
            a = a * 3 + total
            total *= 3
        a %= MOD
        ab %= MOD
        abc %= MOD
        total %= MOD
    
    print(abc)


main()
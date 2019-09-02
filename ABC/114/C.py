import itertools

def main():
    N = int(input())

    num = ['3','5','7']
    num_list = set()

    for a in num:
        for b in num:
            for c in num:
                num_list.add(a+b+c)
                for d in num:
                    num_list.add(a+b+c+d)
                    for e in num:
                        num_list.add(a+b+c+d+e)
                        for f in num:
                            num_list.add(a+b+c+d+e+f)
                            for g in num:
                                num_list.add(a+b+c+d+e+f+g)
                                for h in num:
                                    num_list.add(a+b+c+d+e+f+g+h)
                                    for i in num:
                                        num_list.add(a+b+c+d+e+f+g+h+i)

    cnt = 0
    for i in num_list:
        if i.count("3") >= 1 and i.count("5") >= 1 and i.count("7") >= 1:
            if int(i) <= N:
                cnt += 1

    print(cnt)
    

main()
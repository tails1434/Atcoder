import collections

def main():
    n = int(input())
    v = list(map(int, input().split()))

    even = [j for i, j in enumerate(v) if i % 2 == 0]
    odd = [j for i, j in enumerate(v) if i % 2 == 1]

    cnt_e = collections.Counter(even)
    cnt_o = collections.Counter(odd)

    if len(set(v)) == 1:
        print(n // 2)
        exit()

    if cnt_e.most_common()[0][0] == cnt_o.most_common()[0][0]:
        if cnt_e.most_common()[0][1] > cnt_o.most_common()[0][1]:
            print(n - cnt_e.most_common()[0][1] - cnt_o.most_common()[1][1])
        elif cnt_e.most_common()[0][1] < cnt_o.most_common()[0][1]:
            print(n - cnt_e.most_common()[1][1] - cnt_o.most_common()[0][1])
        else:
            if cnt_e.most_common()[1][1] > cnt_o.most_common()[1][1]:
                print(n - cnt_e.most_common()[1][1] - cnt_o.most_common()[0][1])
            else:
                print(n - cnt_e.most_common()[0][1] - cnt_o.most_common()[1][1])
    else:
        print(n - cnt_e.most_common()[0][1] - cnt_o.most_common()[0][1])


main()
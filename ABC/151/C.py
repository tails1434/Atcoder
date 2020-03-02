def main():
    N, M = map(int, input().split())
    cnt = 0
    answer_list = [[] for _ in range(N)]
    for i in range(M):
        p, S = input().split()
        p = int(p) - 1
        answer_list[p].append(S)

    ac = 0
    wa = 0
    for answers in answer_list:
        tmp_wa = 0
        for a in answers:
            if a == 'AC':
                ac += 1
                wa += tmp_wa
                break
            else:
                tmp_wa += 1
    
    print(ac, wa)

    

if __name__ == "__main__":
    main()
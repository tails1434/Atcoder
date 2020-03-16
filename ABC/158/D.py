from collections import deque

def main():
    S = input()
    Q = int(input())
    cnt = 0
    dS = deque(S)
    for _ in range(Q):
        query = input()
        if query[0] == '1':
            cnt += 1
        else:
            A, F, C = query.split()
            if cnt % 2 == 0:
                if F == '1':
                    dS.appendleft(C)
                else:
                    dS.append(C)
            else:
                if F == '1':
                    dS.append(C)
                else:
                    dS.appendleft(C)

    if cnt % 2 == 0:
        print(*dS, sep ="")
    else:
        dS.reverse()
        print(*dS, sep ="")





if __name__ == "__main__":
    main()
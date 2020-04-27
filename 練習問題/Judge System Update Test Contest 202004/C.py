from itertools import permutations

def main():
    a1, a2, a3 = map(int, input().split())
    A = [a1,a2,a3]
    a = a1 + a2 + a3
    cand = list(range(1, a+1))
    cnt = 0
    for boxes in permutations(cand):
        A1 = [0] * a1
        A2 = [0] * a2
        A3 = [0] * a3
        i = 0
        flag = True
        for j in range(a1): 
            A1[j] = boxes[i]
            i += 1 
        for j in range(a2): 
            A2[j] = boxes[i]
            i += 1
        for j in range(a3): 
            A3[j] = boxes[i]
            i += 1
        
        X = [A1,A2,A3]
        for i in range(3):
            for j in range(1, A[i]):
                if X[i][j] <= X[i][j - 1]:
                    flag = False

        for i in range(1, 3):
            for j in range(A[i]):
                if X[i][j] <= X[i - 1][j]:
                    flag = False

        if flag:
            cnt += 1

    print(cnt)

        



if __name__ == "__main__":
    main()
from itertools import permutations

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    num_list = []
    for a in permutations(range(1,N+1)):
        num_list.append(a)
    num_list.sort
    b = -1
    c = -1
    for i, a in enumerate(num_list):
        if list(a) == P:
            b = i
        if list(a) == Q:
            c = i

        if b != -1 and c != -1:
            break

    print(abs(b-c))

    
            



if __name__ == "__main__":
    main()
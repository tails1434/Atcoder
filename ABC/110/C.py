def main():
    S = input()
    T = input()

    start = [-1] * 26
    goal = [-1] * 26

    for i in range(len(S)):
        a = ord(S[i]) - ord('a')
        b = ord(T[i]) - ord('a')

        if start[a] != -1 or goal[b] != -1:
            if start[a] != b or goal[b] != a:
                print('No')
                exit()
        
        start[a] = b
        goal[b] = a
    
    print('Yes')

main()
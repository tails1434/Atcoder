def main():
    N = int(input())

    paper = set()

    for i in range(N):
        A = int(input())
        if A in paper:
            paper.discard(A)
        else:
            paper.add(A)
    
    print(len(paper))

main()
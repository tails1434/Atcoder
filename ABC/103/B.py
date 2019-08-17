def rotate(word , n):
    return word[n:len(word)] + word[:n]

def main():
    S = input()
    T = input()

    for i in range(len(S)):
        if rotate(S,i) == T:
            print('Yes')
            exit()

    print('No')

main()
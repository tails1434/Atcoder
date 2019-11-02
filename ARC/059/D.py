def main():
    S = input()

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            print(str(i+1) + ' ' + str(i+2))
            exit()
    
    for i in range(len(S)-2):
        if S[i] == S[i+2]:
            print(str(i+1) + ' ' + str(i+3))
            exit()

    print('-1 -1')



if __name__ == "__main__":
    main()
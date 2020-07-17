"""
Having already mastered cooking, Chef has now decided to learn how to play the guitar. Often while trying to play a song,
Chef has to skip several strings to reach the string he has to pluck. Eg. he may have to pluck the 1st string and then the 6th string.
This is easy in guitars with only 6 strings; However, Chef is playing a guitar with 106 strings. In order to simplify his task,
Chef wants you to write a program that will tell him the total number of strings he has to skip while playing his favourite song.

"""
S = []

T = int(input())
if(T>=1 and T<=10):
    for i in range(T):
        num = 0
        del S[:]
        N = int(input())
        if(N>=2 and N<=100000):
            for j in range(N):
                ele = int(input())
                if(ele>=1 and ele<=1000000):
                    S.append(ele)
            for j in range(N-1):
                num = abs(S[j+1] - S[j] ) - 1 + num
            print(num)

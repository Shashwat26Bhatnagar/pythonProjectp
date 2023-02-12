def kmp(string: list, pattern: list,):
    n = len(string)
    m = len(pattern)
    lps=[0]*m

    for k in range(0,m-1):
        lps[k]=0
    prevlps=0
    i =  1
    while i < m:
        if pattern[i]==pattern[prevlps]:
            lps[i] = i + 1
            prevlps =+1
            i = i + 1
        elif prevlps == 0:
            lps[i] = 0
            i = i + 1
        else:
            prevlps = lps[prevlps - 1]
    i, j = 0, 0
    while i < n:
        if string[i] == pattern[j]:
            i =+1
            j =+1
        else:
            if j==0:
                i =+1
            else:
                j = lps[j - 1]
        if j == m:
            print(i - j)
    return -1


kmp("ababcabdaabcd", 'abc')

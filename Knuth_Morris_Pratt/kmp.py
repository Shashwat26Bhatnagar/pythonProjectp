def String(haystack:str,needle:str):
    if needle == "":return 0
    lps=[0]*len(needle)
    prevLPS,i=0,1
    while i<len(needle):
        if needle[i]==needle[prevLPS]:
            lps[i]=prevLPS+1
            prevLPS=prevLPS+1
            i=i+1
        elif prevLPS==0:
            lps[i]=0
            i=i+1
        else:
            prevLPS=lps[prevLPS-1]
    i=0#ptr for stack
    j=0#ptr for needle
    while i<len(haystack):
        if haystack[i]==needle[j]:
            i+=1
            j+=1
        else:
            if j==0:
                i=i+1
            else:
                j= lps[j-1]# say haystack= AAAXAA
                    #     needle=      AAAA
                    #             LPS=[0,1,2,3] so say after comparing first four elements of haystack 4th one is not matching so now check 2nd,3rd,4th,5th elements of haystack in needle but we know that 2nd ,3rd were already matching so seetinf j=lps[prev-1] we avoid to compare them again and that is the heart of our algorithm
        if j==len(needle):
            return i-len(needle)
    return -1

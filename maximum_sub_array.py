def max_seq(arr):
    l=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            l.append(sum(arr[i:j+1]))

    return max(max(l),0)

#kadane algorithm
#hash function which is compatible with sliding window technique is known as rolling hash function
def rabin_krap(s:list,p:list,d=26,q=101):
    n=len(s)
    m=len(p)
    h=pow(d,m-1)%q
#ideally rolliing hashing is (summation of (pi*d**(m-i-1)))%q
    # hash_p=sum(ord(p[i])*d**(m-i-1) for i in range(m))%q but this kind of expersion might led to overflow condition so we make some use of mathematical property of modulo function to change given function
    hash_p=0
    for i in range(m):
        hash_p=(d*hash_p+ord(p[i]))%q #This kind of representation is better but it represents the same thing as methioned above
        hash_s=(d*hash_s+ord(s[i]))%q
    for i in range(n-m+1):
        if hash_s==hash_p:
            print("p found in s")
        #heart of the algorithm
        if i<n-m:
            hash_s=(hash_s-ord(s[i]*h))%q
            hash_s=d*hash_s
            hash_s=(hash_s+ord(s[i+m]))%q
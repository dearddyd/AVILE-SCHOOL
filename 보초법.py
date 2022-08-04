def serch_sentinel(b,key):
    a=b.copy()
    a.append(key)
    
def seq_search(a,key):
    i=0
    while(1):
        if(i==len(a)):
            return -1
        if(a[i]==key):
            return i
        
i=0


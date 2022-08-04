def make_list(a):
    print("원소 값을 입력하시오 (END를 입력하면 끝납니다.)")
    i=1

    while(1):
        s=input("원소값을 입력하시오.: ")
        if(s=="END"):
            break
        a.append(s)
        i+=1
        
def max_list(a):
    idx=0
    for i in a:
        if(max(a)==i):
            print(idx,"가 인덱스입니다.")
            break
        idx+=1
    

def min_list(a,):
    for i in a:
        if(min(a)==i):
            print(idx,"가 인덱스입니다.")
            break
        idx+=1
    
        
a=[]
make_list(a)

max_list(a)
min_list(a)

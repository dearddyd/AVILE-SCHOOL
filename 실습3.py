def search_(ind,a):
    print(a[ind])
    if(ind>len(a)):
        print("잘못된 입력입니다.")
    

def make_list(a):
    print("원소 값을 입력하시오 (END를 입력하면 끝납니다.)")
    i=1

    while(1):
        s=input("원소값을 입력하시오.: ")
        if(s=="END"):
            break
        a.append(s)
        i+=1

a=[]
make_list(a)
ind=int(input("인덱스를 입력하시오.: "))
search_(ind,a)
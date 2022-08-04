def solution(store,customer):
    for i in customer:
        if(i in store):
            print("YES", end=" ")
        else:
            print("NO", end=" ")
    
    
def make_list(a):
    print("원소 값을 입력하시오 (END를 입력하면 끝납니다.)")
    i=1

    while(1):
        s=input("원소값을 입력하시오.: ")
        if(s=="END"):
            break
        a.append(s)
        i+=1
        
        
store=[]
print("매장의 부품번호를 입력하세요.")
make_list(store)

customer=[]
print("고객의 부품번호를 입력하세요.")
make_list(customer)

solution(store,customer)

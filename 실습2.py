a=[]
print("원소 값을 입력하시오 (END를 입력하면 끝납니다.)")
i=1

while(1):
    s=input("원소값을 입력하시오.: ")
    if(s=="END"):
        break
    a.append(s)
    i+=1

print(a[::-1])
    
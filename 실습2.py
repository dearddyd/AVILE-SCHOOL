Num=int(input("정수 값을 입력하시오.: "))
print("+와 -를 번갈아 출력합니다.")
for i in range(1,Num+1,1):
    if(i%2==1):
        print("+",end="")
    else:
        print("-",end="")
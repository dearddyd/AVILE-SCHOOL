Number=int(input("1~99사이의 정수를 입력하시오.: "))

a=0         #새로운 수는 AB
b=0
count=0
N=Number
while(1):
    if(Number<10):
        N=N*10
    A=N%10
    B=N//10 + N%10
    if(B>10):
        B=B%10
    N=A*10+B
    count+=1
    if(Number==N):
        print(Number,"의 사이클 길이는 ",count,"이다.")
        break

    
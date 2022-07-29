n=int(input("직사각형의 넓이를 입력하시오.: "))

for i in range(1,n+1):
    if(n%i==0):
        print(i,"*",n//i)
    
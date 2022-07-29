a=int(input("정수를 입력하시오.: "))
Sum=0
for i in range(1,a+1):
    if(i<a):
        print(i,"+",end="")
    else:
        print(i,"=",end="")
    Sum+=(i)
print(Sum)
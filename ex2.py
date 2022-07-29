#최소공배수 찾기

num1=int(input("정수를 입력하시오.: "))
num2=int(input("정수를 입력하시오.: "))

if(num1<num2):
    num1,num2=num2,num1

Max_result=0
for i in range(1,num1+1,1):
    if(num1%i==0 and num2%i==0):
        Max_result=i

Min_result=0
a=num1/Max_result
b=num2/Max_result
Min_result=int(a*b*Max_result)
print("최소공배수는 ",Min_result,"이다.")
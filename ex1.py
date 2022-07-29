#두 정수의 최대 공약수 찾기

num1=int(input("정수를 입력하시오.: "))
num2=int(input("정수를 입력하시오.: "))

if(num1<num2):
    num1,num2=num2,num1

result=0
for i in range(1,num1+1,1):
    if(num1%i==0 and num2%i==0):
        result=i

print("최대공약수는 ",result,"이다.")
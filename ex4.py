left=int(input("정수를 입력하시오.:"))
right=int(input("정수를 입력하시오.: "))

if(left>right):
    left,right=right,left
count=0
Sum=0
for i in range(left,right+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count%2==0):
        Sum+=i
    else:
        Sum-=i
print(Sum)

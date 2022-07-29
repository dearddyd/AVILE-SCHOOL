Num=int(input("정수를 입력하시오.: "))

root=0
pwr=0

for root in range(1,Num+1,1):
    for pwr in range(2,7,1):
        if(root**pwr==Num):
            print(root,"**",pwr,)
        
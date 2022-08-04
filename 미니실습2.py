from asyncio.windows_events import NULL


def revers_func(a):
    for i in range(len(a)//2):
        a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
    
    
    for j in range(len(a)):
        print(f"x[{j}]=",a[j])


print("리스트를 역순으로 출력합니다.")
num=int(input("원소 수를 입력하세요. : "))

a=[NULL]*num

for i in range(num):
    a[i]=int(input(f"x[{i}]값을 입력하세요. : "))

print("리스트의 역순이 출력됩니다.")
revers_func(a)

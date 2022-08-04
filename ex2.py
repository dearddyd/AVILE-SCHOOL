def Sol(a):
    sum_=0
    for i in range(10):
        if(i not in a):
            sum_+=i
    return sum_

a=[1,2,3,4,6,7,8,0]
b=[5,8,4,0,6,7,9]

print(Sol(a))
print(Sol(b))


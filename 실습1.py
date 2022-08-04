

from asyncio.windows_events import NULL

a=[]
a.append(2)
a.append(3)
a.append(5)
a.append(7)
for i in range(2,1000,1):

    if(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
        a.append(i)
print(a)


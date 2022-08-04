a=[5,7,15,28,28,31,39,58,68,70,95]
pl=0
pr=len(a)-1
pc=len(a)//2

key=int(input("검색값 : "))

while(1):
    if(a[pc]!=key):
        if(a[pc]<key):
            pl=pc+1
        else:
            pr=pc-1
    else:
        print("검색값은 a[",pc,"]에 있습니다,")
        break
    
    if(pl==pc and pc==pr):
        print("찾는 값이 없습니다.")
        break
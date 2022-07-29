def electricPay(use):
    base=0
    pay=0
    if(use>200):
        base=1600
        pay=100*60.7+100*125.9+(use-200)*187.9+base
        RealPay=pay+pay*0.1+pay*0.03
        return int(RealPay)
    elif(use<=200 and use>=100):
        base=910
        pay=100*60.7+(use-100)*125.9+base
        RealPay=pay*0.1+pay*0.03+pay
        return int(RealPay)
    else:
        base=410
        pay=use*60.7+base
        RealPay=pay*0.1+pay*0.03+pay
        return int(RealPay)

Use=int(input("사용량을 입력하시오.: "))
print(electricPay(Use),"원 입니다.")
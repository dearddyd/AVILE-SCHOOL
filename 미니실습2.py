def waterpay(company, use):
    if(company=="A"):
        pay=use*100
        return pay
    elif(company=="B"):
        if(use>50):
            pay=use*75
            return pay
        else:
            pay=use*150
            return pay
    else:
        print("잘못된 입력입니다.")
        
company=input("회사를 입력하시오. ")
use=int(input("사용량을 입력하시오. "))

print("금액은 ",waterpay(company,use),"원 입니다.")
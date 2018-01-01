# 리스트 반복문
stocks = ["카카오","네이버","삼성전자"]
for stock in stocks:
    print("%s - " % stock)

# 튜플 반복문
money = (100,200,300)
for won in money:
    print("%d 원" % won)


# 딕셔너리 반복문
"""
딕셔너리의 한 원소에는 키와 값이 있기 때문에 for 문 다음에 있는 변수가 한 개가 아니라 두 개를 적어야 합니다.
그리고 딕셔너리 이름을 적은 다음 .items( )를 붙여야 합니다.
"""
interest_stocks = {"Naver":10, "Samsung":5, "SK Hynix":30}
for company, stock_num in interest_stocks.items():
        print("%s : %d" % (company, stock_num))

for company in interest_stocks.keys():
    print("%s : %d" % (company, interest_stocks[company]))


# --------------------------------------------
# 위 문법은 옛날 방식 아래가 새로운 문법 방식
for company, stock_num in interest_stocks.items():
    print('{} : {}'.format(company, stock_num))
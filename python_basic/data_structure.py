# 파이썬의 자료구조
"""
 파이썬의 기본 자료구조
 - 리스트 []
    자바스크립트의 [] 배열 형태로 보면 된다. 인덱싱, 리스트 슬라이싱, 삽입, 삭제 등등의 여러 기능을 지원한다.
 - 튜플 ()
    리스트가 제공하는 여러 함수들을 제공하지 않는 경우가 많다. 단 데이터 처리속도는 엄청나다.
 - 딕셔너리 {}
    키-값 으로 되어 있다. 리스트 처럼 삽입,삭제를 제공한다.
"""


# --------- 리스트 [] 예제 ----------
stock = ["카카오","삼성전자","네이버"]
# 인덱싱
print(stock[0])
print(stock[1])
print(stock[2])
print(stock[-3])
print(stock[-2])
print(stock[-1])
# 슬라이싱
print(stock[0:2])
print(stock[0:])
print(stock[:2])
# 데이터 삽입
stock.append("아마존")
print(stock)
stock.insert(1,"구글")
print(stock)
# 데이터 삭제
del stock[-1]
print(stock)

len(stock)
# -------------------------------
# --------- 튜플 () 예제 ----------
"""
1) 리스트는 '[' 와 ']'를 사용하는 반면 튜플은 '('와 ')'를 사용한다. 
2) 리스트는 리스트 내의 원소를 변경할 수 있지만 튜플은 변경할 수 없다. 
"""

friends = ("소싸", "충엽", "승한")
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-3])
print(friends[-2])
print(friends[-1])


# -------------------------------
# -------- 딕셔너리 {} 예제 ---------
"""
딕셔너리는 리스트나 튜플과 달리 원소를 추가한 순서대로 데이터가 저장돼 있지 않기 때문에 딕셔너리에 추가한 데이터를 얻으려면 키 값을 사용해야 합니다
key : value의 JSON , java의 Map,Set 과 비슷한 형태이다.
"""

coins = {'비트코인': 800, '이더리움': 40, '퀀텀': 1.5, '대쉬': 50}
print(coins)
print(coins['비트코인'])
# 데이터 삽입/ 삭제
coins['에너고'] = 1
del coins['비트코인']
print(coins)

# 키 - 값
keys = list(coins.keys())
print(keys)
values = list(coins.values())
print(values)
print('이더리움' in coins.keys())
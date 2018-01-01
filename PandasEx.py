import pandas as pd
from pandas import Series, DataFrame

print(pd.__version__)


s = Series([7, 0, -3, 8, 1])
print(s.values)
print(s.values[1])
print(s.values[2])
print(s.index)

s = Series({'A':7, 'B':0, 'C':-3, 'D':8})
print(s)


s = Series({'A':7, 'B':0, 'C':-3, 'D':8})
print (s[0:3])      # 숫자 인덱스는 0에서 시작, 끝점은 포함하지 않는다.
print (s['A':'C'])  # 라벨 이름은 끝점을 포함


# series 누락 데이트!!
a = Series([2, 3, 6, -4], index=['A', 'B', 'C', 'D'])
b = Series([10, 2, 3, 8], index=['B', 'C', 'D', 'E'])

c = a + b
print(c)
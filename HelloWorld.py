import sys;
import numpy as np;

# 파이썬 금융데이터 수집 및 분석 과정
"""
   파이썬 기본 데이터 타입
   int      4byte    무제한
        * 버전 2에서는 실수형을 int와 long으로 나뉘어 졌고, int는 [-2^31 ~ 2^31-1]의 범위가 있었고
          long은 [무제한] 이였다. 그러나 버전 3에서 통합되었으며, int는 범위가 무제한이다.
   float    8byte   약 10-308 ~ 10+308
   boolen   2bit
   str      4byte
        * str은 java에 String 이라고 보면 되겠다. 특이한 점들은 python의 str에서는 java에서 String과 관련된
          여러 외부지원 기능을 함축하고 있다. 예를들어 보면 split(), substring() 등등의 기능들이 되겠다.
"""

# ex 1>
a = 1;
b = 0.2;
c = False;
d = "Hello";

print(a, "/ ", b, "/ ", c, "/ ", d);
# 위의 예제에서 보면 ,라는 신텍스로 값을 출력할 수 있다.


print('=================================================')

print(sys.version);
# 특정 모듈 import

print('=================================================')

zin_8 = '0o12'         # 8진 정수
zin_16 = '0xa'          # 16진 정수
zin_2 = '011010'       # 2진 정수

zin_8 = int('0o12', 8)      # 16진수 문자열을 정수형으로 변환
zin_16 = int('0xa', 16)      # 16진수 문자열을 정수형으로 변환
zin_2 = int('011010', 2)    # 2진수 문자열을 정수형으로 변환

print(type(zin_8), type(zin_16), type(zin_2))
print(zin_8, zin_16, zin_2)

print('=================================================')

a = 1.2
b = 3.5e3       # 뒤에 나오는 5e3은 뭐? 진법과 관련된 수인가?
c = -0.2e-4     # 그렇다 하더라도 - 라는 신텍스가 변환이 가능한건가?
print(type(a), type(b), type(c))
print(a, b, c)

print('=================================================')

h2 = 123456789012345678901234567890     # python3에서 int형은 무제한이다.
print(type(h2))


print('=' * 40)
ar = np.array([10, 20, 30, 40])
print(ar.dtype)
ar = np.array([10, 20, 30., 40.])
print(ar.dtype)
ar = np.array([10, 20, 30., 40.], dtype='int')
print(ar.dtype)

print('=' * 40)
ar = np.arange(0,16).reshape((4,4))

print(ar)
print('~' * 40)
print(ar[0])
print('~' * 40)
print(ar[1,1])

print('=' * 40)
print(ar)
print('~' * 40)

ar[2, 0:3] = 88         # 배열의 크기를 넘어가도 에러가 나질 않는다.
print(ar)


print('=' * 40)
ar = np.arange(0,16).reshape((4,4))
# - 인덱스는 해당 갯수 로우를 제외한~ 이라고 보면 되겠다.

print(ar)
print('~' * 40)
print(ar[-2])
print('~' * 40)
print(ar[-2:])
print('~' * 40)
print(ar[:-2])


print('=' * 40)
ar = np.array([[0, 1, 2], [10, 11, 12], [20, 21, 22], [30, 31, 32]])
print(ar)
print('~' * 40)

p = ar * 10
print(p)


print('=' * 40)
ar = np.array([[10, 20, 30], [60, 70, 80], [90, 91, 92]])
v = ar[1]
t = ar[1].copy

v[:] = 50   # v 배열 전체 요소에 20을 할당
t = 40

#  v는 ar의 뷰, v의 값을 변경하는 것은 ar의 값을 변경
print(ar)
print(v)
print(t)


print('=' * 40)
city = np.array(['newyork', 'seoul', 'shanghai', 'tokyo', 'london'])
val = np.array([10, 20, 30, 40, 50])

print(city == 'seoul')         # array([False, True, False, False, False], dtype=bool)
print(val[city == 'seoul'])   # array([20])
print(city[val >= 30])         # array(['shanghai', 'tokyo', 'london'], dtype='<U8')
print(city[city != 'tokyo'])    # array(['newyork', 'seoul', 'shanghai', 'london']

mask = (city == 'shanghai') | (city == 'tokyo') | (city == 'london')
print(val[mask])
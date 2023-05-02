from pandas import Series, DataFrame


mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

#파이썬은 반복문을 통해 데이터를 관리할 수 있음
#하단이 예시

for stock in mystock:
    print(stock)

#튜플은 ()사용, 수정 X, 리스트와 달리

#딕셔너러니는 키값으로 쌍으로 데이터를 저장함

exam_dic = {'key1': 'room1', 'key2':'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])

import pandas
from pandas import Series, DataFrame


kakao = Series([92300, 94300, 92100, 92400, 92600])


kakao_daily_ending_prices = {'2016-02-19': 92600,
                             '2016-02-18': 92400,
                             '2016-02-17': 92100,
                             '2016-02-16': 94300,
                             '2016-02-15': 92300}
print(kakao_daily_ending_prices['2016-02-19'])

print(pandas.Series)
print(kakao)
print(kakao[0])

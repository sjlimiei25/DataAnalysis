# pandas/4_data_processing.py
import pandas as pd
import numpy as np

# * products.csv 파일 데이터 읽어오기
# df = pd.read_csv('products.csv')

# * 특정 컬럼은 index로 지정해서 읽어오기

df = pd.read_csv('products.csv', index_col='id')
# 상위 5개 데이터 출력하기 => head()
# 마지막 5개 => tail()
print(df.head())

print(f'index: {df.index}')
print(f'columns: {df.columns}')

# df['상품명']

# * 행/열 선택(인덱싱) 및 범위 선택(슬라이싱) : loc, iloc
#     loc (Label Location) : 라벨 기반 선택
#       loc[행_선택,열_선택]
#       - 행 선택 : 인덱스 라벨(문자열, 숫자, 지정한 이름..)
#       - 열 선택 : 컬럼 라벨(열 이름, 문자열, ...)
#       => 슬라이싱 시 끝 라벨을 포함!

#     iloc (Integer Location) : 정수(위치) 기반 선택
#       iloc[행_선택,열_선택]
#       - 행 선택 : 0부터 시작하는 순서(위치)
#       - 열 선택 : 0부터 시작하는 순서(위치)
#     => 위치 기반으로 기존 슬라이싱과 동일. 끝 위치(인덱스) 미포함(제외)

def practice_loc():
  print("* ==== 상품명만 조회(출력) ==== *")
  # 상품명 -> 컬럼
  print(df['상품명'])     # 데이터 프레임에 []로 인덱싱할 때는 컬럼을 기준으로 선택. 행 x

  print("* ==== 113번 행의 데이터 조회 ==== *")
  print(df.loc[113])      # 행 인덱스로 접근하고자 할 경우 loc, iloc 사용

  print("* ==== 113번 행의 상품명 조회 ==== *")
  print(df.loc[113, '상품명'])

  print("* ==== 113번 행의 상품명, 가격 조회 ==== *")
  print(df.loc[113, ['상품명', '가격']])    # 여러 개의 열을 리스트 형태로 전달
  print(df.loc[113, '상품명':'가격'])       # 슬라이싱 적용

  print("* ==== 110번 행의 상품명, 재고 조회 ==== *")
  # 리스트 방식
  print(df.loc[110, ['상품명', '재고']])

  # 슬라이싱 방식
  print(df.loc[110, '상품명':'재고':2])

# practice_loc()

def practice_iloc():
  print("* ==== 첫번째 행의 전체 컬럼 조회 ==== *")
  print(df.iloc[0])
  # print(df.iloc[0, 0:4:1])  

  print("* ==== 첫번째 행의 마지막 컬럼 조회 ==== *")
  print(df.iloc[0, -1])     # => Scalar
  # print(df.iloc[0, ::3])  # => Series

  print("* ==== 3~5번째 행의 모든 컬럼 조회 ==== *")
  print(df.iloc[2:5])
  print(df.iloc[2:5, :])

  print("* ==== 3~5번째 행의 두번째 컬럼 조회 ==== *")
  print(df.iloc[2:5, 1])

# practice_iloc()

'''
    데이터프레임(DataFrame)의 인덱스는 반드시 숫자가 아닐 수 있음.
    문자나 날짜 등 다양한 값이 라벨이 될 수 있음
    따라서, 위치(index)로 선택하는 것인지, 라벨(label)로 선택하는 것인지 모호해질 수 있음.

    이러한 혼란을 방지하고 의도를 명확하게 하기 위해
    판다스(Pandas)에서는 라벨 기반 선택은 loc, 위치 기반 선택은 iloc로 구분하여 기능 제공.
'''

# ====================================================

# * 새로운 컬럼 생성
#   df[추가할_컬럼명] = 저장할_데이터
def add_column_test():
  df_test = df.copy()       # copy(): 복사본 배열 생성

  df_test['TEST'] = '테스트 데이터'
  print(df_test.head(1))

  df_test = df_test.drop(columns=['TEST'])
  print(df_test.head(1))

# add_column_test()

def add_total_price():
  # df 사용
  print("* ==== 총 금액 컬럼 추가 ==== *")
  # 총 금액 = 가격 * 재고 
  df['총 금액'] = df['가격'] * df['재고']

  print(df.head())

  print("* ==== 재고 수량에 따른 상태 컬럼 추가 ==== *")
  # 재고 상태 => 재고가 130미만이면 '부족', 그렇지 않으면 '충분'
  # numpy.where(조건, 조건만족시_사용할값, 만족하지_않을경우_사용할값)
  df['재고 상태'] = np.where(df['재고'] < 130, '부족', '충분')

  print(df.head())

  print("* ===== 재고 상태별 데이터 개수 조회 =====  *")
  print(df['재고 상태'].value_counts())

# add_total_price()

# ====================================================

# * 문자열 처리
def str_processing():
  # * 상품명 정보 조회
  print( df['상품명'] )

  # 괄호가 포함된 상품의 정보 분리 ==========

  # 1) 괄호를 기준으로 분리

  # df.str : 시리즈(컬럼) 내의 데이터가 문자열이거나 문자열 리스트일 때,
  #          문자열 자체에 접근 가능한 방법 (특별한 통로)
  #          => 전체 데이터를 대상으로 문자열 처리 가능

  # str.split(구분자, n=분리횟수, expand=컬럼확장여부)
  #     * n : 구분자에 해당하는 부분이 여러 개일 때 몇 번 분리할 것인지
  #     * expand : False - 리스트 시리즈 형태로 반환 (하나만 빠르게 추출할 때)
  #                True - 데이터프레임 형태로 반환 (하나의 컬럼을 여러 개의 독립된 컬럼으로 나눌 때. 일반적인 방식)

  # 구분자, 분리횟수 설정하여 분리 
  #   '('      1
  split_df = df['상품명'].str.split('(', n=1)
  print(split_df)

  print(split_df.str[0])  # 첫번째 요소(메인 이름)만 추출
str_processing()
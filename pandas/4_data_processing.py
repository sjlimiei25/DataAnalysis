# pandas/4_data_processing.py
import pandas as pd

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

practice_iloc()
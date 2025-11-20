# pandas/1_basic.py

# pandas 사용 시 import pandas
import pandas as pd

# * Series : 라벨링된 1차원 배열 구조
#    - 생성 
#           pd.Series(저장할_데이터)
#           -> index 항목 생략 시 정수로 자동 생성(0~)

# Series 생성
s = pd.Series([10, 20, 30, 40])
print(s)
'''
0       10
1       20
2       30
3       40
인덱스  데이터
'''
print(f'values : {s.values}')     # 실제 저장된 데이터
print(f'index  : {s.index} / {s.index.to_list()}')      # 인덱스 정보
print(f'dtype : {s.dtype}')     # 요소의 데이터 타입

# -------------------------------------
print('-'*30)

# 인덱스를 지정하여 Series 생성
s2 = pd.Series([3.14, 23.5, 20.0], index=['f1', 'f2', 'f3'])
print(s2)
'''
f1      3.14
f2      23.50
f3      20.00
인덱스 데이터
'''
print(f'dtype : {s2.dtype}')
print(f'index : {s2.index}')

s3 = pd.Series(['햄버거', '제육', '국밥'])
print(s3)
# ---------------------------------------------
print("="* 30)


# * DataFrame : 2차원 테이블 구조, Series들로 구성되어 있음!
#   - 생성
#         pd.DataFrame(저장할_데이터)

# DataFrame 생성
data = {
  'name': ['대성', '성민', '형진', '치민'],
  'age': [20, 36, 21, 26],
  'addr': ['LA', '인천', '죽전', '서울'],
  'score': [75.0, 60.5, 82.7, 50.3]
}
df = pd.DataFrame(data)
print(df)

print(f'index (행의 인덱스) : {df.index} / {df.index.to_list()}')
print(f'columns (열의 인덱스) : {df.columns} / {df.columns.to_list()}')
print(f'values (실제 데이터) : {df.values}')
print(f'dtypes (요소 타입, 컬럼(열) 기준) : {df.dtypes}')


# * DataFrame 요약 정보
print(f'--- DataFrame 요약정보: info() ---')
df.info()

# * DataFrame 요약 통계
print(f'--- DataFrame 요약 통계: describe() ---')
print(df.describe())
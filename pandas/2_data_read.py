# pandas/2_data_read.py
import pandas as pd

'''
    CSV (Comma Separated Values)
    : 쉼표로 구분되어 있는 데이터
    : 저장과 교환이 간편하여 많이 사용되는 형식 중 하나
    : 각 행(Row)은 하나의 정보(레코드)를 의미하고,
      첫번째 행은 일반적으로 컬럼명(header)을 의미함
'''

# * CSV 파일 일기 (read_csv) 
#    pd.read_csv(파일명) => DataFrame
df = pd.read_csv('students.csv')
# print(df)

# * head() : 초기 데이터프레임 확인
# print(df.head(n=1))
# => 데이터 중 앞 부분의 5개(기본개수) 내용 반환

# * tail() : 마지막 5개(기본개수) 데이터 확인
# print(df.tail(n=1))

# ===============

# * 초기 점검
# 전체 정보 확인 : info()
df.info()

# 통계 요약 정보 : describe()
print(df.describe())

## ------------

# 상위 3개 데이터, 하위 2개 데이터 확인
print(df.head(n=3))
print(df.tail(n=2))

print('-'*30)

# hobby 컬럼의 데이터만 확인
print( df['hobby'] )

# 이름만 확인 => 'name' 컬럼
print( df['name'] )

# 고유값 확인 : value_counts()
#  => 취미 컬럼의 고유값 확인
print(df['hobby'].value_counts())
# => 중복되는 데이터가 많은 순서로 결과 확인
print('-'*30)
# * 컬럼별 결측치 확인
#   => 컬럼별 결측치 개수
print( df.isnull() )
print( df.isnull().sum() )

# * 특정 컬럼의 고유값 확인 : unique()
print( df['hobby'].unique())

print(df)
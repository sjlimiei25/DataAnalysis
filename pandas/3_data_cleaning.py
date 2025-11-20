# pandas/3_data_cleaning.py
import numpy as np
import pandas as pd

data = {
  'no': [1, 2, 3, 4, 1, 1,  
         5, 6, 7, 8, 9],
  'name': ['민성', '성빈', '승준', '민환', '수정', '민성', 
            '장훈', '재환', '지훈', '성호', '진형'],
  'age': [25, 30, 33, 20, np.nan, 20,
          np.nan, 147, 31, 27, 70],
  'score': [88.2, 66.9, np.nan, np.nan, 77.7, 20,
            92.5, 87.6, 67.8, 89.0, 72.5],
  'is_active': ['ok', 'nok', 'ok', 'nok', 'nok', 'ok',
                'ok', 'ok', 'ok', 'nok', 'ok']
}
# no : 중복 데이터 존재
# age, score : 결측치 포함

# DataFrame 객체 생성
df = pd.DataFrame(data)

print(df)
print('-'*30)

# * 컬럼별 결측치 개수 확인
print('* ---- 컬럼별 결측치 개수 ---- *')
print(df.isnull().sum())

# * 결측치 데이터를 다른 값으로 대체
#   대상.fillna(대체할_값)

#   age 컬럼의 결측치를 0으로 대체
print('* --- 결측치 대체 전 --- *')
print(df['age'])

'''
df['age'] = df['age'].fillna(0)
print('* --- 결측치 대체 후 --- *')
print(df['age'])
'''
# age 컬럼의 중앙값 : median()
print(df['age'].median())

# --- age 컬럼의 결측치를 중앙값으로 대체 ---
print(df)
age_median = df['age'].median()
df['age'] = df['age'].fillna(age_median)

print('* --- 결측치 대체 후 --- *')
print(df['age'])

# * 결측치 제거 : df.dropna(subset=[컬럼])

print(df['score'])
df_drop = df.dropna(subset=['score'])
print(df_drop['score'])
print(df_drop['score'].isnull().sum())


print(df_drop)

# * 중복값 처리 ---------------------------------
print(df_drop)
print('-'*30)
print( df_drop.duplicated(subset=['no', 'name']) )    # 중복 여부 확인

# 중복 행 제거
df_drop = df_drop.drop_duplicates(subset=['no', 'name'], keep='last')
print('---- 중복 행 제거 ----')
print(df_drop)

print('----- 데이터 타입 변환 ------------------ *')
# ----- 데이터 타입 변환 ------------------ *
#  대상.astype(변환할_타입)

# is_active : 'ok' / 'nok' --> True / False

print(df_drop['is_active'])
df_drop['is_active'] = df_drop['is_active'].map({'ok': True, 'nok': False}).astype(bool)

print('---- 변환 후 데이터 ----')
#print(df_drop['is_active'])

# age 컬럼의 데이터를 float -> int 변환
df_drop['age'] = df_drop['age'].astype(np.int64)
#print(df_drop['age'])

# * 모든 컬럼의 데이터타입... dtypes
print(df_drop.dtypes)


#  ---------- 불필요한 컬럼 제거 ------------------
#      drop()
# name 컬럼을 제거 -> 분석에서 사용되지 않는 항목

df_last = df_drop.drop(columns=['name'])
print('* ---- 최종 데이터 프레임 ---- *')
print(df_last)
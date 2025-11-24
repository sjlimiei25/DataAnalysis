# pandas/6_data_analysis.py
import pandas as pd
import numpy as np

# data.csv 파일을 읽어 df 변수에 저장
df = pd.read_csv('data.csv')

# 데이터 정보 :
# Region : 판매 지역
# Product_Category : 상품 카테고리
# Sales_Amount : 판매 금액
# Units_sold : 판매 수량
# Customer_Rating : 고객 평점
# Promotion_Used : 프로모션 사용 여부 ('Yes' / 'No')

# print(df.head())

# * =========== 전처리 ============== *
# * 프로모션 사용 여부 컬럼의 데이터를 'Yes' 또는 'No'로 통일
#     'Y' -> 'Yes'
df['Promotion_Used'] = df['Promotion_Used'].replace('Y', 'Yes')
# print(df.head())

# df.groupby(컬럼명) : 그룹화 기준 컬럼을 지정하여 GroupBy 객체 생성
#         - 객체 생성 후 집계 함수(mean, median, sum 등)를 지정함.
#         - ex) median() 호출 시, 그룹화 기준 외의 모든 숫자 컬럼에 대해 중앙값을 계산
#         - 만약 데이터 프레임에 문자열이나 결측치 등 중앙값을 계산할 수 없는 
#           데이터가 많으면 오류 발생 또는 잘못된 결과가 나옴 (=> 전처리 후 진행!)

# df.groupby(컬럼명)[집계대상컬럼] : 그룹화 기준 컬럼 지정 후 집계 수행 대상 컬럼 선택


# * transform()  : groupby로 그룹화된 데이터에 집계함수 적용 시 사용
#                  원본 데이터프레임의 행 수와 동일한 크기로 결과 반환 (모든 행에 집계 함수 적용)
#       df.groupby(컬럼명)[집계대상컬럼].transform(집계함수)

# * aggregate() / agg() : groupby로 그룹화된 데이터에 집계함수 적용 시 사용
#                         그룹 수만큼 결과 개수 축소 (요약 통계). 그룹 별로 1개의 행만 반환
#       df.groupby(컬럼명)[집계대상컬럼].agg(집계함수)

# 지역별 판매 금액 통계 (평균, 총합, 개수)
region_agg = df.groupby('Region')['Sales_Amount'].agg(['mean', 'sum', 'count'])
print('* === agg === *')
print(region_agg)
# => 지역별로 판매금액의 평균, 총합, 개수를 각각 출력(표시)

# 지역별 평균 계산
region_mean = df.groupby('Region')['Sales_Amount'].transform('mean')
print('* === tranform === *')
print(region_mean)
# => 모든 행에 결과 표시. 같은 지역인 행은 같은 결과가 표시.

# * 고객 평점 컬럼 결측치 확인
#   - 고객 평점 컬럼의 결측치 개수
print(f' Customer_Rating 결측치 개수 : {df["Customer_Rating"].isnull().sum()}')

#   - 결측치를 중앙값으로 변경 (상품 카테고리 별 고객 평점의 중앙값)
#     1) 상품 카테고리 별 고객 평점 중앙값 확인
rating_by_category = df.groupby('Product_Category')['Customer_Rating']
print('* === 상품 카테고리 별 고객 평점의 중앙값 === *')
print(rating_by_category.median())

#     2) 결측치를 중앙값으로 변경

def test_func(x):
  print('* ---------- test_func ---------- *')
  print(' * 현재 그룹 정보 :')
  print(x)
  print(f' * 그룹의 중앙값 : {x.median()}')
  print(x.fillna(x.median()))
  return x.fillna(x.median())
  print('* ------------------------------- *')
# print(df)
# rating_by_category.transform(test_func)

df['Customer_Rating'] = rating_by_category.transform(lambda x: x.fillna(x.median()))
print(f' * 처리 후 고객 평점 결측치 개수 : {df["Customer_Rating"].isnull().sum()}')
print(df["Customer_Rating"])

# * 판매 금액 (Sales_Amount) 컬럼의 결측치를 지역(Region)별 판매금액 평균으로 변경
df['Sales_Amount'] = df.groupby('Region')['Sales_Amount'].transform(lambda x: x.fillna(x.mean()))

print('* ------ 고객 평점, 판매 금액 컬럼의 결측치 처리 ------ *')
print(df[['Customer_Rating', 'Sales_Amount']].isnull().sum())

# * 판매 수량(Units_Sold) 컬럼의 결측치를 전체 데이터의 최빈값으로 변경
#   - 최빈값 : 가장 자주 나오는 값. mode()

print(f'판매 수량의 최빈값 : {df["Units_Sold"].mode()[0]}')
print(df["Units_Sold"].mode())
# => 최빈값의 경우 여러 개의 데이터가 결과로 표시되어, 값 자체를 사용할 때 첫번째 데이터를 선택!

# 판매 수량의 결측치를 최빈값으로 변경
df['Units_Sold'] = df['Units_Sold'].fillna(df['Units_Sold'].mode()[0])

print(f'판매 수량 컬럼의 결측치 개수 : {df["Units_Sold"].isnull().sum()}')
# ====================================================================
# * 이상치 (Outlier) 처리 *
#   : 데이터의 대부분의 분포에서 벗어난 극단적인 값을 처리하는 과정
#   : 상한선(Capping)을 설정하여 이상치를 찾아 대체

# * 판매금액 컬럼의 95% 분위수를 초과하는 값을 이상치로 판단하여
#   설정된 상한선의 값으로 대체

# 95% 분위수 => quantile(q%)
cap = df['Sales_Amount'].quantile(0.95)
print(f'판매 금액 컬럼의 95% 분위수 : {cap}')

# 판매 금액 데이터 중 상한선을 초과하는 값을 상한선 값으로 변경
# np.where(조건, 조건에해당될때사용할값, 조건에해당되지않을때사용할값)
print('* ---- 이상치 처리 전 ---- *')
print(df['Sales_Amount'])

df['Sales_Amount'] = np.where(df['Sales_Amount'] > cap, cap, df['Sales_Amount'])

print('* ---- 이상치 처리 후 ---- *')
print(df['Sales_Amount'])

# -----------------------------------

# * 컬럼 추가 : 기존 데이터를 활용하여 분석에 유의미한 새로운 변수 생성
#               => 특성 공학 (Feature Engineering)


# * 평균 판매 가격 계산 (Avg_Price)
#   평균 판매 가격 = 판매 금액 / 판매 수량
df['Avg_Price'] = df['Sales_Amount'] / df['Units_Sold']

print(df)

# * 매출 등급 생성 (Sales_Grade)
#   판매 금액이 전체 판매금액 평균보다 높으면 'High', 그렇지 않으면 'Low' 등급 부여
sales_mean = df['Sales_Amount'].mean() # 전체 판매금액 평균
df['Sales_Grade'] = np.where(df['Sales_Amount'] >= sales_mean, 'High', 'Low')
print(df)
# * ======================= 전처리 완료 ======================= *

# * 단순히 평균, 합계가 아닌 복합적인 통계 (그룹 별 비교, 정규화, 다차원 집계 등)를
#   사용하여 데이터의 숨겨진 패턴이나 관계를 파악하는 과정 => 심층 분석

# * 그룹별 복합 통계 *
#   agg : 그룹화된 데이터에 대해 여러 개의 집계 함수를 한 번에 적용하여 요약 통계를 생성하는 함수
#         groupby 결과에 대해 sum, mean, max, std 등 집계함수를 적용

# 카테고리 별 판매 금액 컬럼에 대한 다양한 요약 통계 
# - 총합, 평균, 최대값, 표준편차

category_stat = df.groupby('Product_Category')['Sales_Amount'].agg(
  Total_Sales='sum',
  Mean_Sales='mean',
  Max_Sales='max',
  Std_Sales='std'
).round(2)
# df.round(소수점_자리) : 해당 소숫점자리까지 반올림

# print(type(category_stat))
print(category_stat)

# * 그룹 내 비교 분석 *
#   transform : 그룹화된 데이터를 이용하되, 그 결과를 원래 데이터프레임 크기에 맞게 변환하여 새로운 컬럼을 생성
#               그룹 내 정규화나 그룹별 평균 대치 등에 활용

# * 지역 별 고객 평점 평균을 기준으로 개별 평점 차이  (Rating_Diff)
# * 지역별 고객 평점 평균
print( df.groupby('Region')['Customer_Rating'].agg('mean') )

#   개별 평점 - 지역 별 고객 평점 평균 => + / -
df['Rating_Diff'] = df.groupby('Region')['Customer_Rating'].transform(lambda x: x-x.mean()).round(2)

# 지역, 고객평점, 평균대비 평점 차이 출력
print( df[['Region', 'Customer_Rating', 'Rating_Diff']] )


# * 피벗 테이블
#   pivot_table(df, index=행분류기준컬럼, columns=열분류기준컬럼, values=집계대상값, aggfunc=적용할집계함수)

# - 카테고리 별 평균 금액 조회
pivot_ctg_mean = pd.pivot_table(df
               , index='Product_Category'
               , values='Sales_Amount'
               , aggfunc='mean')

print('* 카테고리 별 평균 금액 *')
print(pivot_ctg_mean)
print()

# - 카테고리별 프로모션 사용 여부에 대한 평균 금액 조회
pivot_mean = pd.pivot_table(df
               , index='Product_Category'
               , columns='Promotion_Used'
               , values='Sales_Amount'
               , aggfunc='mean')

print('* 카테고리 별 프로모션 사용 여부에 따른 평균 금액 *')
print(pivot_mean)
# => 피벗 테이블 : 복잡한 테이블 데이터를 2차원 교차 요약표 형태로 재구성하는 함수
#                  groupby와 agg를 조합한 것과 유사하지만, 가로/세로 축으로 펼쳐서 보여주는 특징을 가짐

# 카테고리 별 프로모션 사용 여부에 따른 평균금액, 평점평균 조회
last_pivot = pd.pivot_table(df
               , index='Product_Category'
               , columns='Promotion_Used'
               , values=['Sales_Amount', 'Customer_Rating']
               , aggfunc={'Sales_Amount': 'mean', 'Customer_Rating': 'mean'}
               , fill_value=0.0)

print('* 카테고리 별 프로모션 사용 여부에 따른 평균 금액/평점 비교 *')
print(last_pivot)

# 결측치 대체값 설정 : pivot_table(..., fill_value=대체값)
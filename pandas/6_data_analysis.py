# pandas/6_data_analysis.py
import pandas as pd

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
df['Customer_Rating'] = rating_by_category.transform(lambda x: x.fillna(x.median()))
print(f' * 처리 후 고객 평점 결측치 개수 : {df["Customer_Rating"].isnull().sum()}')
print(df["Customer_Rating"])
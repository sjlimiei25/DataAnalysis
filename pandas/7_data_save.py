# pandas/7_data_save.py
import pandas as pd

# 샘플 데이터
data = {
  'Region': ['East', 'West', 'East', 'North', 'West', 'East'],
  'Sales': [1500, 2200, 1800, 1000, 2500, 1600],
  'Expense': [300, 450, 350, 200, 500, 320]
}

# dict -> dataframe 변환
df = pd.DataFrame(data)

# Profit 컬럼 추가 : Sales - Expense
df['Profit'] = df['Sales'] - df['Expense']

# Region 별 Profit 합계 확인
print(df.groupby('Region')['Profit'].sum())

# reset_index() : 의미를 가지고 있는 인덱스를 제거하고 0부터 초기화
df_summary = df.groupby('Region')['Profit'].sum().reset_index()
# => 이전에 표시했던 인덱스는 새로운 컬럼으로 표시됨 (drop=False)

# rename() : 인덱스나 컬럼명을 변경할 때 사용
# * Profit -> Total_Profit 이름 변경
# df_summary.rename(columns={'Profit': 'Total_Profit'}, inplace=True)
df_summary = df_summary.rename(columns={'Profit': 'Total_Profit'})

print(df_summary)

# * CSV 저장
#     to_csv(파일명, index=인덱스행저장여부, encoding=인코딩정보)
#     - index : 일반적으로 False. 데이터프레임의 행 정보는 저장하지 않음
#     - encoding : 한글을 포함하는 경우 'utf-8' 또는 'euc-kr'로 설정 ('utf-8' => 표준)
#       * utf-8 (전세계모든언어/유니코드기반) vs euc-kr (한국어/국내용)
#     - sep : 구분자 설정. 기본값 콤마(,). 다른 값으로 구분하고자 할 때 설정

save_filepath = 'result.csv'
df_summary.to_csv(save_filepath, index=False, encoding='utf-8')
print(f'*** CSV 파일로 저장 완료 : {save_filepath} ***')

# * 저장한 파일을 다시 읽어서 확인
save_df = pd.read_csv(save_filepath)
print(save_df)
# ===========================================================

# * Excel 저장
#     to_excel(파일명, index=인덱스행저장여부, sheet_name=시트명)
#     - sheet_name : 저장될 시트 이름. 기본값: Sheet1
#     => 내부적으로 이미 유니코드 기반으로 문자를 저장하도록 설계되어 있음
save_excel_filepath = 'result.xlsx'
df_summary.to_excel(save_excel_filepath, index=False, sheet_name='Summary')
print(f'*** 엑셀파일로 저장 완료 : {save_excel_filepath}')
# ==> 엑셀 파일 저장 시 'openpyxl' 모듈 설치 필요
#     > pip install openpyxl
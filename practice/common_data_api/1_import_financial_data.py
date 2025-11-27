# practice/common_data_api/1_import_financial_data.py
import math
import time
import requests
import pandas as pd

# 환경 변수 관련 모듈 ----
import os
from dotenv import load_dotenv
#import dotenv
# > pip install python-dotenv
# ---------
load_dotenv()     # .env 파일 불러오기

# * 공공데이터 포털 사이트에서 발급받은 서비스 키(인증키)
SERVICE_KEY=os.environ.get('SERVICE_KEY')

# * BASE URL
BASE_SERVICE_URL='https://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2'
# * 재무상태표 조회 API 
API_PATH='getBs_V2'

REQUEST_URL = f'{BASE_SERVICE_URL}/{API_PATH}'
# print(REQUEST_URL)

# * API 연동 테스트 * ===================================================
# params = {
#   "numOfRows": "10",
#   "pageNo": "1",
#   "resultType": "json",
#   "serviceKey": SERVICE_KEY,
#   "crno": "1301110006246"     # 삼성전자 법인번호 - 전자공시시스템(Dart)에서 조회
# }
# response = requests.get(REQUEST_URL, params=params)
# data = response.json()
# # print(type(data))

# # 응답 데이터 추출
# items = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])

# # ---- 반복문 이용하여 출력
# for x in items:
#   print(x)
# ===================================================================

# * API 요청 후 수집된 데이터를 CSV 파일로 저장 =====================
def get_first_data():
  '''
    재무 상태표 API의 첫번째 페이지의 데이터 (item)와 
                      전체 건수(totalCount)를 반환해주는 함수
  '''
  params = {
    "numOfRows": "10",
    "pageNo": "1",
    "resultType": "json",
    "serviceKey": SERVICE_KEY,
    "crno": "1301110006246"     # 삼성전자 법인번호 - 전자공시시스템(Dart)에서 조회
  }

  response = requests.get(REQUEST_URL, params=params)
  # print(type(response), response)
  data = response.json()
  # print(type(data), data)
  response = data.get('response', {})
  # print(type(response), response)
  body = response.get('body', {})
  # print(type(body), body.keys(), body)

  totalCount = body.get('totalCount', 0)   # 전체건수
  # totalCount = data.get('response', {}).get('body', {}).get('totalCount', 0)
  items = body.get('items', {}).get('item', []) # 조회한 데이터 목록
  # print(type(items), items[0])
  if data:
    return items, totalCount
  else:
    return [], 0
'''
data_list, totalCount = get_first_data()
# print(len(data_list), totalCount)
if totalCount > 0:
  # CSV 파일로 저장 : financial_ss.csv
  df = pd.DataFrame(data_list)
  df.to_csv('financial_ss.csv', encoding='utf-8')
  print("* --- 파일 저장 완료 --- *")
'''
# numOfRows : 10 , totalCount : 172 --> math.ceil(totalCount / numOfRows) 올림처리!! -> 전체 페이지 수: 18
# numOfRows : 100, totalCount : 172 --> 전체 페이지 수 : 2
# 
# 전체 데이터를 수집하여 csv 파일로 저장 -> financial_ss.csv
def get_params(page_no, num_of_rows):
  """
  get_params의 Docstring
  API 요청에 필요한 매개변수(Query Parameters)를 반환해주는 함수
  
  :param page_no: 페이지 번호
  :param num_of_rows: 한 페이지 당 데이터 개수
  """
  return {
    "numOfRows": str(num_of_rows),
    "pageNo": str(page_no),
    "resultType": "json",
    "serviceKey": SERVICE_KEY,
    "crno": "1301110006246"     # 삼성전자 법인번호
  }

def get_all_data():
  """
  get_all_data의 Docstring
  전체 데이터를 수집하여 리스트 형태로 반환해주는 함수
  """
  all_data = []     # 전체 데이터를 저장할 변수(리스트)
  data_size = 30    # 한 번에 요청할 데이터 개수(numOfRows)

  print(f'* --- {data_size} 건씩 요청 --- *')

  # 첫 요청 -> 페이지 번호: 1, 요청 데이터 개수: data_size
  params = get_params(1, data_size)

  # API로 요청
  response = requests.get(REQUEST_URL, params=params)
  data = response.json()

  # 응답 데이터에서 (totalCount' - 전체 데이터 개수, 'item' - 현재 요청한 데이터 목록) 추출

  body = data.get('response', {}).get('body', {})
  total_count = body.get('totalCount', 0)
  items = body.get('items', {}).get('item', [])

  #all_data += items    # [] + [....]
  all_data.extend(items) # => [....]
  print(f'* --- 전체 데이터 개수 : {total_count}')

  # 전체 페이지 수 계산
  #  => (전체_데이터_개수 / 요청할_데이터_수) 올림처리
  #     math.ceil(total_count / data_size)
  total_pages = math.ceil(total_count/data_size)
  print(f'* --- 요청할 전체 페이지 수 : {total_pages}')

  # 2 페이지부터 마지막 페이지(total_pages)까지 요청
  # => 반복문 사용 
  #    [2,3,...,total_pages] -> range(2, total_pages+1)
  for page_no in range(2, total_pages+1):
    print(f'* ---- {page_no}/{total_pages} 요청 시작 ---- *')

    # 요청 데이터 (parameters)
    params = get_params(page_no, data_size)

    time.sleep(1)   # 1초 지연 => 서버 부하 방지

    # API로 요청
    response = requests.get(REQUEST_URL, params=params)
    data = response.json()

    # 응답 데이터 목록('item') 추출
    items = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])
    all_data.extend(items)

  return all_data

# 삼성전자 재무정보 조회 후 CSV 파일로 저장 (financial_ss.csv)
ss_data = get_all_data() # [......]
df = pd.DataFrame(ss_data)

file_name = 'financial_ss.csv'
df.to_csv(file_name, encoding='utf-8')
print('* --- 데이터 수집 및 CSV 저장 완료 --- *')
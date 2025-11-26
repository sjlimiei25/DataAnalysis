# practice/x_api/x_api_test.py

# * 사전 작업 *
#   X 개발자 플랫폼에 회원 가입하여 API 키 발급

# * ========== 주의사항! 아래 정보는 github, cloud에 올리지 말것!! ================= *
# CONSUMER API KEY
CONSUMER_KEY='X 개발자 플랫폼에서 발급받은 CONSUMER KEY'
CONSUMER_SECRET='X 개발자 플랫폼에서 발급받은 CONSUMER SECRET'

# ACCESS TOKEN
ACCESS_TOKEN='X 개발자 플랫폼에서 발급받은 ACCESS TOKEN'
ACCESS_SECRET='X 개발자 플랫폼에서 발급받은 ACCESS TOKEN SECRET'

# BEARER TOKEN
BEARER_TOKEN='X 개발자 플랫폼에서 발급받은 BEARER TOKEN'
# * ============================================ *

# * tweepy 라이브러리(모듈)
#   > pip install tweepy
import tweepy

# Client 객체 -> 기능(API)을 함수호출 방식으로 연동
def get_client_v1():
  return tweepy.Client(consumer_key=CONSUMER_KEY
                , consumer_secret=CONSUMER_SECRET
                , access_token=ACCESS_TOKEN
                , access_token_secret=ACCESS_SECRET)

# * 인증 계정 정보 조회 : get_me()
def get_user(client):
  response = client.get_me()
  print(response)
  username = response.data['username']
  print(f'인증 성공: 계정명 - {username}')

# * 트윗 (작성) : create_tweet()
def create_tweet(client):
  response = client.create_tweet(text='오늘은 수요일.. 참.. 좋다...')
  print(response)

'''
# 계정 조회, 트윗 작성 테스트
client = get_client_v1()
get_user(client)
create_tweet(client)
'''
# ====================================================================

# Client 객체 생성 (Bearer token)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# * 최근 트윗(post) 검색 => search_recent_tweets()
keyword = '파이썬'
option = ' -is:retweet lang:ko'   # 리트윗 제외, 한국어
response = client.search_recent_tweets(query=keyword+option, max_results=10)
print(response) # => response.data 반복문....
# numpy/random.py
'''
    난수(랜덤값), 분포 생성

    - np.random.seed  : 난수 시드 설정
    - np.random.randint : 정수 난수 생성
    - np.random.normal : 실수 난수 생성
    - np.random.rand/randn : 0 ~ 1 사이 난수 생성
'''
import numpy as np

def set_seed():
  '''
      시드 설정 ? 시드를 고정하면 이후에 코드를 실행해도 동일한 난수가 생성됨
      => 재현성 확보를 위함
  '''
  np.random.seed(42)


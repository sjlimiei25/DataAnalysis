# 9_DataAnalysis/1_basic.py

import numpy as np

# 0차원 배열 생성 -> 스칼라(Scalar). 축(Axis)이 없는 배열
def zero_dimension_arr():
  # 연산 일관성 유지, 브로드 캐스팅, 내부 처리 구조를 통일하기 위해 NumPy에서는 스칼라도 배열로 취급

  arr = np.array(55)

  print(arr)
  print(type(arr))
  print(arr.ndim)   # 차원수
  print(arr.shape)  # 배열 형태

  # print(arr[0])   # 인덱싱 불가! IndexError 발생..

# zero_dimension_arr()

# 1차원 배열 생성 -> 벡터(Vector). 축이 1개.
def one_dimension_arr():
  arr = np.array([1,2,3,4,5])

  print(arr)
  print(type(arr))

  print(arr.ndim)  # 차원수
  print(arr.shape) # 배열 형태

  # 0으로 채워진 배열 생성 : np.zeros(개수)
  # 0이 5개 들어있는 배열 생성
  zeros_arr = np.zeros(5)
  print(zeros_arr)
  print(zeros_arr.dtype)     # 요소의 데이터타입

  # 1로 채워진 배열 생성 : np.ones(개수)
  # 1이 10개 채워져있는 배열 생성
  ones_arr = np.ones(10)
  print(ones_arr)
  print(ones_arr.dtype)

  # 특정 범위 내의 숫자로 채워진 배열 생성
  # : np.arange(시작값, 끝값, 증가값)
  # 0 ~ 9까지 숫자가 담긴 배열을 생성
  range_arr = np.arange(0, 10, 1)
  print(range_arr)
  print(range_arr.dtype)

# one_dimension_arr()

# 2차원 배열 생성 -> 행렬(Matrix). 축 2개 (Axis 0: 행, 1: 열)
def two_dimension_arr():
  arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
  ])

  print(arr)
  print(type(arr))
  print(arr.ndim)
  print(arr.shape)

  # 0으로 채워진 배열 생성 => 3x4. np.zeros((행,열))
  zeros_arr = np.zeros((3,4))
  print(zeros_arr)
  print(zeros_arr.dtype)

  # 1로 채워진 배열 생성 => 2x2. np.ones((행,열))
  ones_arr = np.ones((2,2))
  print(ones_arr)
  print(ones_arr.dtype)

  # 1 ~ 9로 채워진 배열 생성. 3x3.
  # 1D -> 2D
  range_arr = np.arange(1, 10).reshape(3,3)
  print(range_arr)

# two_dimension_arr()

# 3차원 배열 생성 -> 텐서 (Tensor). 축이 3개 (Axis 0:깊이-면, 1: 행, 2: 열)
def three_dimension_arr():
  arr = np.array([
    [
      [1,2,3],
      [4,5,6]
    ],
    [
      [7,8,9],
      [10,11,12]
    ]
  ])

  print(arr)
  print(type(arr))

  print(arr.ndim)
  print(arr.shape)   # (2,2,3) -> 2개의 면, 2개의 행, 3개의 열

  # 0으로 채워서 배열 생성 : np.zeros((면,행,열))
  zeros_arr = np.zeros((2,3,4))
  print(zeros_arr)

  # 1로 채워서 배열 생성 : np.ones((면, 행, 열))
  ones_arr = np.ones((1, 2, 3))
  '''
    [[[1,1,1],[1,1,1]]]
  '''
  print(ones_arr)

three_dimension_arr()
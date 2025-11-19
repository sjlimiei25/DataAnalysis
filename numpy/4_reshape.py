'''
    reshape()
    - 배열 형태(차원, 가로/세로)를 원하는 형태로 바꿔주는 함수 (재배치)
    - 배열 요소의 총 개수는 유지해야 함! (절대 변하면 안됨)
    - 한 축의 크기를 자동 계산하고자 할 경우 -1 사용 (단, -1은 한 번만 사용 가능)
'''
import numpy as np

def reshape_1d_to_2d():
  # 0 ~ 11 까지 데이터를 담은 1차원 배열 생성
  arr = np.arange(12)
  print(arr)

  # 3x4 형태로 변경
  arr_2d_3x4 = arr.reshape(3,4)
  print(arr_2d_3x4)

  # 2x6 형태로 변경
  arr_2d_2x6 = arr.reshape(2, 6)
  print(arr_2d_2x6)

  # 3개씩 묶어서 행은 자동 계산 -> -1
  arr_2d_auto = arr.reshape(-1, 3)
  print(arr_2d_auto)

  # 2개의 행에 데이터는 자동 계산
  arr_2d_auto = arr.reshape(2, -1)
  print(arr_2d_auto)

  # arr.reshape(-1, -1) # => -1을 한번만 작성!

# reshape_1d_to_2d()

def reshape_2d_to_3d():
  arr = np.arange(12).reshape(3,4)
  print(arr)

  # 2x2x3 형태로 변경
  arr_3d = arr.reshape(2,2,3)
  print(arr_3d)

  # 1x6x2 형태로 변경
  arr_3d = arr.reshape(1,6,2)
  print(arr_3d)


  # auto(-1)  적용
  arr_3d = arr.reshape(3, 2, -1)
  print(arr_3d)

  # arr_3d = arr.reshape(3, -1, -1)

# reshape_2d_to_3d()

def reshape_to_1d():
  arr = np.arange(12).reshape(3, 4)
  print(arr)

  arr_1d = arr.reshape(-1)
  print(arr_1d)

  arr_3d = arr.reshape(3,2,2)
  print(arr_3d)

  arr_1d = arr_3d.reshape(-1)
  print(arr_1d)
  # => reshape(-1) : 1차원 배열로 변경
  print('-'*30)

  # * flatten() : 1차원 배열로 변경. 복사본을 반환.
  arr_flat = arr_3d.flatten()
  print(arr_flat)

  # * ravel() : 1차원 배열로 변경. 뷰를 반환
  arr_ravel = arr_3d.ravel()
  print(arr_ravel)

# reshape_to_1d()

def copy_and_view():
  # 원본 배열
  origin_arr = np.arange(6)

  print(f'origin array : {origin_arr}')

  print('* ------ ravel ------ *')
  ravel_arr = origin_arr.ravel()
  print(f'ravel array : {ravel_arr}')

  ravel_arr[0] = 999

  print(f'ravel array: {ravel_arr}')
  print(f'origin array: {origin_arr}')
  # => 원본 배열의 데이터도 변경됨. 메모리 공유.

  print('-'*30)

  origin_arr[0] = 0 # 초기화

  print('* ------ flatten ------ *')
  flat_arr = origin_arr.flatten()
  print(f'flatten array : {flat_arr}')

  flat_arr[0] = 666

  print(f'flatten array : {flat_arr}')
  print(f'origin array : {origin_arr}')
  # => 원본 배열의 데이터가 유지됨. flatten -> 새로운 배열을 반환

  print('* ------ reshape ------ *')
  reshape_arr = origin_arr.reshape(2, -1)
  print(f'reshape array : {reshape_arr}')

  # 데이터 0(0,0)을 다른 값으로 변경
  reshape_arr[0,0] = 444

  print(f'reshape array: {reshape_arr}')
  print(f'origin array: {origin_arr}')
  # => 원본 배열도 변경됨. 메모리 공유.

  """
          뷰(ravel, reshape)            복사(flatten)

  메모리  원본과 공유(하나의 데이터)    새로운 메모리 공간에 복제(두 개의 독립된 데이터)
  수정    뷰를 수정하면 원본도 변경됨   복사본을 수정해도 원본은 그대로 유지
  속도    빠름 (복사 과정이 불필요)     상대적으로 느림(복사 과정 필요)
  """

copy_and_view()
'''
1. 문제설명
N개 원소의 수열이 오름차순으로 정렬
이 수열에서 x가 등장하는 횟수 계산

2. 알고리즘
시간복잡도 logN -> 이진 탐색

3. 구현
1)입력
  원소의 갯수(N), 횟수를 구하고자 하는 특정 수(x)를 받는다.
  수열을 리스트로 입력받는다.
2)x가 처음 등장하는 index와 
  x가 마지막으로 등장하는 index를 구하기
  그 인덱스의 차이를 계산하기
3)첫 위치를 찾는 이진탐색 함수 구현
4)마지막 위치를 찾는 이진탐색 함수 구현

4. 느낀점
1) 첫 위치와 마지막 위치 같이 찾는 것이 아니라,
이진 탐색 함수 2개를 각각 실행한 뒤 답을 도출하는 관점을 얻었다.
2) 파이썬의 이진 탐색 라이브러리 bisect을 적절히 활용하면 손쉽게 문제 해결할 수 있다.

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split())) # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
'''

def count_num(arr, x):
  n = len(arr)

  # 첫 위치를 찾는 이진탐색함수
  first_index = first_found(arr, x, 0, n-1)

  # 마지막 위치를 찾는 이진탐색함수
  last_index = last_found(arr, x, 0, n-1)

  count = last_index - first_index + 1
  return count

def first_found(arr, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
  if(mid == 0 or target > arr[mid-1]) and arr[mid] == target :
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인 
  elif arr[mid] >= target :
    return first_found(arr, target, start, mid-1)
  # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else :
    return first_found(arr, target, mid+1, end)

def last_found(arr, target, start, end):
  if start > end:
    return None
  

  mid = (start + end) // 2
# 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
  if(mid == n-1 or target < arr[mid+1]) and arr[mid] == target :
    return mid
  elif arr[mid] > target :
    return last_found(arr, target, start, mid-1)
  else :
    return last_found(arr, target, mid+1, end)


n, x = map(int, input().split())
arr = list(int, input().split())

count = count_num(arr, x)

if count == 0:
  print(-1)
else :
  print(count)

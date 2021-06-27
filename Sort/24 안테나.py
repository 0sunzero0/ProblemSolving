'''
1. 문제 설명
일직선 상의 마을에 여러 채의 집이 위치해 있다. 
효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되는 위치에 설치하려고 한다. 
이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택
1) 입력
- 집의 수 N
- 집에 위치
2) 출력
- 안테나를 설치할 위치의 값을 출력(여러 개의 값이 도출될 경우 가장 작은 값을 출력)

2. 어떤 알고리즘인지
- 정렬 사용하여, cost가 적은 순으로 정렬 
- cost 가장 적은 순 선택

3. 어떻게 코드를 짰는지 (나의 풀이)
1) 수, 위치 입력 받기 (element 접근 쉽게 하기위해 리스트로)
2) cost 계산해서 위치 안에 리스트로 받기
- cost 계산 : 반복문 사용 += (해당 위치 - 나머지 위치) 계산하기
3) cost 비교해서 정렬
4) 가장 적은 cost의 위치값 출력

4. 다른 사람의 풀이
안테나 가운데 위치에 있는 것이 가장 cost가 적다.
-> 1) sort 해서 2) 가운데 값을 가져오자.
가운데 값을 가져올 때, 몫을 가져오면 된다. 홀수 가운데 값 가져오고 짝수도 가운데 값 중 작은 값을 가져온다.

5. 느낀점  
cost 계산할 때, 안테나가 가운데 있는 것이 가장 cost가 적다.
-> 코딩테스트는 문제 접근 : 간단하게, 간결하게 하는 것이다.
-> 경우를 다 따지는 것만 답이 되는 것이 아니다. 경우 다 따지는 것 외에 효율적인 답이 있다.
'''

N = int(input())
position_list = list(map(int,input().split()))
position_list.sort()
print(positoin_list[(n-1)//2])

'''
cost_list = []
for i in range(0, N):
  cost = 0
  for j in range(0, N):
    if(i != j):
      cost += abs(position_list[i]- position_list[j])
  cost_list.append(cost)

total_list = []
for i in range(0, N):
  total_list.append([position_list[i], cost_list[i]])

total_list = sorted(total_list, key = lambda x : (x[1], x[0]))
print(total_list[0][0])
'''

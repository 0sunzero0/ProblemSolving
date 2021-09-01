class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)
        '''
        # 3. Counter
        freqs = collections.Counter(stones)
        count = 0
        for char in jewels:
            count += freqs[char]
        # Counter, 각 개수를 계산을 자동으로 해주기에 코드를 더욱 짧게 할 수 있음
        '''
        '''
        #2. default를 이용한 비교 생략
        freqs = collections.defaultdict(int)
        count = 0
        
        for char in stones:
            freqs[char] += 1
        
        for char in jewels:
            count += freqs[char]
        # defaultdict를 이용할 경우, 키가 존재하는지 여부를 판별할 필요가 없다. -> 코드수 감소
        '''
        '''
        #1. 해시테이블을 이용한 풀이
        freqs = {}
        count = 0
        
        # 돌(S)의 빈도수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
                
        # 보석(J)의 빈도수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        '''
        
        #return count
        

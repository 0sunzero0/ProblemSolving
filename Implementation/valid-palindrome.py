class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 3. 슬라이싱 사용
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] # 슬라이싱    
        '''
        대부분 문자열 작업은 슬라이싱으로 처리하는 편이 가장 빠르다.
        슬라이싱의 빠른 속도를 잘 보여준다.
        
        s[:] 사본을 리턴한다. 문자열이나 리스트를 복사
        s[::1] 뒤집는다.
        s[::2] 2칸씩 앞으로 이동한다.
        '''
        '''
        # 1. 리스트로 변환
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
        ''' 
        '''
        # 2. 데크 자료형을 이용한 최적화
        strs: deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
        '''

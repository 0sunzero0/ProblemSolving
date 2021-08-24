class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''
        # 1. 투 포인터를 이용한 스왑
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        '''
        # 2. pythonic
        s.reverse()
        

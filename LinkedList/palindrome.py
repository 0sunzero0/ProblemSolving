# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 2. 데크를 이용한 최적화
        q: Deque = collections.deque()
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

        '''
        1. 리스트 변환
        q:List = []
        
        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # 팰린드롬 판별 
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
        '''
        

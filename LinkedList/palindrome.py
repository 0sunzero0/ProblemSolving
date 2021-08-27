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
        
        '''
        느낀점:
        list는 q.pop() 값을 꺼내오면 모든 값이 한칸씩 시프팅이 되어 시간복잡도 O(n)을 발생
        최적화 -> Python의 deque는 이중 연결리스트 구조로 양쪽 방향 모두 추출하는데 시간 복잡도 O(1)에 실행된다.
        '''

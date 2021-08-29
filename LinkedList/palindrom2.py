# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        
        # runner를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast :
            slow = slow.next
            
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

   '''
    1. runner 기법
        연결리스트를 순회할 때 2개의 포인터를 동시 사용하는 기법
        빠른 런너가 연결리스트의 끝에 도달하면 느린 런너는 정확히 연결리스트가 중간 지점을 가리키게 된다.
        이 같은 방식으로 중간 위치르 찾아내면, 여기서부터 값을 비교하거나 뒤집기를 시도하는 드 여러모로 활용할 수 있다. 
    2. 다중 할당
   '''

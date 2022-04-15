# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#LC Easy https://leetcode.com/problems/reverse-linked-list/submissions/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #concept is to go through list and convert next pointers to prevous pointers
        #1->2->3->4->5 = 1<-2<-3<-4<-5 and then returning it from its last value as if its head 
        prev = None
        curr = head
        while curr:
            currNext = curr.next #saving next elem reference 
            curr.next = prev #set node pointer next to previous, first one will be null () 
            prev = curr 
            curr = currNext #using saved elem reference
        
        return prev

        
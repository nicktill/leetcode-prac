# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#LC Easy https://leetcode.com/problems/reverse-linked-list/submissions/
# concept is to go through list and convert next pointers to prevous pointers
#ie, 1 -> 2 -> 3 -> 4 -> 5 would = 1 <- 2 <- 3 <- 4 <- 5 and then return it from last node
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            currNext = curr.next #saving next elem reference 
            curr.next = prev #set node pointer next to previous, by doing this to every node we reverse the list 
            prev = curr #update prev to next list elem, 
            curr = currNext #using saved elem reference

        
        return prev

        
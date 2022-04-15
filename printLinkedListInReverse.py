#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

#https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
#LC MED
class Solution(object):
    def printLinkedListInReverse(self, head):
        reverseList = []
        while head:
            reverseList.insert(0, head) #we can consistently add to front of list using insert
            head = head.getNext() 
        
        for nums in reverseList: #simplly iterate through list and print
            nums.printValue()

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
      List<Integer> nums = new ArrayList<>(); 
        
        ListNode curr = head; 
        
        while (curr != null) {
            nums.add(curr.val);
            curr = curr.next; 
        }
          
        int start = 0; 
        int end = nums.size() -1; 
        while(start < end) 
        {
            
            if (!nums.get(start).equals(nums.get(end))) 
            {
                   return false; 
            }
            
            start++; 
            end--; 
        }
    return true; 
        
    }

    
};

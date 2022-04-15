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

// LC Easy, https://leetcode.com/problems/reverse-linked-list/solution/
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode prev = null; 
        while(curr != null){ 
                ListNode nextTemp = curr.next; //save next node to elem
                //we dont have access to prev pointer, so we set next to point to prev variable
                curr.next = prev; //make next point to previous element
                prev = curr; //make previous element update to current element
                curr = nextTemp; //update current element to next elem

            }
        return prev;
        }
        
        
    }
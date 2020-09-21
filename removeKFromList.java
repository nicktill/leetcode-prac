//Nicholas Tillmann, CodeSignal Submission
// RemoveKFromList.java

//Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

ListNode<Integer> removeKFromList(ListNode<Integer> l, int k) {
    
    if(l == null) {
        return l;
    }
    while (l != null && l.value == k) {
        l = l.next; 
    }
    
    ListNode<Integer> temp = l; 
    while ( temp != null && temp.next != null) {
        if (temp.next.value == k) {
            temp.next = temp.next.next;
            
        } else {
            temp = temp.next;
        }
    }
    
    return l;
    
}




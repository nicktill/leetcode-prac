import java.util*;

public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    int length = 0;
    
    ListNode first = head;
    while(first != null){
        length++; 
        first = first.next; 
    }
    length-=n; 
    first = dummy;
    while( length > 0){
        length--;
        first = first.next; 
    }
    //at this point you are at the node before one to remove
    first.next = first.next.next; //change the node to remove with the next position
    return dummy.next; //then return list normally
}
public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
      
        var dummy = new ListNode(12);
        dummy.next = head;
        var p = dummy;
        
        while(p.next !=null){
            if(p.next.val == val){
                p.next = p.next.next;
            }
            else{
                p= p.next;
            }
        }
        
        return dummy.next;
    }
}

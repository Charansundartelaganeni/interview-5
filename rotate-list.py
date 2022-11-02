#TC: O(n)
#SC: O(1)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 


        if head == None:  #while thereis no node, return none
            return None 

        if head.next == None: #if there's no next node for head, then also return 1
            return head 

        #length 

        length = 0  
        curr1 = head

        while curr1:  #traverse until there's curr1 node

            curr1 = curr1.next  #increase Curr1
            length+=1  #length will also increase

        if k > length:  #if k is greater than the length, then the operations will be repeated, inorder to avoid that, we can take modulo answer as k

            k = k%length 

        newhead = head
        while k>0:  #now traverse through the linked list and rotate it to the point where it needs to be repeated
            prev = newhead 
            curr = newhead.next 

            while prev.next.next != None: 

                prev = prev.next 
                curr = curr.next 

            curr.next = newhead  
            newhead = curr
            prev.next = None 
            k-=1 
        return newhead 
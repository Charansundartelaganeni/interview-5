#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.findMid(head)    #Initialize mid to the output given by the function findMid
        midNext = mid.next  #Initialize midNext as mid.next
        mid.next = None #Initialize mid.next to None
        rev = self.reverse(midNext) #Initialize rev to the output given by the function reverse
        
        while rev:  #Continue till rev
            if head.val == rev.val: #If the head value is euqal to rev value
                head = head.next    #Change head to head.next
                rev = rev.next  #Change rev to rev.next
            else:
                return False    #Else return False
        return True #Return True
        
    def findMid(self,head): #findMid function
        slow = head #Initialize slow to head
        fast = head #Initialize fast ro head
        while fast.next!= None and fast.next.next != None:  #Continue till fast.next and fast.next.next is not equal to None
            slow = slow.next    #Change slow to slow.next
            fast = fast.next.next   #Change fast to fast.next.next
        return slow #Return slow which gives the mid point of linked list

    def reverse(self,head): #reverse Function
        prev = None #Initailze pre =v as None
        curr = head #Initialize curr as head
        while curr: #Continue till curr is None
            temp = curr.next    #Initialize temp to curr.next
            curr.next = prev    #Initialize curr to prev
            prev = curr #Initiallize prev to curr
            curr = temp #Initialize curr to temp
        return prev #Return prev which return the reversed linked list
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        pointer1 = l1
        pointer2 = l2
        string1 = str(l1.val)
        string2 = str(l2.val)
        list_to_return = ListNode()
        result_pointer = list_to_return  # Initialize a pointer for the result linked list

        # Extract values from l1 and l2
        while pointer1.next is not None:
            string1 = str(pointer1.next.val) + string1
            pointer1 = pointer1.next
        while pointer2.next is not None:
            string2 = str(pointer2.next.val) + string2
            pointer2 = pointer2.next

        # Calculate the sum
        total_sum = int(string1) + int(string2)

        # Create the result linked list
        while total_sum != 0:
            digit = total_sum % 10
            total_sum = total_sum // 10
            result_pointer.val = digit
            if total_sum != 0:
                result_pointer.next = ListNode()  # Create a new node if there are more digits
                result_pointer = result_pointer.next

        return list_to_return

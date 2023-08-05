class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycleStart(head):
    slow = head
    fast = head

    # Step 1: Detect cycle using Floyd's Cycle Detection Algorithm
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    # Step 2: Find the starting node of the cycle
    if has_cycle:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # The starting node of the cycle
    else:
        return None  # No cycle in the linked list

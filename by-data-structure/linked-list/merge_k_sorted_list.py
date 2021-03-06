'''
Prob: Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Approach 1 : Traverse all linked list and store all vlaues in arrray, sort the array and generate soted LinkedList

# Time : O(N log N)
# Space: O(N) where N is number of nodes

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes = []
        
        for list in lists:
            while list:
                nodes.append(list.val)
                list = list.next
        
        start = head = ListNode(0)
        for node in sorted(nodes):
            new_node = ListNode(node)
            head.next = new_node
            head = head.next
        
        return start.next
        
# Approach 2:
# Time - O(N log K) k is number of list
# Space - O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for idx, list in enumerate(lists):
            if list:
                heap.append((list.val, idx))
        
        heapq.heapify(heap)
        
        curr = head = ListNode(None)
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(heap, (node.val, idx))
        return head.next
                
        

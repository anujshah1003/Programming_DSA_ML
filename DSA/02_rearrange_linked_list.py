# -*- coding: utf-8 -*-
'''
this is a problem from daily coding interview - https://www.dailycodingproblem.com/
I recived this question as I have subscribed for recieveing mail

Given a linked list of numbers and a pivot k, partition the linked list so 
that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, 
the solution could be 1 -> 0 -> 5 -> 8 -> 3.

'''

# let's first create a linked list
class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

def traverse(head):
    while head is not None:
        print(head.value, end=' ')
        head=head.next
    
def insert(head,value):
    if head==None:
        return Node(value)
    current_node=head
    while current_node.next is not None:
        current_node=current_node.next
    current_node.next=Node(value)
    return head
head=insert(None,5)
head=insert(head,1)
head=insert(head,8)
head=insert(head,0)
head=insert(head,3)
traverse(head)
#%%
# 5 1 0 8 3
#Time Complexity - O(N)+O(N) =O(2N) ~ O(N)
# Space Complexity - O(1)
def rearranage_linked_list(head,k):
    # first loop once to find the length of the linked list and also to mark 
    # the tail node
    length_ll=0
    current_node=head
    while current_node.next is not None:
        current_node=current_node.next
        length_ll+=1
    # for the last node
    length_ll+=1
    tail_node=current_node
    
    # lets rearrange the linked list
    current_node=head
    prev_node=None
    for i in range(length_ll):
        if current_node.value<k: # when value is less than k
            prev_node=current_node
            current_node=current_node.next
        else: #
            next_node=current_node.next
            # deleting an element from middle
            if prev_node:  # or if current_node==head_node 
                current_node.next=None
                tail_node.next=current_node
                tail_node=current_node
                prev_node.next=next_node
                current_node=next_node
            # deleting an element from head
            else:
                current_node.next=None
                tail_node.next=current_node
                tail_node=current_node
                current_node=next_node
                head=current_node
    return head
#%%
# test the code
head=insert(None,5)
head=insert(head,1)
head=insert(head,8)
head=insert(head,0)
head=insert(head,3)
print('before rearranging')
traverse(head)
rearranged_ll=rearranage_linked_list(head,3)
print('\nafter rearranging')
traverse(rearranged_ll)

head=insert(None,5)
head=insert(head,1)
head=insert(head,8)
head=insert(head,0)
head=insert(head,3)
print('\nbefore rearranging')
traverse(head)
rearranged_ll=rearranage_linked_list(head,5)
print('\nafter rearranging')
traverse(rearranged_ll)


    
    
    
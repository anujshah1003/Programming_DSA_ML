'''
This question was asked by the daily coding problem
“Given a singly linked list and an integer k, remove 
the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is 
prohibitively expensive.

Do this in constant space and in one pass.”

'''

class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

def get_linked_list():	
	a=Node(1)
	b=Node(2)
	c=Node(3)
	d=Node(4)
	e=Node(5)
	f=Node(6)

	a.next=b
	b.next=c
	c.next=d
	d.next=e
	e.next=f
	return a

def traverse_linked_list(head):
	while head is not None:
		print(head.value)
		head=head.next
head=get_linked_list()		
traverse_linked_list(head)
# solution -1: compute the length of the linked list and then delete the length-k+1 th node from beginning
#####
# yet to do
#####
# solutiom-2: keep two pointers the main and the refernce, both being assigned the head node in the beginning
# move the refernce pointer k times. then move both the refernce and the main pointers one step at a time. when the 
# reference reaches the end the main will be at the kth position from the end
def remove_kth_from_end(head,k):
    if head.next==None and k==1:
        return []
		
    prev_node=None
    ref_node=head
    kth_node=head
	
    for i in range(k):
        ref_node=ref_node.next
		
    while ref_node is not None:
        ref_node=ref_node.next
        next_node=kth_node.next
        prev_node=kth_node
        kth_node=next_node
		
    if kth_node==head:
        next_node=kth_node.next
        kth_node.next=None
        head=next_node
    elif kth_node.next is None:
        prev_node.next=None
    else:
        next_node=kth_node.next
        kth_node.next=None
        prev_node.next=next_node
		
    return head

head=get_linked_list()
head=remove_kth_from_end(head,2)
traverse_linked_list(head)	

head=get_linked_list()
head=remove_kth_from_end(head,4)
traverse_linked_list(head)	
		
head=get_linked_list()
head=remove_kth_from_end(head,6)
traverse_linked_list(head)	
		
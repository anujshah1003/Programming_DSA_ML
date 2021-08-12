
'''
this is a problem from daily coding interview - https://www.dailycodingproblem.com/
I received this question as I have subscribed for recieveing mail

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].

'''

# since we need to print the childrens at every level first we need to do breadth first traversal
# we can use a queue to keep track of the all the childrens that need to be visited next

# let's first create a linked list
# let's assume we are going to construct a complete binary tree here

class Node:
	def __init__(self,val):
		self.value=val
		self.left=None
		self.right=None
		
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
g=Node(7)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g

#breadth first traversal
def traverse(root):
	queue=[]
	queue.append(root)
	while len(queue):
		current_node = queue.pop(0)
		print(current_node.value)
		if current_node.left:
			queue.append(current_node.left)
		if current_node.right:
			queue.append(current_node.right)

	
traverse(a)
# time complexity = O(N) N- number of nodes assuming that reverse is constant operation
# space complexity - at any moment the queue as well as current childern will have the leave nodes at every level
# worst case is in complete binary tree where the last level is comletely filled and teh last level conatins nearly
# half of the toatl nodes
# so worst case space comlexity - O(N/2)+O(N/2) ~ O(N)
def boustrophedon_order(root):
	final_list=[]
	queue=[]
	queue.append(root)
	num_child=1
	current_children=[]
	mode=1
	while len(queue):
		current_node=queue.pop(0)
		current_children.append(current_node.value)
		if current_node.left:
			queue.append(current_node.left)
		if current_node.right:
			queue.append(current_node.right)
		num_child-=1
		#print(current_children,num_child)
		
		if num_child==0:
			if mode==1:
				final_list.extend(current_children)
				mode=-1
			elif mode==-1:
				final_list.extend(current_children[::-1])
				mode=1	
			num_child=len(queue)
			current_children=[]
			
	return final_list
result=boustrophedon_order(a)
print(result)
		
		

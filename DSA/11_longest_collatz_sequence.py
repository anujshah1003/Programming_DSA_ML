'''
which starting number below a given number n produce teh longest collatz sequence
https://www.mathblog.dk/project-euler-14/
https://www.geeksforgeeks.org/maximum-sequence-length-collatz-conjecture/
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

 

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

def compute_collatz_seq(n):
	num_steps=0
	while n!=1:
		if n%2==0:
			n=n/2
		else:
			n=3*n+1
		num_steps+=1
	return num_steps
	
	
# to find the starting number that gives longest sequence compute the num_setps for every number

def get_starting_num_for_longest_sequence(n):
	starting_num=1
	longest_seq_len=0
	for i in range(2,n):
		num_steps=compute_collatz_seq(i)
		if num_steps>longest_seq_len:
			longest_seq_len=num_steps
			starting_num=i
			
	return starting_num,longest_seq_len
for i in range(1,21):
	starting_num,longest_seq_len=get_starting_num_for_longest_sequence(i)
	print(i,starting_num,longest_seq_len)	

print('--------------')		

# what if we use dynamic programming and store the num of seq of prev observed values we can solve it recursively
dp={}
dp[1]=0

def compute_collatz_length_rec(n):
	
	if n==1:
		return 0
	if n in dp:
		return dp[n]
	if n%2==0:
		return 1+compute_collatz_length_rec(n/2)
	else:
		return 1+compute_collatz_length_rec(3*n+1)
def get_starting_num_for_longest_sequence_dp(n):
	starting_num=1
	longest_seq_len=0
	for i in range(2,n):
		num_steps=compute_collatz_length_rec(i)
		if num_steps>longest_seq_len:
			longest_seq_len=num_steps
			starting_num=i
		if i not in dp:
			dp[i]=num_steps
			
	return starting_num,longest_seq_len
for i in range(1,21):
	starting_num,longest_seq_len=get_starting_num_for_longest_sequence_dp(i)
	print(i,starting_num,longest_seq_len)
print('--------------')		

# compute teh starting number for 1000000
n=1000000
starting_num,longest_seq_len=get_starting_num_for_longest_sequence_dp(n)
print(n,starting_num,longest_seq_len)	
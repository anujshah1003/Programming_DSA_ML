'''
this is a problem at hackerrank
Implement a modified Fibonacci sequence using the following definition:
    fib(n)=fib(n-1)**2 + fib(n-2)
'''
#The solution is based on dynamic programming bottom up approach
# solution -1 : Time Complexity: O(n)
#				Space Complexity: O(n)
# solution -2 : Time Complexity: O(n)
#				Space Complexity: O(1)

def fibonacci_modified_1(t1, t2, n):
    # Write your code here
    fib_table=[0]*n
    fib_table[0]=t1
    fib_table[1]=t2

    for i in range(2,n):
        fib_table[i]=fib_table[i-1]**2 + fib_table[i-2]
    return fib_table[-1]



def fibonacci_modified_2(t1, t2, n):
    # Write your code here
    prev_1=t2
    prev_2=t1
    
    for i in range(3,n+1):
        current_fib=prev_1**2+prev_2
        prev_2=prev_1
        prev_1=current_fib
    return prev_1
	
assert(fibonacci_modified_2(0,1,5)==5)
assert(fibonacci_modified_2(0,1,6)==27)
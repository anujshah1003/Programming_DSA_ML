'''
this is a problem from daily coding interview - https://www.dailycodingproblem.com/
I recived this question as I have sun=bscribed for recieveing mail
You are given an array of nonnegative integers. Let's say you start at the 
beginning of the array and are trying to advance to the end. You can advance 
at most, the number of steps that you're currently on. Determine whether you 
can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 
0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

'''

# The solution is based on dynamic programming bootom up approach
# Time Complexity : O(n^2)
# Space Complexity : O(1)

def can_reach_end(array):
    
    n=len(array)
    # if you have just one element you are alreday at the end
    if len(array)<=1:
        return True
    
    # loop and find the wheter you can reach the ith index from any of the previous indices
    
    for i in range(1,n):
        can_reach=False
        for j in range(i-1,-1,-1):
            if array[j]+j>=i:
                can_reach=True  # if we found tha twe can reacj i from any of the previous index , break no need to further look back
				break                # as we are building from bottom up, the previous index would alreday have been reached
        # if that index i was not possible to reach from anyindex simply return false because if we cannot reach this index how can we reach the end
		if not can_reach:
            return False
    if not can_reach:
        return False
    return True

array_1=[1, 3, 1, 2, 0, 1]
array_2=[1,0,0,1,2,1]
array_3=[1,2,1,0,0]

assert(can_reach_end(array_1)==True)
assert(can_reach_end(array_2)==False)
assert(can_reach_end(array_3)==False)
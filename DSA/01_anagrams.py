'''
Q Given two string check whether they are anagrams of each other

Two strings are said to be anagrams of one another if you can turn the first 
string into the second by rearranging its letters.

example
APPLE and ALPEP are anagrams
APPLE and APLLE are not anagrams because although they noth have same unique 
letter A,P,L and E the number of P and L is not same in both

PAIRS and PARIS are anagram
'''
#Solution-1 : Using Dictionary
# Time complexity O(N) <- O(N)+O(N)
# space complexity of O(N)

#Solution-2 : Using sorting
# Time comlexity O(NlogN) ,<- O(NlogN)+O(NlogN)+O(N)
# space complexity of O(N) <- O(N)+O(N)

# solution 1

word1='APPLE'
word2='AEPLP'

def check_anagrams(word1,word2):
    if len(word1)!=len(word2):
        return False
    # dcictionary for word 1
    char_count={}
    
    for char in word1:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
            
    for char in word2:
        if char not in char_count:
            return False
        if char_count[char]==0:
            return False
        else:
            char_count[char]-=1
            
    return True

print(check_anagrams(word1,word2))
print(check_anagrams('APPLE','APLLE'))
print(check_anagrams('APPLE','AMANGLE'))

# solution2

def check_anagrams_2(word1,word2):
    if len(word1)!=len(word2):
        return False
    
    sorted_word1=sorted(word1) #nlogn
    sorted_word2=sorted(word2)
    
#    for i in range(len(word1)):
#        if sorted_word1[i]!=sorted_word2[i]:
#            return False
    for char1,char2 in zip(sorted_word1,sorted_word2):
        if char1!=char2:
            return False
    return True

print(check_anagrams_2(word1,word2))
print(check_anagrams_2('APPLE','APLLE'))
print(check_anagrams_2('APPLE','AMANGLE'))
          
            
            
            
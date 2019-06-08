import sys

class Solution(object):
    # Write your code here
    def __init__(self):
        self.stack = list()
        self.queue = list()

    def pushCharacter(self, inputchar):
        self.stack.append(inputchar)

    def enqueueCharacter(self, inputchar):
        self.queue.append(inputchar)

    def popCharacter(self):
        outputchar = self.stack[0]
        self.stack.remove(outputchar)
        return outputchar

    def dequeueCharacter(self):
        outputchar = self.queue[-1]
        self.queue.remove(outputchar)
        return outputchar

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
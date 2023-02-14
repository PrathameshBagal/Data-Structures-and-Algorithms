# Input: S1 = ABCD, S2 = CDAB
# Output: Strings are rotations of each other

# Input: S1 = ABCD, S2 = ACBD
# Output: Strings are not rotations of each other
# Naive soln n*n
from operator import truediv


def checkStrRot(s1,s2,index):
   i=0
   while i<len(s1):
         if s1[i]!=s2[(index+i)%len(s1)]:
            return False
         i+=1
   return True

def isStrRotated(s1,s2):
   indexes=[]
   if len(s1)!=len(s2):
      return 0
   
   # Collected qall indexes of s2 which have s1[0]
   else:
      for i in range(len(s2)):
         if s2[i]==s1[0]:
            indexes.append(i)
   
   
   for index in indexes:
      
      strRot=checkStrRot(s1,s2,index)
      if strRot:
         return True
   return False

# Optimal approach
# We add s1 to s1 and check if s2 is a substring of s1

def isStrRotated2(s1,s2):
   s1=s1+s1
   if s2 in s1:
      return True
   else:
      return False

 
s1='abcdbab'
s2='bcdbaaa'
print(isStrRotated(s1,s2))

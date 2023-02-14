# from collections import Counter
s1='listen'
s2='silent'
count1={}
count2={}

# def checkAnagram(s1,s2):
#     if Counter(s1)==Counter(s2):
#         return True
#     return False

# Implemented Counter method manually
def checkAnagram2(s1,s2):
    for i in range(len(s2)):
        if s1[i] not in count1:
            count1[s1[i]]=1
        else:
            count1[s1[i]]+=1
    for i in range(len(s2)):
        if s2[i] not in count2:
            count2[s2[i]]=1
        else:
            count2[s2[i]]+=1
    print(count1,count2)
    return count1==count2

# Iterate through both.
# Add the chars of 1 and remove of s2
# if anagram then all values in dict should be zero
def checkAnagram3(s1,s2):
    counts={}
    for c1,c2 in zip(s1,s2):
        if c1 in counts:
            counts[c1]+=1
        else:
            counts[c1]=1
        if c2 in counts:
            counts[c2]-=1
        else:
            counts[c2]=-1 
    for count in counts.values():
        
        if count!=0:
            return False
    return True
s1='listen'
s2='silent'
print(checkAnagram2(s1,s2))
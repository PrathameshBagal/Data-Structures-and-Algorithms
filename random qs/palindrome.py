def palinRecursion(s,start,end):
    
        if s[start]!=s[end]:
            return False
        if start<=end:    
         return palinRecursion(s,start+1,end-1)    
        return True 
        


s="123421"
n=(len(s))
start=0
end=n-1
if palinRecursion(s,start,end):
    print("Palindrome")
else:
    print("not plaindrome")    


from collections import defaultdict
def redPar(op):
    s=[]
    operators=["+","/","*","-"]
    for i in range(len(op)):
        flag=True
        if op[i]!=")":
            s.append(op[i])
        else:
            #print(s)
            if s and s[-1]!="(":
                while s and s[-1]!="(":
                    if s[-1] in operators:
                        flag=False
                    s.pop()
                s.pop()
            if flag==True:
                return True
                
    return flag

op="((a+b)+c)"
print(redPar(op))

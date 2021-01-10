#. Naive string matching algo......... 
T=str(input())
P=str(input())
n=len(T) 
m=len(P)
c=0
for s in range((n-m)+1):
    j=0
    while(j<m and T[s+j]==P[j]):
        j+=1
    if j>=m:
        c+=1
        #print("found")
       # break
print(c)
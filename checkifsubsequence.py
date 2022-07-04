'''   q- find if the given subsequence is a subsequence of the given array...   '''

'''inserting values'''
arr=[]
subseq=[]
for i in range(int(input("length of main array >>"))):
    arr.append(int(input()))
for i in range(int(input("length of subsequence >>"))):
    subseq.append(int(input()))
    

# ------------------------- 1.  itration approach    ------------------------------------
j=0
val='no'
for i in subseq:
    while j<len(arr):
        if arr[j]==i:
            if subseq.index(i)==len(subseq)-1 :
                val='yes'
            j+=1
            break
        j+=1
print(val)


#  --------------------- 2.   recursion approach    ------------------------------------


# arr=[5,1,22,25,6,-1,8,10]
# subseq=[1,6,9,10]
def decide(arr, suseq, i=0, j=0):
    if(j==len(subseq)-1) and arr[i]==subseq[j]:
        print('yes')
        return 
    if(i==len(arr)-1):
        print('no')
        return 
    if arr[i]==subseq[j]:
        return decide(arr, subseq, i+1, j+1)
    return decide(arr, subseq, i+1, j)

decide(arr, subseq)

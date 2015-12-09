

a=[5, 2, 4, 6, 1, 3]


for j in range(1, len(a)):
    key=a[j]
    #Insert A[j] into the sorted sequence A[1...j-1]
    i=j-1
    while i>=0 and a[i]>key: #i had to be i>=0 (since we moved the ranges down). This is why it wasn't sorting the first item.
        a[i+1]=a[i]
        i=i-1
    a[i+1]=key
    
#To convert this code to work in Python 
def binary_search(array,key,low,high):
    while(low<=high):
        mid=(low+high)//2
        if(array[mid]==key):
            return mid
        elif(array[mid]<key):
            low=mid+1
        else:
            high=mid-1
    return -1
array=[1,2,3,4,5,6,7,8,9,10]
key=87
n=len(array)
res=binary_search(array,key,0,n-1)
if res == -1 :
    print('element is not found')
else:
    print("elemrnt is found at :",str(res))
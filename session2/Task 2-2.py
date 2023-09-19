#Quick Sort
def partition(Arr,first,last):
    pivot = first
    lastS1 = first
    firstUnknown = first+1
    while firstUnknown <= last:
        if(Arr[firstUnknown] < Arr[pivot]):
            lastS1 = lastS1+1
            Arr[lastS1],Arr[firstUnknown] = Arr[firstUnknown],Arr[lastS1]
        firstUnknown = firstUnknown+1
    Arr[first],Arr[lastS1] = Arr[lastS1],Arr[first]
    pivot =lastS1
    return pivot


def quick_sort(Arr,first,last):
    if(first<last):
        pivot = partition(Arr,first,last)
        quick_sort(Arr,first,pivot-1)
        quick_sort(Arr,pivot+1,last)

arr= [9,100,4,8,24,70,12,35,2,70,0,45]
print("Before sorting:",arr)
quick_sort(arr,0,len(arr)-1)
print("Quick  Sorting:",arr)
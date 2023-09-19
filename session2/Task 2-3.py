#using quick sort to sort both strings to be easily comapred
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

x = list(input("First String: "))
y =list(input("Second String: "))
quick_sort(x,0,len(x)-1)
quick_sort(y,0,len(y)-1)
if x == y:
    print("Anagrams")
else:
    print("Not Anagrams")


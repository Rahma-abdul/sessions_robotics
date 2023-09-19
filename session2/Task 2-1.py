def recursive_binanry_search(array,left,right,item):
    if left <= right:
        middle = (left + right )//2
        #print("Left:", array[left]," Right:",array[right], " Middle:",array[middle], " Item:", item)
        if array[middle] == item: #found
            return middle
        elif array[middle] > item:  #item is in left side
            return recursive_binanry_search(array,left , middle-1,item)
        elif array[middle] < item: #item is in right
            return recursive_binanry_search(array, middle+1, right , item)

    else:
        return -1

array = [4,9,16,20,60,77,89,100] #example
print("Array : ", array)
item = int(input("Enter item to search for: "))
output = recursive_binanry_search(array,0,len(array)-1,item)
if output != -1:
    print("Found at index: ",output)
else:
    print("Not Found")

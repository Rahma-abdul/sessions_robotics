def partition(Arr, first, last):
    pivot = first
    lastS1 = first
    firstUnknown = first + 1
    while firstUnknown <= last:
        if (Arr[firstUnknown] < Arr[pivot]):
            lastS1 = lastS1 + 1
            Arr[lastS1], Arr[firstUnknown] = Arr[firstUnknown], Arr[lastS1]
        firstUnknown = firstUnknown + 1
    Arr[first], Arr[lastS1] = Arr[lastS1], Arr[first]
    pivot = lastS1
    return pivot


def quick_sort(Arr, first, last):
    if (first < last):
        pivot = partition(Arr, first, last)
        quick_sort(Arr, first, pivot - 1)
        quick_sort(Arr, pivot + 1, last)



num = input("Input:  ")
item = int(input("Number: "))
flag = 0
num_list = num.split()
for i in range(0, len(num_list)):
    num_list[i] = int(num_list[i])
# to avoid O(n^2) ----> sort first ----> quick sort
quick_sort(num_list, 0, len(num_list) - 1)
#print(num_list)

x =0
y= len(num_list)-1
while x < y:
    z = num_list[x]+ num_list[y]
    if z == item:
        flag = 1
        break
    elif z > item:
        y =y-1
    else: x= x+1

if flag == 1:  # 2 numbers found
    print("Yes, ", item, " = ", num_list[x], "+", num_list[y])
else:
    print("NO")



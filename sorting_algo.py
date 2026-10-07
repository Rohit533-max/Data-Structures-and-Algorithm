#bubble sort
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i -1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

    return nums

#insertion sort
def insertion_sort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i -1
        while j >=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j-=1

        nums[j+1]=  key

    return nums

def quicksort(arr,start,end):
    if start < end:

        pivotIdx = partition(arr,start,end)

        quicksort(arr,start,pivotIdx-1)
        quicksort(arr,pivotIdx + 1,end)


def partition(arr,start,end):
    pivot = arr[end]
    i = start -1

    for j in range(start,end):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    #placing the pivot at its correct position
    i+=1
    arr[i],arr[end] = arr[end],arr[i]

    return i

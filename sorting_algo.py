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
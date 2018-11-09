def is_sorted(nums):
    isSorted = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            isSorted = False
    return isSorted
def main():
    num_list = [1,2,3,2,3]
    print(is_sorted(num_list))
main()
    

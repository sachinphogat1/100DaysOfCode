def remove_duplicates(nums):
    # index of the next non-duplicate element  
    l=1
    
    for r in range(1,len(nums)):
        if nums[r]!=nums[r-1]:
            nums[l] = nums[r]
            l+=1
    return nums[:l]

def main():

    print("Array w/o duplicate elements are: " + str(remove_duplicates([0,0,1,1,1,2,2,3,3,4])) )

main()


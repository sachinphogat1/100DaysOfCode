def square_of_sorted_arrays(nums):
    '''instead of comparing squares of both nums[L] and nums[R], we can compare abs(nums[L]) and abs(nums[R]) because squaring takes more time than absolute. Or we can store and reuse the squared values.'''
    l, r = 0, len(nums)-1
    res = []
    while(l<=r):

        # if nums[l]*nums[l]>nums[r]*nums[r]:
        if abs(nums[l])>abs(nums[r]):
            res.append(nums[l]*nums[l])
            l+=1
        else:
            res.append(nums[r]*nums[r])
            r-=1

    return res[::-1]

def main():
    print("Squared array is: " + str(square_of_sorted_arrays([-4,-3,0,1,2,3])))

main()


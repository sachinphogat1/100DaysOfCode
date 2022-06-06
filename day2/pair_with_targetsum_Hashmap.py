### Two Number Sum Solution 1
# def pair_with_targetsum_Hashmap(arr, target_sum):
#     nums = {}
#     for i, num in enumerate(arr):
#         if target_sum - num in nums:
#             return [nums[target_sum - num],i]
#         else:
#             nums[arr[i]] = i
#     return [-1, -1]




### Two Number Sum Solution 2
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     dict = {}
#     for i in range(len(array)):
#         secondNumber = targetSum - array[i]
#         if secondNumber in dict:
#             return [array[i], secondNumber]

#         else:
#             dict[array[i]] = i

#     return []
#     pass


def main():
    print(pair_with_targetsum_Hashmap([1,2,3,4,6],6))
    print(pair_with_targetsum_Hashmap([2,5,9,11],11))

main()
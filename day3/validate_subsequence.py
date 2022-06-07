"""SOLUTION1"""
#This is my solution, But this will run longer, but its possible to stop the array traversing soon if we find all the elements too soon in the subsequence
#Here some of the edge cases are failing
# def validate_subsequence(array, subsequence):

#     r=0
#     for i in range(len(array)-1):
#         # while r <= len(subsequence)-1:
#         if array[i] == subsequence[r]:
#             r+=1
#             continue

#         else:
#             continue

#     if r == len(subsequence)-1:
#         return True

#     else:
#         return False

print(validate_subsequence([5,1,22,25,6,-1,8,10],[22,25,6]))

"""SOLUTION2"""
#Real Solution: O(N) N-> Number of elements in main array

# O(1) in space

def validate_subseq(array, subseq):

    arrIdx = 0 
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(subseq):
        if array[arrIdx] == subseq[seqIdx]:
            seqIdx+=1
        arrIdx+=1

    return seqIdx == len(subseq)  # Its not seqIdx == len(subseq) - 1 because we are initializing the seqIdx = 0 at the beginning!

print(validate_subseq([],[]))

"""SOLUTION3"""

# def validateSubsequence(array, sequence):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(sequence):
#             break
#         if sequence[seqIdx] == value:
#             seqIdx+=1
#     return seqIdx == len(sequence)

# print(validateSubsequence([],[]))
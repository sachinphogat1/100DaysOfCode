from typing import List


def minimum_size_subarray_target(target_sum, arylst: List[int]):
    lftptr=0
    target=0
    res = float("inf")
    for r in range(len(arylst)):
        target+= arylst[r]
        while target>=target_sum:
            res = min(r-lftptr+1, res)
            target -= arylst[lftptr]
            lftptr+=1

    return 0 if(res == float("inf")) else res

lst = []
print("Enter the element you want to add into the list: ")

while(True):
    lst_input =int(input())
    if(lst_input!=0):
        lst.append(lst_input)
    else:
        break

print("Enter the target sum: ")
target_input = int(input())

print(minimum_size_subarray_target(target_input, lst))

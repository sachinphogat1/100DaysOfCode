def three_number_sum(arr):
    arr.sort()
    triplet = []
    for i in range(len(arr)-2):
        l = i+1
        r = len(arr)-1

        while l<r:
            
            if arr[i]+arr[l]+arr[r] == 0:
                triplet.append([arr[i], arr[l], arr[r]])
                l+=1
                r-=1

            elif arr[i]+arr[l]+arr[r] < 0:
                l+=1

            else:
                r-=1

    return triplet

print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6]))
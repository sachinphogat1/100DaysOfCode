def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        """Here above we are adding the next element 
        slide the window, we dont need to slide if we've not hit 
        the required window size """

        if windowEnd >= K-1:
            result.append(windowSum / K) #calculate the average
            windowSum -= arr[windowStart]
            windowStart +=1

        return result

def main():
    result = find_averages_of_subarrays(5, [1,3,2,6,-1,4,1,8,2])
    print("Averages of subarrays of size K: " + str(result))

main()
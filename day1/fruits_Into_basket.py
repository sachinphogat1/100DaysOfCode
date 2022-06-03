def fruits_into_basket(K, arr):

    max_length = 0
    window_start = 0
    fruit_basket = {}

    for window_end in range(len(arr)):

        right_fruit = arr[window_end]
        if right_fruit not in fruit_basket:
            fruit_basket[right_fruit] = 0
        fruit_basket[right_fruit] +=1

        while len(fruit_basket) > K:
            left_fruit = arr[window_start]
            fruit_basket[left_fruit] -=1
            if fruit_basket[left_fruit] == 0:
                del fruit_basket[left_fruit]
            window_start +=1

        max_length = max(max_length, window_end - window_start +1)
    return max_length

def main():

    print("Max length is: " + str(fruits_into_basket(2, ['A','B','C','A','C'])))
    print("Max length is: " + str(fruits_into_basket(2, ['A','B','C','B','B','C'])))

main()



from curses import window
from turtle import left
from typing import List


def maximum_number_of_fruits_in_two_baskets(basket):
    window_start, window_end = 0, 0
    fruits = {}
    max_length = 0

    for window_end in range(len(basket)):
        Curr_fruit = basket[window_end]
        if Curr_fruit not in fruits:
            fruits[Curr_fruit]=0
        fruits[Curr_fruit]+=1

        while len(fruits)>2:
            left_fruit = basket[window_start]
            fruits[left_fruit] -=1
            if fruits[left_fruit]==0:
                del fruits[left_fruit]
            window_start+=1
            max_length = max(max_length, window_end - window_start +1)
    return max_length

def main():
    print("Maximum number of fruits " + str(maximum_number_of_fruits_in_two_baskets(['A','B','C','A','C'])))

main()
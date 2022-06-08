"""SOLUTION
Here the logic is that if the next coin in the sorted array is larger than
the sum off all the coins till now + 1 then sumof all the coins till now + 1 
will be the answer

else

it will be added to the sum of coins

"""


def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:

        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1

print("str(sachin)")
print(nonConstructibleChange([5,7,1,1,2,3,22]))

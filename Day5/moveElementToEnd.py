def moveElementToEnd(array, toMove):

    ptr1 = 0
    ptr2 = len(array) - 1

    while ptr1 < ptr2:
        if array[ptr1] == toMove:
            while array[ptr2] == toMove and ptr1 < ptr2:
                ptr2-=1
            array[ptr1] = array[ptr2]
            ptr1+=1
            array[ptr2] = toMove
            ptr2-=1

        else:
            ptr1+=1

    return array


print(moveElementToEnd([2,1,2,2,2,3,4,2],2))
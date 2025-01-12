# This logic sorts items in monotonically descending order.
def insertion_sort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i - 1
        #Flipping the > to < here to change the ascending order to descending order
        while j >= 0 and Arr[j] < key:
            Arr[j + 1] = Arr[j]
            j = j - 1
        Arr[j + 1] = key
    return Arr  

arr = [7,5,2,11,65, 23,33,21, 11]    
print("Sorted array in monotonically descending order:", insertion_sort(arr))
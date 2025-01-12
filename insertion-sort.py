# This logic sorts items in ascending order.
# Need to change the logic so that it is in descending order.
def insertion_sort(Arr):
    for i in range(1, len(Arr)):
        key = Arr[i]
        j = i - 1
        while j >= 0 and Arr[j] > key:
            Arr[j + 1] = Arr[j]
            j = j - 1
        Arr[j + 1] = key
    return Arr  

arr = [7,5,2,11,65, 23,33,21]    
print("Sorted array in ascending order:", insertion_sort(arr))
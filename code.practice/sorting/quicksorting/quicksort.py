def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    
    greater = quicksort([i for i in array[1:] if i >= pivot])
    less = quicksort([i for i in array[1:] if i < pivot])

    return less + [pivot] + greater


if __name__ == "__main__":
    print(quicksort([5,3,6,1,8,2]))
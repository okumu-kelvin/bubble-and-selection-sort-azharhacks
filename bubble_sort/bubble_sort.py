values = [64, 34, 25, 12, 22, 11, 90]
def bubble_sort(numbers):
    # TODO: Implement bubble sort
    
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j + 1]:
                x=numbers[j+1]

                numbers[j+1]=numbers[j]
                numbers[j]=x
    return numbers
    pass
sorted_list = bubble_sort(values)
print("Sorted list:", sorted_list)

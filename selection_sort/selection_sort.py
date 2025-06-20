values=[1, 34, 25, 12, 22, 11, 34]
def selection_sort(numbers):
    # TODO: Implement selection sort
     
    for i in range(len(numbers)):
        print("i",numbers[i])
        
        min_index = i
        for j in range( i+1,len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
                print("j",numbers[j])

        # Swap the found minimum with the first unsorted element
        x=numbers[i]
        numbers[i]=numbers[min_index]
        numbers[min_index]=x
        
    return numbers
    pass
sorted_list = selection_sort(values)
print("Sorted list:", sorted_list)

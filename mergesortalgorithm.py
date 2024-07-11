def mergeSort(array):
    if len(array) <= 1:
        return
    else:
        middle_point = len(array) // 2
        left_part = array[:middle_point]
        right_part = array[middle_point:]
        mergeSort(left_part)
        mergeSort(right_part)
        left_array_index = 0
        right_array_index = 0
        sorted_index = 0
        while left_array_index < len(left_part) and right_array_index < len(right_part):
            if left_part[left_array_index] < right_part[right_array_index]:
                array[sorted_index] = left_part[left_array_index]
                left_array_index += 1
            else:
                array[sorted_index] = right_part[right_array_index]
                right_array_index += 1
            sorted_index += 1
        while left_array_index < len(left_part):
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
            sorted_index += 1
        while right_array_index < len(right_part):
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
            sorted_index += 1
if __name__ == "__main__":
    test_case = [1, 7, 5, 3, 2, 4, 11]
    mergeSort(test_case)
    print(test_case)
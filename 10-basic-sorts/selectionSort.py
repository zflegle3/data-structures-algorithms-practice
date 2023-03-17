def selection_sort(my_list):
    for i in range(len(my_list)-1):
        #initalize selected as first item of unsorted items
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                # updates min index to smallest item of unsorted items
                min_index = j
        #swap item at i and item at min index
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([4,2,6,5,1,3]))
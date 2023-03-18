def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    #rearranges items in list so pivot item in middle
    # less than items to left
    # greater than items to right
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    #returns index not value
    return swap_index

def quick_sort_helper(my_list, left, right):
    if left < right:
        #excludes pivot index b/c sorted
        pivot_index = pivot(my_list, left, right)
        #recursive call on left
        quick_sort_helper(my_list, left, pivot_index-1)
        #recursive call on right
        quick_sort_helper(my_list, pivot_index+1, right)
    #base case
    #stops running code when left and right index are equal
    return my_list

def quick_sort(myList):
    #removes need to pass list indices
    return quick_sort_helper(my_list, 0, len(my_list)-1)


my_list = [4,6,1,7,3,2,5]
print(quick_sort(my_list))

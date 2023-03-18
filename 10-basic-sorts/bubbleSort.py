def bubble_sort(my_list):
    #for each item in list
    for i in range(len(my_list)-1, 0, -1):
        #compare to 
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                #swap items
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([4,2,6,5,1,3]))
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

    #Drop non dominants
    #single for loop ran O(n)
    for l in range(n):
        print(l)
    

print_items(10)


# NOTES:
# n*n items returned (i,j)
# n*n*n items returned (i,j,k)
# Regardless of # of nested loops, simplified to O(n^2)
# EX: 3 loops >> O(n^3) >> O(n^2)

#Drop non dominants
#single for loop (l) ran O(n)
#Total function ran as O(n^2 + n)
#Can drop n bc it is non dominant and insignificant in comparison to n^2
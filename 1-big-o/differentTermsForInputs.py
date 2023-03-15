def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(i)

print_items(10)
#complexity O(a + b)

def print_items_nested(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items(10)
#complexity O(a * b)
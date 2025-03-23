def remove_element(arr):
    iterator = enumerate(arr)
    for i in iterator:
        if(i[0] == 0 or i[0] == 5 or i[0] == 2):
            arr.pop(i[0])
    print(arr)
            


arr = ['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']

remove_element(arr)
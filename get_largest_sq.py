def get_largest_sqr(listx):
    len_list = len(listx)
    for i in range(len_list):
        x = listx[i]
        listx[i] = x*x
    largest = max(listx)
    return largest

list1 = [2,-3,1]
result = get_largest_sqr(list1)
print(result)
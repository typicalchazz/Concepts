a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def in_both(list1,list2):
    sol_list = []
    for item in a:
        for num in b:
            if num == item:
                if num not in sol_list:
                    sol_list.append(num)
    return sol_list

print(in_both(a,b))
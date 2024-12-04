num_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list2 = num_list.copy()
list3 = []

for _ in num_list:
    list3.append(list2[-1])
    list2.pop(-1)

    num_list = list3
    print(num_list)

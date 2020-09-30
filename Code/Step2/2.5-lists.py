# my_list = [int(i) for i in input().split()]
# if len(my_list) > 1:
#     for i in range(len(my_list)):
#         print(int(my_list[i-1]) + int(my_list[i+1-len(my_list)]), end=" ")
# else:
#     print(my_list[0])


my_list, new_list = [int(i) for i in input().split()], []
[new_list.append(elm) for elm in my_list if my_list.count(elm) > 1 and elm not in new_list]
print(*new_list)
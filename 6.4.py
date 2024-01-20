def sumof_list(list1,total_number =None):
    if(total_number is None):
        total_number = [0]
    for count in list1:
       total_number[0] += count
    return total_number[0]



list1 = [3,4,5]
total_number = sumof_list(list1)
print(total_number)
 
def split_list(grade):
    sum = 0
    lst_1 = []
    lst_2 = []
    try:
        for i in grade:
            sum += i
        average_val = sum / len(grade)
    except ZeroDivisionError:
        return lst_1, lst_2
    for i in grade:
        if i <= average_val:
            lst_1.append(i) 
        elif i > average_val:
            lst_2.append(i)
        else:
            return lst_1, lst_2
    return lst_1, lst_2
                


grade = [5, 13, 26, 23, 30, 50, 14, 10]
split_list(grade)

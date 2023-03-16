def devolver_distintos(int1, int2, int3):

    num_list = [int1,int2,int3]

    if sum(num_list) > 15:
        return max(num_list)
    elif sum(num_list) < 10:
        return  min(num_list)
    elif sum(num_list) >= 10 and sum(num_list) <= 15:
        num_list.remove(max(num_list))
        num_list.remove(min(num_list))

        return num_list[0]

print(devolver_distintos(10,3,1))
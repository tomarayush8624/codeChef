total_cases = int(input())
for i in range(total_cases):
    arr_size = int(input())
    arr_given = list(map(int, input().split(" ")))
    total_ele = {}
    for i in arr_given:
        if i in total_ele:
            total_ele[i] += 1
        else :
            total_ele[i] = 1
    
    ele = max(total_ele.values())
    print(arr_size - ele)

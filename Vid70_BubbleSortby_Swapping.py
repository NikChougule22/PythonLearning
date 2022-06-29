def sort(list):
    for i in range(len(list) - 1, 0, -1):  # i goes from 5 to 0 so from last num in list to first num
        for j in range(i):  # j goes from 1 st to ith num in list like 1 to 6 in first loop
            # 1 to 5 in 2nd loop and 1 to 4 in 3rd loop and so on comparing if jth num is
            # > (j+1)th number to see if swapping is required
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
                print(list, 'i =',i,'j =',j)

list = [5, 3, 8, 6, 7, 2]

sort(list)
print(list)

# Selection sort is used because bubble sort takes lot of space while sorting as it goes through loop multiple times
# and selection sort on other hand does this faster and requires less memory and time
def sort(list):
    for i in range (5):
        minpos = i
        for j in range (i,6):
            if list[j] < list[minpos]:
                minpos = j
            print( 'i = ',i,'j =',j, list,minpos)

        temp = list[i]
        list[i]=list[minpos]
        list[minpos]=temp
        print(list)

list = [5, 3, 8, 6, 7, 2]

sort(list)
print(list)






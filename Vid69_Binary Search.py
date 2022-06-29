# Binary search is done if you want to find a number from a big array or list and
# to avoid to go through huge list because it increases time as well as takes space

Pos = -1

def search(list,n):
    l=0; u=len(list)-1

    while l<=u:
        mid = (l + u) // 2
        if list[mid]==n:
            globals()['Pos'] = mid
            return True
        else:
            if list[mid]<n:
                l=mid + 1
            else:
                u=mid - 1
    return False

list=[1,22,33,55,66,77,88,99]
n=1
if search(list,n):
    print("Value found in List at",Pos+1)
else:
    print("Value not found in list")

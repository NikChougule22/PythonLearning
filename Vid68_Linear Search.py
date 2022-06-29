Pos = -1
Pos2=0
n=2
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals() ['Pos'] = i
            return True
        i += 1
    return False

list = [1,9,6,5,4,3,7]

if search(list,n):
    print("Value found at position",Pos+1,"in list")
else:
    print("Value not present in list")

# Using For loop
def search2(list,n):
        ii = 0
        index=1
        for ii in list:
            if ii==n:
                globals()['Pos2'] = index
                return True, index
            index += 1

if search2(list,n):
    print("Value found at position",Pos2,"in list")
    print(Pos2)
else:
    print("Value not present in list")

# Example 1- Generator can be used to access iterator easily. By using generator we do not need to create
# or define _iter_ and _next_. Generator does that automatically for you just by using yield

def topten():

    yield 1
    yield 2
    yield 2
    yield 3
    yield 4


values=topten()

#print(values.__next__())

for i in values:
    print(i)

# Example 2, want to print top ten perfect square:

def topsquares():

    n=1

    while n<=10:
        sq=n*n
        yield sq
        n+=1

val=topsquares()

for i in val:
    print(i)
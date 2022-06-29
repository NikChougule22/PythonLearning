# We want to print values for top ten iterations
# we need to methods for doing any iterations possible in python. __iter__ and __next__

class TopTen:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num += 1
            return val
        else:
            raise StopIteration

Values=TopTen()

for i in Values:
    print(i)

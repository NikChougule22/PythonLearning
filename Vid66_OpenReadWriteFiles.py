f=open('PyData','r') # Open PyData Text file and read file

#print(f.read) # prints the object and address
#print(f.read()) # Prints all the data from file that is read
#print(f.readline())# Reads and prints single line at a time

# print(f.readline(),end="") # prints first line and then end helps to say line end and go to next line
# print(f.readline())

f1=open('abc','w')
# f1.write('Something is printed in Laptop')
# f1=open('abc','a')
# f1.write('HP')

#Copying data from one file and writing in other
for data in f:      # goes line by line to copy data from file f
    f1.write(data)   # writes all data in file f1 one by one as loop progresses


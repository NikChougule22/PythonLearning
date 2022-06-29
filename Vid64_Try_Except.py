a=4
b=2

try:     # Try these things without giving error
    print ("resource open")
    print(a/b) # if error happens at this statement it will jump to except line and not execute next lines below it
    k=int(input("Enter a number"))
    print(k)
    print(i)
except ZeroDivisionError as e:  # handle if this error happens by printing this statement
    print("You can not divide by zero")

except ValueError as e:
    print("Invalid Input")

except Exception as e:  # Handle all/ anytime of error including above two/ is used as general one for any error
    print("Something else is wrong, please double check")

finally:  # Helps to try anything that needs to be outside of try and except
    print("resource closed")

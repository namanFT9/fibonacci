#initiation
def Fibonacci(n):

    #execution   
    #Check if the input is 0
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Updation
print(Fibonacci(9))

a = int(input("What number would you like to substitute for Fizz?  ")) # prompts user for two inputs in order the substite for Fizz and Buzz
b = int(input("What number would you like to substitute for Buzz?  "))

def Fizzbuzz(n):
    for i in range (n): #runs below code loop 100 times
        if i % a == 0 and i % b == 0: # first checks for multiples of a AND b as cannot check this after i has been changed
            i = "FizzBuzz" # substitutes for string and prints the string
            print(i)
        elif i % a == 0: # checks just a
            i = "Fizz"
            print(i)
        elif i % b == 0: # checks just b
            i = "Buzz"
            print(i)
        else:
            print(i) # if no conditions are met it will just print i as the number

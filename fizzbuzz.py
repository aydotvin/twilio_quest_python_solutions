import sys

numbers = sys.argv

for i in range(len(numbers)):
    if(i > 0):
        n = int(numbers[i])
        if(n % 3 == 0 and n % 5 == 0):
            print("fizzbuzz")
        elif(n % 3 == 0):
            print("fizz")
        elif(n % 5 == 0):
            print("buzz")
        else:
            print(n)
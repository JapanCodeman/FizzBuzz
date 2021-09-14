'''
FizzBuzz

Create a function that lists all numbers from 1 - 100. All multiples of 3 should be replaced by the string 'Fizz',
all multiples of 5 should be replaced by the string 'Buzz', and all multiples of 3 and 5 (i.e. 15) should be replaced
by 'FizzBuzz'

Hints:

- Functions
- Looping
- Conditionals
- Math Operators

* Extra Credit - Make the function be able to run to any number of specified digits by the user (i.e. instead of 1-100,
it could run up to 1000 or a million, etc.
'''


def fizz_buzz(num1 = 1, num2 = 101):
    for i in range(num1, num2):
        if (i / 3) == 1:
            print("Fizz")
        elif (i / 5) == 1:
            print("Buzz")
        elif (i / (3 * 5)) == 1:
            print("FizzBuzz")


fizz_buzz()
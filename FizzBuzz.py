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


def fizz_buzz(num1=1, num2=100):
    num2 += 1
    num_list = []
    fizz_buzz_list = []
    for i in range(num1, num2):
        num_list.append(i)

    for i in num_list:
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append("fizzbuzz")
        elif i % 5 == 0:
            fizz_buzz_list.append("buzz")
        elif i % 3 == 0:
            fizz_buzz_list.append("fizz")
        else:
            fizz_buzz_list.append(i)

    for i in fizz_buzz_list:
        print(i)


fizz_buzz(1, 5)
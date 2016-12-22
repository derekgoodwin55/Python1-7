### Input ###

number = int(input("Enter the upper bound: "))

### Perfect Numbers Accumulator ###

perfect_numbers = ''

### Upper Bound Test ###

while number < 1:
    print("\nInvalid upper bound!\n")
    number = int(input("Enter the upper bound: "))

### While Loop + Nested While Loop ###
integer = number + 1
while integer > 0:
    integer -= 1
    pool = 0
    divisor = integer
    while divisor >= 2:
        divisor -= 1
        if integer % divisor == 0:
            pool += divisor
            if int(pool) == int(integer) and divisor == 1:
                perfect_numbers += str(integer) + " "
                    
### Output ###

print("Perfect numbers in the interval", range(number), ":", perfect_numbers)

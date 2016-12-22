### Input (which is the Iterator Variable) ###

integer = int(input("Enter an integer value: "))

### Integer Greater than Zero Test ###

while integer < 0:
    print("\nInput must be greater or equal to zero\n")
    integer = int(input("Enter an integer value: "))

### Accumulator Variable ###

empty_str = ''


### Iteration, Accumulatiion and Concatenation ###

while integer > 0:
    one_or_zero = str(integer % 2)
    empty_str = one_or_zero + empty_str
    integer = integer // 2

### Output ###

print("Base-2 equivalent:", empty_str)

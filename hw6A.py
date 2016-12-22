### Recursive Function Definition 1 ###

def digitsum(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    else:
        return int(n[-1]) + int(digitsum(n[:-1]))

### Recursive Function Definition 2 ###

def digitalroot(n):
    if digitsum(n) < 10:
        return digitsum(n)
    else:
        return digitalroot(digitsum(n))

### Input & Function Call ###

starting_input = int(input("Enter an integer: "))

value = digitalroot(starting_input)

### Output ###

print("The digital root of your value is:",value)

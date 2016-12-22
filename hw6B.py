### Recursive Function with 2 Base Cases ###

def pyramid(h):
    if h == 1:
        return h
    elif h == 0:
        return 0
    else:
        return (h**2 + pyramid(h-1))

### Input ####

number_of_spheres = int(input("Enter a value for the height of a pyramid: "))

### Positive Integer Check ###

if number_of_spheres < 0:
    print("Your input was negative and converted to its positive equivalent")
    number_of_spheres = (number_of_spheres * -1)

### Function Call with 1 Argument ###

function_call = pyramid(number_of_spheres)

### Output ###

print("The number of spheres in a pyramid with height",number_of_spheres, "is", function_call)

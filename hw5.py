### Part 1 Function ###

def OneDigit(x):
    if x == "I" or x == "i":
        return 1
    elif x == "V" or x == "v":
        return 5
    elif x == "X" or x == "x":
        return 10
    elif x == "L" or x == "l":
        return 50
    elif x == "C" or x == "c":
        return 100
    elif x == "D" or x == "d":
        return 500
    elif x == "M" or x == "m":
        return 1000
    else:
        return 0

### Part 2 Function ###

def RomanNumerals(y):
    total_sum = 0

    i = 0
    while i < len(y):
        if len(y) > 3 and ((i+3) < len(y)) and OneDigit(y[i]) == OneDigit(y[i+1]) == OneDigit(y[i+2]) == OneDigit(y[i+3]):
            print("Invalid Roman Numeral. Symbol repeated more than 3 times in succession.")
            raise SystemExit
        else:
            if len(y) > 1 and ((i+1) < len(y)) and (OneDigit(y[i]) < OneDigit(y[i+1])):
                total_sum += OneDigit(y[i+1]) - OneDigit(y[i])
                if y[i] in "VLDvld":
                    print("Cannot use V, L or D for subtraction.")
                    raise SystemExit
                if (OneDigit(y[i+1]) != (5* OneDigit(y[i]))) or (OneDigit(y[i+1]) != (10* OneDigit(y[i]))):
                    print("Cannot Subtract the Value at " + y[i] + " from " + y[i+1])
                    raise SystemExit
                    
                i += 2
            else:
                total_sum += OneDigit(y[i])
                i += 1
    return "Decimal value: " + str(total_sum)

### Input/Function Call/Part 3 Function ###

numeral_expression = str(input("Enter a Roman Numeral: "))

while numeral_expression != "":
    answer = RomanNumerals(numeral_expression)
    print(answer)
    numeral_expression = str(input("Enter a Roman Numeral: "))

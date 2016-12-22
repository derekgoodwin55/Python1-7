### Intro Message ###

print("This Program Converts Any Dollar Amount to the Smallest \
Amount of Coins of Equal Value\n\n")

### Inputs ###

dollar = int(input("Enter any amount of dollars: "))

cents = int(input("Enter an amount of cents: "))

### New Abstract Data Type ###

total = dollar + (cents/100)

### Operations ###

quarters = total// .25

remainder_for_dimes = round(total % .25, 2)

dimes = remainder_for_dimes // .1

remainder_for_nickels = round(remainder_for_dimes % .1, 2)

nickels = remainder_for_nickels // .05

remainder_for_pennies = round(remainder_for_nickels % .05, 2)

pennies = remainder_for_pennies * 100
        
### Output ###

print()

print(int(quarters), "quarters")

print(int(dimes), "dimes")

print (int(nickels), "nickels")

print(int(pennies), "pennies")

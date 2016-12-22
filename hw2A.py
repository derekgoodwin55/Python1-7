### Input ###

balance = float(input("Enter current account balance: "))

### Valid Account Balance Check ###

while balance < 0:
    print("\n Invalid account balance \n\n")
    balance = float(input("Enter current account balance: "))

### Possible Error Resolved ###

if balance > 999.99 and balance <1000:
    balance = 999.99

### Round Account Balance to Nearest Penny ###
    
balance = round(balance,2)

### Conditional Statements ###

if balance <= 1000:
    interest = round(balance * .015, 2)
    amount_due = round(balance + interest,2)
    if amount_due <= 10:
        minimum_payment = amount_due
    else:
        minimum_payment = round((amount_due / 10),2)
        minimum_payment2 = 10.00
        if minimum_payment < minimum_payment2:
            minimum_payment = minimum_payment2
else:
    balance2 = balance - 1000
    interest = round((balance2 * .01) + 15, 2)
    amount_due = balance + interest
    minimum_payment = round((amount_due / 10),2)
    
### Outputs ###

print("\nInterest:", interest)
print("Amount Due:", amount_due)
print("Minimum Payment:", minimum_payment)

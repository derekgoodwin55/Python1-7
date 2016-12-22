### Inputs ###

String1 = str(input("Enter first string: "))

String2 = str(input("Enter second string: "))

String3 = str(input("Enter third string: "))

### Conditional Statements and Printed Outputs ###

if String1 < String2 and String1 < String3:
    print(String1)
    if String2 < String3:
        print(String2)
        print(String3)
    else:
        print(String3)
        print(String2)

if String2 < String1 and String2 < String3:
    print(String2)
    if String1 < String3:
        print(String1)
        print(String3)
    else:
        print(String3)
        print(String1)

if String3 < String1 and String3 < String2:
    print(String3)
    if String1 < String2:
        print(String1)
        print(String2)
    else:
        print(String2)
        print(String1)

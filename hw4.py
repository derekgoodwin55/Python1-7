### Empty List and Mean Accumulator Variables ###

total_scores = []

mean = 0

### Initial Score to Setup While Loop ###

score = int(input("Enter a score: "))

if score >= 0 and score <= 100:
    total_scores.append(score)
    mean = mean + score
    minimum = score
    maximum = score
else:
    print("Invalid score... re-enter")
    score = 0
    minimum = 100
    maximum = 0
    mean = 0

### While Loop to Store Scores ###

while score >= 0:
    score = int(input("Enter a score: "))
    if score <= 100 and score >= 0:
        total_scores.append(score)
        mean += score
        if score > maximum:
            maximum = score
        if score < minimum:
            minimum = score
    elif score < 0:
        print()
    else:
        print("Invalid score... re-enter")

### Abstract Data Type for Number of Scores ###

length_of_list = len(total_scores)

### Abstract Data Type for Mean ###

mean = mean / length_of_list

### Standard Deviation ###

variance = 0

i = 0

while i < len(total_scores):
    variance += (total_scores[i] - mean)**2
    i += 1

standard_dev = (variance / length_of_list)**.5

### Output ###

print("-------------------\n")
print("Number of scores:", length_of_list)
print("Maximum score:", maximum)
print("Minimum score:", minimum)
print("Average score:", round(mean, 2))
print("Standard dev.:", round(standard_dev, 2))

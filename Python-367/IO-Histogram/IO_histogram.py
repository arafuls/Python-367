from collections import Counter

sumCol0 = 0
sumCol1 = 0
sumCol2 = 0
numOfLines = 0

# column averages
with open("data.txt", "r") as f:
    for line in f:
        currentline = line.split(",")
        sumCol0 += int(currentline[0])
        sumCol1 += int(currentline[1])
        sumCol2 += int(currentline[2])
        numOfLines += 1

# histogram (sum -> occurance)
with open("data.txt", "r") as f:
        with open("histogram.txt", "w") as f2:
            for line in f:
                currentline = line.split(",")
                lineSum = str(int(currentline[0]) + int(currentline[1]) + int(currentline [2])) + "\n"
                f2.write(lineSum)

# displaying column averages
print("-------------------------------------------")
print("Average 1: ", round(sumCol0 / numOfLines, 3))
print("Average 2: ", round(sumCol1 / numOfLines, 3))
print("Average 3: ", round(sumCol2 / numOfLines, 3))

# displaying histogram info
print("-------------------------------------------")
print("Histogram of sums:")
with open("histogram.txt", "r") as f:
    c = Counter()
    for line in f:
        c.update(line.split())
    for key, value in sorted(c.items()):
        print(key, "->", value)

array=[10, 20, 30, -10, -20, -30, 10]

## soma do array
i = 0
sum = 0
for item in array:
    sum = array[i] + sum
    i = i + 1

print(sum)

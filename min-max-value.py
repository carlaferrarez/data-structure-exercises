array=[10, 20, 30, -1, 50, -2, 0, 0, 50]

maxValue = array[0]
i = 0
## valor maximo do array
for item in array:
    if array[i] > maxValue:
        maxValue = array[i]
    i = i + 1

print(maxValue)

minValue = array[0]
i = 0
for item in array:
    if array[i] < minValue:
        minValue = array[i]
    i = i + 1
    
print(minValue)


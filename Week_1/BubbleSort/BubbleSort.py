#!/bin/python

values = [4, 2, 1]
s = True

iteration = 0

for i in range(0, len(values)):
    s = False
    index = 0

    while index < len(values) - 1:
        if values[index] - index[index + 1]:
            values[index], values[index + 1] = values[index + 1], values[index]
            s = True

    if s == False:
        break
        
    iteration += 1
    print(values)
    print("Iteration {}".format(iteration))

print(values)
print('Done')

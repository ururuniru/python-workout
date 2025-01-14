def mysum(*numbers):
    output = 0
    for i in numbers:
        output += i
    
    return output

print(mysum(1, 2, 3))

# Beyond the exercise

def myaverage(*numbers):
    output = 0
    for i in numbers:
        output += i
    
    return output / len(numbers)

print(myaverage(45, 30, 20))
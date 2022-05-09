def average(a,b):
    return (a + b) / 2

running_sum = 0
for i in range(10):
    running_sum += 3


def mySum(num):
    running_sum = 0
    for i in range(1,num+1):
        running_sum += i
    return running_sum

# Square + 1 summation
def mySum2(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 + 1
    return running_sum

def average3(numList):
	return sum(numList) / len(numList)
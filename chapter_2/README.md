# Making Tendious Arithmetic Fun

## Basic Operators


| **Operator**   | **Syntax** |
| ---------------- | ------------ |
| Addition       | +          |
| Substraction   | -          |
| Multiplication | *          |
| Division       | /          |
| Exponent       | **         |

## Notes

When using + sign with strings, the strings concatenate.

```python
# Enumerate function
for index, name in enumerate(list):
	print(f"{index} - {name}")

# Checking for type
type(item) # return data type

# Checking index
list.index(item) # returns index

```

- Strings use indicies too (Can be reffered to, print len() etc)

## Summation

- Greek letter Sigma

```python
# Summation of all the numbers in the range from 1 to the given integer
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
```

## Average

```python
# Function finding average of any numerical list
def average3(numList):
	return sum(numList) / len(numList)
```

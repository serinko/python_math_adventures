# Factors
**Find factors of any given number:**

```python
# TODO
# 1. Define the factors Function, which takes a number as an argument
# 2. Create an empty factors list to fill factors.
# 3. Loop over all the numbers from 1 to the given number
# 4. If any of these numbers divides evenly, add it to the factors list.
# 5. Return the list of factors at the end.

def factors(num):
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors
```

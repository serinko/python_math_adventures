# Transforming and Storing Numbers with Algebra
## Solving First Degree Equations
Say we have an equation to solve:
```latex
$2x + 5 = 13$
```
**Using Brute Force**
```python
# Solving mathematical equation by brute force:

def plug():
    x = -100 # start at -100
    while x < 100: # go up to 100
        if 2*x + 5 == 13: # if it makes the equation true
            print("x = ", x) # print it out
        x += 1 # make x go up b 1 to test the next number
        
plug()
```

# Lambda function to double a given argument
doubler = lambda n: n * 2

# Test the doubler function with different values
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Lambda function to triple a given argument
tripler = lambda n: n * 3

# Test the tripler function with different values
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# Function that returns a multiplier lambda for any given factor
def multiplier(factor):
    return lambda n: n * factor

# Create multiplier variables using the multiplier function
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# Test each new multiplier variable with a sample value
print(quadrupler(2))
print(quintupler(2))
print(sextupler(2))
print(septupler(2))
print(octupler(2))
print(nonupler(2))
print(decupler(2))

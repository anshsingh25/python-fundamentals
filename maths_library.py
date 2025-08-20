import math

#constant
print(math.pi)       # 3.141592...
print(math.e)        # 2.718281...
print(math.tau)      # 6.283185...
print(math.inf)      # infinity
print(math.nan)      # Not a Number

#Arithmetics
print(math.sqrt(16))    # 4.0
print(math.pow(2, 3))   # 8.0 (always float)
print(2 ** 3)           # 8 (Python built-in, faster sometimes)
print(math.fabs(-5))    # 5.0 (always positive float)

#factorial and combinatorics
print(math.factorial(5))  # 120
print(math.comb(5, 2))    # 10 (nCr)
print(math.perm(5, 2))    # 20 (nPr)

#trigonometry
print(math.sin(math.radians(90)))  # 1.0
print(math.cos(math.radians(0)))   # 1.0
print(math.tan(math.radians(45)))  # 0.9999 ≈ 1

print(math.degrees(math.pi))  # 180
print(math.radians(180))      # 3.14159

#logarithms
print(math.log(10))       # ln(10)
print(math.log10(1000))   # log base 10 = 3
print(math.log2(8))       # log base 2 = 3



print(math.ceil(4.3))  # 5
print(math.floor(4.7)) # 4
print(math.trunc(4.7)) # 4 (just removes decimal part)
print(math.isfinite(100))    # True
print(math.isinf(math.inf))  # True
print(math.isnan(math.nan))  # True

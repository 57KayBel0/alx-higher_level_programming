#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

sum_result = add(a, b)
diff_result = sub(a, b)
prod_result = mul(a, b)
quot_result = div(a, b)

print("10 + 5 =", sum_result)
print("10 - 5 =", diff_result)
print("10 * 5 =", prod_result)
print("10 / 5 =", quot_result)

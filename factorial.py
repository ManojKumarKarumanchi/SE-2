"""Program to compute the factorial # factorial.py
"""

import time

final_list = []

def factorial(var_n):
    """docstring for factorial
    """
    time.sleep(.1)
    fact = 1
    for i in range (1, var_n + 1):
        fact = fact * i
    return fact

def sum_factorial():
    """docstring for sum_factorial
    """
    for i in range(50):
        final_list.append(factorial(i))
        result=sum(final_list)
        print("Final SUM is ", result)
    return result

if __name__ == "__main__":
    sum_factorial()
   # Final SUM = 620960027832821612639424806694551108812720525606160920420940314

#Broadcasting
"""
Broadcasting is how numpy performs arithmetic operation between arrays with different shapes.
The smaller array is broadcasted across the larger one

Advantages- much faster than for loops.
          - Don't create new copies in memory
          - Efficient algorithm implementation

Rules- ONe of the dimensions is 1
     - Trailing dimensions match.
"""

#Usage
import numpy as np

np_arr = np.array([[2,3], [4, 10]])

np_arr_broad = np_arr*5
print(np_arr_broad)

np_five = np.array([[5,5], [5,5]])
np_arr_nobroad = np_arr*np_five
print(np_arr_nobroad)

#both give the same output.
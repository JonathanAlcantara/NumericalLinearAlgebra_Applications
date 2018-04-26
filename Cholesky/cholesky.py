# Copyright 2018 - Jonathan Alcantara e Osmar Fernandes

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from math import pow
from math import sqrt


def cholesky(A):
    # if not np.all(np.linalg.eigvals(A) > 0):
    #     print "Matriz nao e Positiva Definida"
    #     return false


    L = [[0.0] * len(A) for i in range(len(A))]

    for row in range(len(A)):
        sum_row = 0
        for k in range(row):
            sum_row += pow(L[row][k], 2)

        L[row][row] = sqrt(A[row][row] - sum_row)
        print('%s, %s: %s' % (row+1, row+1, L[row][row]))
        for column in range(row + 1, len(A)):
            sum_column = 0
            for k in range(row):
                sum_column += L[row][k]*L[column][k]

            L[column][row] = (A[row][column] - sum_column)/L[row][row]
            print('%s, %s: %s' % (row+1, column+1, L[column][row]))

    A = np.array(A)
    L = np.array(L)
    transposed_L = np.transpose(L)

    print '\nA : \n', A
    print '\nL : \n', L
    print '\nL_T :\n', transposed_L

    return A, L, transposed_L

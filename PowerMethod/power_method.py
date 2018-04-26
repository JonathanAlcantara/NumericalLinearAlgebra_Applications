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

tolerance = 0.00001
A = [[1,0.2,0],[0.2,1,0.5],[0,0.5,1]]
X = [1]*len(A[0])

new_X = list(X)
eigenvalue_candidate = 1
solution_residue = eigenvalue_candidate

while solution_residue > tolerance:
   X = np.matmul(A,X)

   solution_residue = abs(X[0] - eigenvalue_candidate)/abs(X[0])
   eigenvalue_candidate = X[0]

   for X_element in range(len(X)):
      X[X_element] = X[X_element]/float(eigenvalue_candidate)

print('Largest Eigenvalue: ', eigenvalue_candidate)
print('Associate Eigenvector: ', list(X))
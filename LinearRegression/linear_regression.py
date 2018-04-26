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

X_vector = [1, 2, 3]
Y_vector = [2, 3.5, 6.5]

regressor_matrix = []

for x_element in X_vector:
    regressor_matrix.append([1,x_element])

transposed_regressor_matrix = np.transpose(regressor_matrix)

coefficient_vector = np.matmul(
        np.matmul(np.linalg.inv(
            np.matmul(transposed_regressor_matrix,regressor_matrix)), 
                transposed_regressor_matrix),
        Y_vector)


print 'X vector: ', X_vector
print 'Y vector: ', Y_vector
print 'Coefficients Vector (B): ', list(coefficient_vector)
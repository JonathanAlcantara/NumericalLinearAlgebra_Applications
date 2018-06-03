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

tolerance = 0.00000001
iterations_limit = 10000

def multi_newton(x0_vector, f_vector, jacobian_vector):

    x_vector = x0_vector
    for iteration in range(iterations_limit):

        jacobian_current_values = jacobian_vector(x_vector)
        function_current_values = f_vector(x_vector)
        
        delta_x = -1*(np.matmul(np.linalg.inv(jacobian_current_values),
                                function_current_values))

        x_vector = np.add(x_vector, delta_x)

        if(np.linalg.norm(delta_x)/np.linalg.norm(x_vector) \
            < tolerance):
            return x_vector

    return "Convergence not reached"

def f_vector(x_vector):
    return [[x_vector[0][0] + 2*x_vector[1][0] - 2.0], 
            [pow(x_vector[0][0], 2) + 4*pow(x_vector[1][0], 2) - 4]]

def jacobian_vector(x_vector):
    return [[1, 2], [2*x_vector[0][0], 8*x_vector[1][0]]]

print(multi_newton([[2], [3]], f_vector, jacobian_vector))

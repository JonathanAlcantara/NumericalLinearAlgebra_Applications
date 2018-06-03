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

def newton(x0, f, f_derivative):

    x_previous = x0
    for iteration in range(iterations_limit):
        x_current = x_previous - f(x_previous)/f_derivative(x_previous)
        if(abs(x_current - x_previous) < tolerance):
            return x_current

        x_previous = x_current

    return x_current

def f(x):
    return pow(x, 2) - 4*np.cos(x);

def f_derivative(x):
    return 2*x + 4*np.sin(x)

print(newton(10.0, f, f_derivative))

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
pace = 0.001

def secant(x0, f):
    x_previous = x0
    x_current = x_previous + pace
    func_previous_value = f(x0)

    for iteration in range(iterations_limit):
        func_current_value = f(x_current)
        x_next = x_current - func_current_value*\
                                ((x_current - x_previous)/\
                                (func_current_value - func_previous_value))
        if(abs(x_next - x_current) < tolerance):
            return x_current
        x_previous = x_current
        x_current = x_next
        func_previous_value = func_current_value

    return x_current

def f(x):
    return pow(x, 2) - 4*np.cos(x);

print(secant(10.0, f))

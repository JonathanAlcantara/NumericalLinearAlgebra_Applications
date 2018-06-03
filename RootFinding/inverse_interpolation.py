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

def update_xs(x1, x2, x3, x_current, f):
    x_list = [x1, x2, x3]
    f_list = [abs(f(x1)), abs(f(x2)), abs(f(x3))]

    largest_index = f_list.index(max(f_list))
    x_list[largest_index] = x_current
    x_list.sort()

    return x_list


def inverse_interpolation(x1, x2, x3, f):
    x_previous = pow(10, 36)
    for iteration in range(iterations_limit):
        y1 = f(x1)
        y2 = f(x2)
        y3 = f(x3)
        x_current = (y2*y3*x1)/((y1 - y2)*(y1 - y3)) +\
                    (y1*y3*x2)/((y2 - y1)*(y2 - y3)) +\
                    (y1*y2*x3)/((y3 - y2)*(y3 - y1))
        if(abs(x_current - x_previous) < tolerance):
            return x_current
        else:
            [x1, x2, x3] = update_xs(x1, x2, x3, x_current, f)
            x_previous = x_current

    return x_current

def f(x):
    return pow(x, 2) - 4*np.cos(x);

print(inverse_interpolation(3.0, 5.0, 10.0, f))

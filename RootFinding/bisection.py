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

tolerance = 0.00000001

def bisection(a, b, f):

    while abs(b - a) > tolerance:
        x_current = (a+b)/2.0
        func_current_value = f(x_current)

        if(func_current_value > 0.0):
            b = x_current
        else:
            a = x_current

    return x_current


def f(x):
    return x - 1;

print(bisection(-10, 10, f))

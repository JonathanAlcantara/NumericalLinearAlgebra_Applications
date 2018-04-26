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
from Cholesky.cholesky import cholesky
from PowerMethod.power_method import power_method
from LinearRegression.linear_regression import linear_regression
from LU.LU import LU

from csv import reader

first_argument = []
second_argument = []

with open('input.csv','r') as csvfile:
    spamreader = reader(csvfile, delimiter=',')

    for line in spamreader:
        if len(line) == 0:
            break
        first_argument.append(line)

    for line in spamreader:
      second_argument.append(line)

cholesky(np.array(first_argument, float))
power_method(np.array(first_argument, float))
linear_regression(np.array(first_argument, float), np.array(second_argument, float))
LU(np.array(first_argument, float), np.array(second_argument, float))
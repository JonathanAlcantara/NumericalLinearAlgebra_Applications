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

def integrate(points, a, b, type):
  if type == "gauss":
    L = b-a
    if points > 10:
            print("Numero de pontos de integração indisponivel.")
    
    if points == 2:
        peso = np.array([1, 1])
        vectorx = np.array([-0.577, 0.577])
    elif points == 3:
        peso = np.array([0.889, 0.556, 0.556])
        vectorx = np.array([0, -0,775, 0.775])
    elif points == 4:
        peso = np.array([0.652, 0.652, 0.348, 0.348])
        vectorx = np.array([-0.340, 0.340, -0.861, 0.861])
    elif points == 5:
        peso = np.array([0.569, 0.477, 0.477, 0.237, 0.237])
        vectorx = np.array([0, -0.538, 0.538, -0.906, 0.906])
    elif points == 6:
        peso = np.array([0.361, 0.361, 0.468, 0.468, 0.171, 0.171])
        vectorx = np.array([0.661, -0.661, -0.239, 0.239, -0.932, 0.932])
    elif points == 7:
        peso = np.array([0.462, 0.382, 0.382, 0.280, 0.280, 0.129, 0.129])
        vectorx = np.array([0, 0.406, -0.406, -0.742, 0.742, -0.949, 0.949])
    elif points == 8:
        peso = np.array([0.363, 0.363, 0.314, 0.314, 0.222, 0.222, 0.101, 0.101])
        vectorx = np.array([-0.183, 0.183, -0.526, 0.526, -0.797, 0.797, -0.960, 0.960])
    elif points == 9:
        peso = np.array([0.330, 0.181, 0.181, 0.081, 0.081, 0.312, 0.312, 0.261, 0.261])
        vectorx = np.array([0, -0.836, 0.836, -0.968, 0.968, -0.324, 0.324, -0.613, 0.613])
    elif points == 10:
        peso = np.array([0.296, 0.296, 0.269, 0.269, 0.219, 0.219, 0.149, 0.149, 0.067, 0.067])
        vectorx = np.array([-0.149, 0.149, -0.433, 0.433, -0.679, 0.679, -0.865, 0.865, -0.974, 0.974])

    function = np.zeros((points, 1))
    for i in range(points):
        function[i] = f((a + b + L*vectorx[i])/2)
    return (np.dot(function.T, peso)*(b-a))[0]/2
  else:
    x = np.zeros(points)
    
    if points == 1:
      x[0] = (a+b)/2
    else:
      delta = (b-a)/(points - 1)
      for i in range(points):
        x[i] = a + i*delta
      
      vandermonde = np.zeros((points, points))
      function = np.zeros((points, 1))
      matrixB = np.zeros((points, 1))
      
      for i in range(points):
        vandermonde[i] = np.power(x, i)
        matrixB[i] = ((b**(i+1)) - (a**(i+1))) / (i+1)
        function[i] = f(x[i])
      
      pesos = np.linalg.solve(vandermonde, matrixB)
      
      return np.dot(function.T, pesos)[0,0]
      
    
    
def f(x):
  return (2 + x + 2*pow(x,2))

result = integrate(2, 1, 3, "gauss")
print(result)
  

  

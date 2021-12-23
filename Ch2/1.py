import numpy as np
import torch

print("=====================================", '\n')
t = np.array([0., 1., 2., 3., 4., 5., 6.])
print(t)
print("Rank of t: ", t.ndim)
print('Shape of t: ', t.shape) # (7,) mean 1*7 vector

print('t[0] t[1] t[-1] = ', t[0], t[1], t[-1])
print('t[2:5] t[4:-1] = ', t[2:5], t[4:-1]) # start:end -> not include end
print('t[:2] t[3:] = ', t[:2], t[3:])

print('\n', "=====================================", '\n')

t2 = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
print(t2)
print('Rank  of t: ', t2.ndim)
print('Shape of t: ', t2.shape) # 4 * 3 = row * column

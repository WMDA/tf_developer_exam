import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')


tensor=tf.ones([3,3,3])

#Getting output from tensors

print('\nDatatye:', tensor.dtype)
print('\nNumber of dimensions:', tensor.ndim)
print('\nShape of tensor:', tensor.shape)

for i in list(range(tensor.ndim)):
    print(f'\nElements of tensor along {i} axis:',tensor.shape[i])

print('\nTotal Elements of tensor:',tf.size(tensor).numpy())

#Getting elements from a tensor. Exactly like list indexing
print('\nGet 2nd element from tensors:', tensor[:2,:2,:2])
print('\nIgnoring last dimension', tensor[:2,:2,:])
import tensorflow as tf
import numpy as np
import warnings
warnings.filterwarnings('ignore')
print('tf version',tf.__version__)

'''
Creating tensors using constant (immutable), Variable (mutable) and random.
'''

#Creating tensors with tf.constant()

#Create a scalar
scalar = tf.constant(7)
print('\nSCALAR\nScalar info:', scalar, '\nScalar dimensions', scalar.ndim)

#Create a vector
vector = tf.constant([10,10])
print('\nVECTOR\nvector info:', vector,'\nvector dimensions', vector.ndim)

#Create a matrix
matrix = tf.constant([[10,10],
                   [10,10]])
print('\nMATRIX\nMatrix info:', matrix,'\nMatrix dimensions:', matrix.ndim)

#Matrix as float as this
matrix = tf.constant([[10,10],
                   [10,10]],dtype=tf.float16)
print('\nMATRIX\nMatrix info:', matrix,'\nMatrix dimensions:', matrix.ndim)

#Create a tensor
tensor = tf.constant([[[3,2,4],
                      [4,5,10]],
                      [[4,50,100],
                      [300,400,400]],
                      [[400,40,8],
                       [600,700,800]]
                      ])

print('\nTensor\nTensor info:', tensor,'\nTensor dimensions:', tensor.ndim)

#Creating tensors with tf.variable(). Changeable

tensor_var= tf.Variable([[[3,2,4],
                      [4,5,10]],
                      [[4,50,100],
                      [300,400,400]],
                      [[400,40,8],
                       [600,700,800]]
                      ])

print('\ntensor variable info:', tensor_var)

tensor_var= tensor_var[0,0,0].assign(10)
print('\nUpdated tf variable:',tensor_var)

#Create random tensors from uniform distribution
ran= tf.random.Generator.from_seed(seed=1) #THis sets the global seed and makes sure that random tensors are always the same each time the programme is run.
ran= ran.normal(shape=(3,3,3))
print('random tensor:', ran)

#Shuffle order of tensor. Shuffles data so order doesn't affect learning.
#Global seed means the tensor will be shuffled the same way each
shuffle= tf.random.shuffle(ran,seed=1)
print('\nshuffled tensor:',ran)

#Tensor of all ones/zeros with tf.

onestf=tf.ones([3,3,3])
zerostf=tf.zeros([3,3,3])

print(onestf,zerostf)

#Numpy to tensor. Tensors can be ran on GPU faster than numpy arrays

np_array=np.arange(1,25)
tensor_from_numpy=tf.constant(np_array,shape=(2,3,4)) #shape must equal the number of elements in original array.
print('\nTensor from numpy:',tensor_from_numpy)
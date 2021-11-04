#!/usr/bin/env python
# coding: utf-8

# ## Basics 

# ### Let's Start

# - The main difference between tensors and NumPy arrays is that tensors can be used on GPUs (graphical processing units) and TPUs (tensor processing units).
# - The number of dimensions of a tensor is called its rank. A scalar has rank $0$, a vector has rank $1$, a matrix is rank $2$, a tensor has rank $n$.
# - There are $2$ ways of creating tensors. `tf.Variable()` and `tf.constant()` the difference being tensors created with `tf.constant()` are immutable, tensors created with `tf.Variable()` are mutable. `any_tensor[2].assign(7)` can be used to change a value of a specific element in the tensor, same would fail for `tf.constant()`.
# - There are other ways of creating tensors examples being `tf.zeros` or `tf.ones`. You can also convert numpy arrays into tensors.
# - Tensors can also be indexed just like Python lists.
# - You can an extra dimension by using `tf.newaxis` or `tf.expand_dims`
# - `tf.reshape()`,`tf.transpose()` allows us to reshape a tensor
# - Data type of a tesnor can be changed with `tf.cast(t1, dtype=tf.float16)`
# - You can squeeze a tensor to remove single-dimensions (dimensions with size 1) using `tf.squeeze()`.

# In[1]:


# Some common commands are as follows
import tensorflow as tf
print("Check TF version: ",tf.__version__)

t1 = tf.constant([[10., 7.],
                [3., 2.],
                [8., 9.]], dtype=tf.float16) # by default TF creates tensors with either an int32 or float32 datatype.

print("Access a specific feature of the tensor, in this case shape of t1: ",t1.shape)
print("Size of t1: ", tf.size(t1))
print("Datatype of every element:", t1.dtype)
print("Number of dimensions (rank):", t1.ndim)
print("Shape of tensor:", t1.shape)
print("Elements along axis 0 of tensor:", t1.shape[0])
print("Elements along last axis of tensor:", t1.shape[-1])
print("Total number of elements:", tf.size(t1).numpy()) # .numpy() converts to NumPy array
print("Details of the tensor: ",t1)

print("Index tensors: ", t1[:1,:])


# In[27]:


import tensorflow as tf

# Math operations

t1 = tf.constant([[10., 7.],
                [3., 2.],
                [8., 9.]], dtype=tf.float16) # by default TF creates tensors with either an int32 or float32 datatype.

print("Sum: ",t1+10)
print("Substraction: ",t1-10)
print("Multiplication: ",t1*10, tf.multiply(t1, 10))
print("Matrix Multiplication: ",t1 @ tf.transpose(t1)) # can also be done with tf.tensordot()

# Aggregation functions

print("Max: ", tf.reduce_max(t1)) # same or min, mean
print("Sum: ", tf.reduce_sum(t1))
print("Max Position: ", tf.argmax(t1)) # same or min


# ### Random

# Randomness is often used in deep learning, be it initializing weights in a Neural Network or shuffling images while feeding data to the model. 

# In[5]:


random_1 = tf.random.Generator.from_seed(35) # setting seed ensures reproducibility
random_1 = random_1.normal(shape = (3,2))
print("Generating tensor from a normal distribution: ", random_1)
print("Shuffling the elements of the tesnor: ", tf.random.shuffle(random_1))


# 

# In[ ]:





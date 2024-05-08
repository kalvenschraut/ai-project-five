import tensorflow as tf
import numpy as np
# Create a simple function
def function(x, y):
  return x ** 2 + y

x = tf.constant(np.arange(0, 10))
y = tf.constant(np.arange(10, 20))
function(x, y)

@tf.function
def tf_function(x, y):
  return x ** 2 + y

tf_function(x, y)

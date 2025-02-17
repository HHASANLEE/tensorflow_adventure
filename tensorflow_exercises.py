import tensorflow as tf

#Task 1

scalar = tf.constant(1)
vector = tf.constant([1,2,3])
matrix = tf.constant([[1,2,3],
                     [4,5,6],
                     [6,7,8]])
tensor = tf.constant([[[1,2,3],
                      [3,2,1]],
                     [[4,5,6],
                      [6,5,4]],
                      [[7,8,9],
                       [9,8,7]]])
scalar, vector, matrix, tensor

#Task 2

tensor.shape, tensor.ndim, tf.size(tensor)

#Task 3

tensor1 = tf.random.uniform(shape=[5,300], minval=0, maxval=1)
tensor2 = tf.random.uniform(shape=[5,300], minval=0, maxval=1)
tensor1, tensor2

#Task 4

tensor1 = tf.random.uniform(shape=[5, 300], minval=0, maxval=1)
tensor2 = tf.random.uniform(shape=[300, 5], minval=0, maxval=1)
multiply = tf.matmul(tensor1, tensor2)
multiply

#Task 5

tensor1 = tf.random.uniform(shape=[300, 5], minval=0, maxval=1)
tensor2 = tf.random.uniform(shape=[300, 5], minval=0, maxval=1)
tensor3 = tf.tensordot(tensor1, tf.transpose(tensor2), axes=1)
tensor3

#Task 6

t1 = tf.random.uniform(shape=[224, 223, 3], minval=0, maxval=1)
t2 = tf.random.uniform(shape=[224, 223, 3], minval=0, maxval=1)
t1
t2

#Task 7

min_t1 = tf.reduce_min(t1)
max_t1 = tf.reduce_max(t1)
min_t2 = tf.reduce_min(t2)
max_t2 = tf.reduce_max(t2)
min_t1.numpy(), max_t1.numpy(), min_t2.numpy(), max_t2.numpy()

#Task 8

tensor1 = tf.random.normal(shape=[1,224,224,3])
tensor2 = tf.reshape(tf.squeeze(tensor1), shape=[224,224,3])

tensor1.shape, tensor2.shape

#Task 9

tensor0 = tf.constant([12,3,32,45,4,5,6,47,76,6])

print(tf.argmax(tensor0).numpy())

#Task 10

one_hot_tensor = tf.one_hot(tensor0, depth=4)
one_hot_tensor

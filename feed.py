import tensorflow as tf

x1 = tf.placeholder("float", None)
x2 = tf.placeholder("float", None)
y = x1 * 2 + x2

with tf.Session() as session:
    result = session.run(y, feed_dict={x1: [1, 2, 3],x2:[2,4,6]})
    print(result)
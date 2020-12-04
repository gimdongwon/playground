import tensorflow.compat.v1 as tf

with tf.compat.v1.Session() as sess:
    x_data = [1,2,3]
    y_data = [1,2,3]

    W = tf.Variable(tf.random_normal([1]), name='weight')
    X = tf.placeholder(tf.float32)
    Y = tf.placeholder(tf.float32)

    hypothesis = X * W

    cost = tf.reduce_sum(tf.square(hypothesis - Y))

    learing_rate = 0.1
    gradient = tf.reduce_mean((W * W - Y) * X)
    descent = W - learing_rate * gradient
    update = W.assign(descent)

    sess = tf.Session()

    sess.run(tf.global_variables_initializer())
    for step in range(21):
        sess.run(update, feed_dict={X: x_data, Y: y_data})
        print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))

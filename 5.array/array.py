import tensorflow as tf
data1 = tf.placeholder(tf.float32)
data2 = tf.placeholder(tf.float32)
dataAdd = tf.add(data1,data2)

with tf.Session() as sess:
	print(sess.run(dataAdd, feed_dict={data1:6,data2:2}))
print("end")


import tensorflow as tf
data3= tf.constant([[1,2],\
		    [3,4],\
		    [5,6]])
print(data3.shape)
with tf.Session() as sess:
	print(sess.run(data3[1]))		
	print(sess.run(data3[:,1]))
	print(sess.run(data3[1,1]))


import tensorflow as tf
data1 = tf.constant([[1,2],[3,4]])
data2 = tf.constant([[3],[4]])
matMul = tf.matmul(data1,data2)

data3= tf.constant([[1,2],\
		    [3,4],\
		    [5,6]])
print(data3.shape)

data3 =tf.zeros([3,3])
data4 = tf.ones([4,4])
data5 = tf.fill([2,3],10)
data6 = tf.linspace(0.0,10.0,11)
data7 = tf.random_uniform([2,4],10)
with tf.Session() as sess:
	print(sess.run(matMul))		
	print(sess.run(data3))	
	print(sess.run(data4))	
	print(sess.run(data5))	
	print(sess.run(data6))	
	print(sess.run(data7))





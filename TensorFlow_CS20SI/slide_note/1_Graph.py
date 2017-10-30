import tensorflow as tf

#creates nodes in a graph
g = tf.Graph() # user created graph ,  tf.get_default_graph() to hande default graph
with g.as_default():
	x = 2
	y = 3
	add_op = tf.add(x,y)
	mul_op = tf.multiply(x,y)
	useless = tf.multiply(x,add_op)
	pow_op = tf.pow(add_op,mul_op)

#define session
with tf.Session(graph=g) as sess: # with statement use the session for the following statement then close when done
	# add this line to use TensorBoard.
	writer = tf.summary.FileWriter('./graphs', sess.graph)
	#run result
	z,not_useless = sess.run([mul_op,useless])
	print z,not_useless

writer.close() # close the writer when you're done using it

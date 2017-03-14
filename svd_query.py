import time
from collections import deque

import numpy as np
import tensorflow as tf
from six import next
from tensorflow.core.framework import summary_pb2
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file

import dataio
import ops

np.random.seed(13575)

BATCH_SIZE = 1000
USER_NUM = 6040
ITEM_NUM = 3952
DIM = 15
EPOCH_MAX = 100
DEVICE = "/cpu:0"


def clip(x):
    return np.clip(x, 1.0, 5.0)


def make_scalar_summary(name, val):
    return summary_pb2.Summary(value=[summary_pb2.Summary.Value(tag=name, simple_value=val)])




if __name__ == '__main__':
    #zeros= tf.Variable(tf.zeros([1]),name="zeros")
    infer, regularizer = ops.inference_svd(user_batch, item_batch, user_num=USER_NUM, item_num=ITEM_NUM, dim=DIM,
                                           device=DEVICE)
    init_op = tf.global_variables_initializer()
    #print_tensors_in_checkpoint_file(file_name="/tmp/tfrecomm.ckpt", tensor_name='')
    #df_train, df_test = get_data()
    #saver=tf.train.Saver()
    with tf.Session() as sess:
       new_saver = tf.train.import_meta_graph("tfrecomm.meta")
       new_saver.restore(sess, tf.train.latest_checkpoint('./'))
 
       #saver.restore(sess,"/tmp/tfrecomm.ckpt")
       users=[1]
       items=[1]
       pred_batch = sess.run(infer, feed_dict={user_batch: users,item_batch: items})
       print (pred_batch)
       print("Done!")

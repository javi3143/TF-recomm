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
USER_NUM = 259137
ITEM_NUM = 165201
DIM = 15
EPOCH_MAX = 100
DEVICE = "/cpu:0"


def clip(x):
    return np.clip(x, 1.0, 5.0)


def make_scalar_summary(name, val):
    return summary_pb2.Summary(value=[summary_pb2.Summary.Value(tag=name, simple_value=val)])

def get_movies():
    df = dataio.read_movies("/tmp/movielens/ml-latest/movies.csv", sep=",")
    rows = len(df)
    return df, rows	



if __name__ == '__main__':
    #zeros= tf.Variable(tf.zeros([1]),name="zeros")
    user_batch = tf.placeholder(tf.int32, shape=[None], name="id_user")
    item_batch = tf.placeholder(tf.int32, shape=[None], name="id_item")
    init_op = tf.global_variables_initializer()
    #print_tensors_in_checkpoint_file(file_name="/tmp/tfrecomm.ckpt", tensor_name='')
    #df_train, df_test = get_data()
    #saver=tf.train.Saver()
    with tf.Session() as sess:
       new_saver = tf.train.import_meta_graph("tfrecomm.meta")
       new_saver.restore(sess, tf.train.latest_checkpoint('./'))
       sess.run(tf.global_variables_initializer())
       print ("Get Movies Data")
       moviefile,rows = get_movies()
       graph = tf.get_default_graph()
       infer = graph.get_tensor_by_name("svd_inference:0")
       
       user_batch = graph.get_tensor_by_name("id_user:0")
       item_batch = graph.get_tensor_by_name("id_item:0")
       movies=list(range(len(moviefile)))
       infer = graph.get_tensor_by_name("svd_inference:0")
       users=[1]
       feed_dict={user_batch: users,item_batch: movies}       
       pred_batch = sess.run(infer, feed_dict)

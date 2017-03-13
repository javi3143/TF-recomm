import time
from collections import deque

import numpy as np
import tensorflow as tf
from six import next
from tensorflow.core.framework import summary_pb2

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


def get_data():
    df = dataio.read_process("/tmp/movielens/ml-1m/ratings.dat", sep="::")
    rows = len(df)
    df = df.iloc[np.random.permutation(rows)].reset_index(drop=True)
    split_index = int(rows * 0.9)
    df_train = df[0:split_index]
    df_test = df[split_index:].reset_index(drop=True)
    return df_train, df_test



if __name__ == '__main__':
    zeros= tf.Variable(tf.zeros([1]),name="zeros")
    init_op = tf.global_variables_initializer()
    df_train, df_test = get_data()
    saver=tf.train.Saver()
    with tf.Session() as sess:
       saver.restore(sess,"/tmp/tfrecomm.ckpt")
       users=[1]
       items=[1]
       pred_batch = sess.run(infer, feed_dict={user_batch: users,item_batch: items})
       print (pred_batch)
       print("Done!")

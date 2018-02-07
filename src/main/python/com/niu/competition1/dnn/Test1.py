#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/06 20:05
# @Author  : niuliangtao
# @Site    : 
# @File    : Test1.py
# @Software: PyCharm
# encoding=utf-8


from __future__ import print_function

__author__ = 'freedom'
import tensorflow as tf
import pandas as pd


class example1:
    def __init__(self, data_train, epoch=100000
                 , rate=0.00025, batch_size=20):
        self.data_train = data_train
        self.epoch = epoch
        self.rate = rate
        self.batch_size = batch_size
        self.feature_size = 2
        self.feature_size = len(data_train.columns) - 1

    def get_batch(self, index):
        if index == -200:
            print("nothing")
        columns = train_data.columns
        columns.drop('sale_quantity')
        train_x = self.data_train.loc[:, columns].as_matrix()
        train_y = self.data_train.loc[:, 'sale_quantity'].as_matrix()
        return train_x, train_y

    def train(self):
        xs = tf.placeholder(tf.float32, [None, self.feature_size])
        ys = tf.placeholder(tf.float32, [None, 1])

        weight1 = tf.Variable(tf.random_normal([self.feature_size]))  # 生成随机权重
        biases = tf.Variable(tf.random_normal([1]))
        pred = tf.multiply(weight1, xs) + biases

        loss = tf.reduce_sum(tf.pow(pred - ys, 2))
        optimizer = tf.train.GradientDescentOptimizer(self.rate).minimize(loss)

        sess = tf.Session()
        sess.run(tf.global_variables_initializer())

        for index in range(self.epoch):
            train_x, train_y = self.get_batch(index)

            sess.run(optimizer, {xs: train_x, ys: train_y})
            print('loss is ', sess.run(loss, {xs: train_x, ys: train_y}))


if __name__ == "__main__":
    train_path = "../data/data/data_cnn1.csv"
    train_data = pd.read_csv(train_path, low_memory=False)
    train_data.fillna
    print(train_data)
    example = example1(train_data)

    example.train()

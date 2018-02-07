在很多机器学习和深度学习的应用中，我们发现用的最多的优化器是 Adam，为什么呢？

下面是 TensorFlow 中的优化器：

关于深度学习优化器 optimizer 的选择，你需要了解这些

详情参见：https://www.tensorflow.org/api_guides/python/train

在 keras 中也有 SGD，RMSprop，Adagrad，Adadelta，Adam 等，详情：

https://keras.io/optimizers/

我们可以发现除了常见的梯度下降，还有 Adadelta，Adagrad，RMSProp 等几种优化器，都是什么呢，又该怎么选择呢？

在 Sebastian Ruder 的这篇论文中给出了常用优化器的比较，今天来学习一下： 

原文链接：https://arxiv.org/pdf/1609.04747.pdf

本文将梳理：

● 每个算法的梯度更新规则和缺点

● 为了应对这个不足而提出的下一个算法

● 超参数的一般设定值

● 几种算法的效果比较

● 选择哪种算法

  优化器算法简述
首先来看一下梯度下降最常见的三种变形 BGD，SGD，MBGD， 

这三种形式的区别就是取决于我们用多少数据来计算目标函数的梯度， 

这样的话自然就涉及到一个 trade－off，即参数更新的准确率和运行时间。

1. Batch gradient descent
梯度更新规则: 

BGD 采用整个训练集的数据来计算 cost function 对参数的梯度： 

关于深度学习优化器 optimizer 的选择，你需要了解这些

缺点: 

由于这种方法是在一次更新中，就对整个数据集计算梯度，所以计算起来非常慢，遇到很大量的数据集也会非常棘手，而且不能投入新数据实时更新模型

for i in range(nb_epochs):

  params_grad = evaluate_gradient(loss_function, data, params)

  params = params - learning_rate * params_grad

我们会事先定义一个迭代次数 epoch，首先计算梯度向量 params_grad，然后沿着梯度的方向更新参数 params，learning rate 决定了我们每一步迈多大。

Batch gradient 
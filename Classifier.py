#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sklearn.naive_bayes import MultinomialNB        # 多项式贝叶斯算法
from sklearn.linear_model import LogisticRegression  # 逻辑回归算法
from sklearn.neighbors import KNeighborsClassifier   # K近邻分类算法
from sklearn.svm import SVC                          # SVC
from sklearn.tree import DecisionTreeClassifier      # 决策树
from sklearn.neural_network import MLPClassifier     # MLP
from sklearn import metrics
from Tools import readbunchobj
from sklearn.utils import resample

# 导入训练集
trainpath = "E:/1-学习/NLP/chinese_text_classification-master/train_word_bag/tfdifspace.dat"
train_set = readbunchobj(trainpath)

# 导入测试集
testpath = "E:/1-学习/NLP/chinese_text_classification-master/test_word_bag/testspace.dat"
test_set = readbunchobj(testpath)

# 计算分类精度：
def metrics_result(actual, predict):
    print('accuracy:{0:.4f}'.format(metrics.precision_score(actual, predict, average='weighted')))
    print('recall:{0:0.4f}'.format(metrics.recall_score(actual, predict, average='weighted')))
    print('f1-score:{0:.4f}'.format(metrics.f1_score(actual, predict, average='weighted')))

def shuffle_dataset():
    train_set.tdm, train_set.label = resample(train_set.tdm, train_set.label, random_state=0)  
    test_set.tdm, test_set.label = resample(test_set.tdm, test_set.label, random_state=0)
    print('ok shuffle')

def different(label, filenames, predicted):
    for flabel, file_name, expct_cate in zip(label, filenames, predicted):
        if flabel != expct_cate:
            print(file_name, ": 实际类别:", flabel, " -->预测类别:", expct_cate)

shuffle_dataset()

# 多项式贝叶斯:
# 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)
# different(test_set.label, test_set.filenames, clf.predict(test_set.tdm))  # 显示预测错误的文章的预测类别与实际类别
metrics_result(test_set.label, clf.predict(test_set.tdm))
print("多项式贝叶斯预测完毕")

# 逻辑回归:
lgr = LogisticRegression(n_jobs=-1).fit(train_set.tdm, train_set.label)
# different(test_set.label, test_set.filenames, lgr.predict(test_set.tdm))
metrics_result(test_set.label, lgr.predict(test_set.tdm))
print("逻辑回归预测完毕")

# K近邻:
knc = KNeighborsClassifier(n_jobs=-1).fit(train_set.tdm, train_set.label)
# different(test_set.label, test_set.filenames, knc.predict(test_set.tdm))
metrics_result(test_set.label, knc.predict(test_set.tdm))
print("K近邻预测完毕")

# SVC
svc = SVC().fit(train_set.tdm, train_set.label)
# different(test_set.label, test_set.filenames, svc.predict(test_set.tdm))
metrics_result(test_set.label, svc.predict(test_set.tdm))
print("SVC预测完毕")

# 决策树
dct = DecisionTreeClassifier().fit(train_set.tdm, train_set.label)
# different(test_set.label, test_set.filenames, dct.predict(test_set.tdm))
metrics_result(test_set.label, dct.predict(test_set.tdm))
print("决策树预测完毕")

# MLP
nn = MLPClassifier(hidden_layer_sizes=(100, 100, ), max_iter=200).fit(train_set.tdm, train_set.label)
# different(test_set.label, test_set.filenames, nn.predict(test_set.tdm))
metrics_result(test_set.label, nn.predict(test_set.tdm))
print("MLP预测完毕")
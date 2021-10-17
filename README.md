# 中文法律文书分类器

该篇借鉴了博客《[Python中文文本分类](http://blog.csdn.net/github_36326955/article/details/54891204)》的源代码.

### 项目背景
- 本项目来自自然语言处理课程的课程作业，作业要求如下：
1. 从[裁判文书网](https://wenshu.court.gov.cn/)上分类采集10000+条结案文书，至少有5个类别，如交通肇事类等。
2. 将采集到的文书分词并生成核心词集，可以采用TF-IDF等方法，用8000+文书训练、2000+测试，test分类正确率

### 环境
- python3.8 (用来爬文书的playwright有python版本限制) / pyhton3.6 (已有数据的话也可以用python3.6直接跑)

### 安装
- jieba
- pickle
- playwright
- sklearn

### 使用
1. playwright爬数据：python playwright.py
    - playwright可以录制网页操作对应的代码，本项目仅提供了裁判文书网的录制代码（裁判文书网真的很难爬，像登录等步骤只能手动来，playwright模拟登不上去的）
    - 另外裁判文书网下载下来的数据是doc文件，不能直接使用，需要使用VBA来转换成txt格式，可以参考https://www.zhihu.com/question/382831071/answer/1142716625 的方法
2. 分词：python corpus_segment.py
3. 建立词集：python corpus2Bunch.py
4. TF-IDF处理：python TFIDF_space.py
5. 预测分类结果：python Classifier.py
    - 原博客中作者使用的是多项式贝叶斯算法,本项目在同学的帮助下增加了逻辑回归、K近邻分类、SVC、决策树等其他方法

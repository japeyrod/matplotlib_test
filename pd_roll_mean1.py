# -*- coding: utf-8 -*-
import os, sys

if len(sys.argv) == 2:
    i = sys.argv[1]
else:
    print
    'usage: pd_roll_mean1.py i '
    sys.exit(1)

import pandas as pd

# dataFrame  第6章 数据加载   读写文本格式的数据 第167页
df = pd.read_csv('/python/66001_.txt', parse_dates=True, index_col=0)

df.head()  # 预览前5行数据
df.describe()  # 数据基本统计量

import matplotlib.pyplot as plt

# 加这个两句 可以显示中文
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

jz = 'jz' + str(i)
df[jz].plot(figsize=(12, 6), grid=True, legend=jz, label='66001' + str(i))
# 画30日移动平均线
pd.rolling_mean(df[jz], 30).plot(grid=True)
plt.show()

# -*- coding:utf-8 -*-
# @Time : 2020/4/2 10:01
# @Author : a2htray
# @File : PSO.py
# @Desc : DESC

from eas import PSO
from eas.target import fs
import sys
import matplotlib.pyplot as plt
from math import log10

random_state = 42
_np = 60  # 种群个数
n = 10
max_gen = 500

ea = PSO(_np,
         n,
         [100] * n,
         [-100] * n,
         vub=[5] * n,
         vlb=[-5] * n,
         max_gen=max_gen,
         procedure=fs[sys.argv[1]],
         random_state=random_state)
ea.fit()
fig, ax = plt.subplots(1, 1)
ax.plot([log10(x) for x in ea.hbsc], 'r')
plt.show()



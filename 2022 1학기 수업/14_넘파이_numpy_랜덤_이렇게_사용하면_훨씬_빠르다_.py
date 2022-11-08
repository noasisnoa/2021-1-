# -*- coding: utf-8 -*-
"""14. 넘파이 NumPy 랜덤 이렇게 사용하면 훨씬 빠르다..ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ug6qv1dw0_k7YBzpbC-OGrCHV8thVkJf

# 14. 넘파이 NumPy 랜덤 이렇게 사용하면 훨씬 빠르다.
"""

import numpy as np
np.ones(3)

np.zeros(3)

rng = np.random.default_rng(0) #seed 고정해주기
rng.random(3)

np.ones((3, 2))

np.zeros((3, 2))

rng.random((3, 2)) # 위에 seed값을 고정해주었기 때문에 random 값이 같게 나온다.

rng.integers(5, size=(2, 4))

import matplotlib.pyplot as plt
rn = rng.standard_normal(1000)
plt.hist(rn)

rex = rng.standard_exponential(1000)
plt.hist(rex)

rgm = rng.standard_gamma(1000)
plt.hist(rgm)

rnd = rng.random(1000)
plt.hist(rnd)
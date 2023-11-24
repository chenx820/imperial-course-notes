import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# 定义系统的参数
N = 20  # 光场的最大光子数
alpha = np.sqrt(5)  # 信号光的复振幅
beta = 5  # 本振光的复振幅

# 光场的初始态
a = destroy(N)
b = destroy(N) * np.exp(1j * 2)

rho1 = ket2dm((alpha * a.dag() - alpha.conjugate() * a).expm() * basis(N, 0))
rho2 = ket2dm((beta * b.dag() - beta.conjugate() * b).expm() * basis(N, 0))

a_BS = a + 1j * b
b_BS = b + 1j * a

rho1_BS = ket2dm((alpha * a_BS.dag() - alpha.conjugate() * a_BS).expm() * basis(N, 0))
rho2_BS = ket2dm((beta * b_BS.dag() - beta.conjugate() * b_BS).expm() * basis(N, 0))

hinton(rho2_BS)

# 定义分束器的操作矩阵
# BS = Qobj([[1, 1j], [1j, 1]]) / np.sqrt(2)


# 用分束器操作光场的态
# rho_BS = BS.dag() * * BS

# b1 = a1 + 1j * a2
# b2 = a2 + 1j * a1

# 计算两个探测器的输出的期望值
I1 = expect(a_BS.dag()*a_BS, rho1_BS)
I2 = expect(b_BS.dag()*b_BS, rho2_BS)

# 计算差分放大器的输出
I_diff = I1 - I2

print("The output of the balanced homodyne detection is ", I_diff)

# hinton(rho)
plt.show()

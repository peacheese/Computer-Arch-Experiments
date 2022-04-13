import matplotlib.pyplot as plt
import numpy as np
import math
def x_update_scale_value(temp, position):
    return str(int(2 ** temp))
# 生成数据
x = np.arange(1,7,1) # 横坐标数据为从0到10之间，步长为0.1的等差数组
# y = np.array([0.039825, 0.040520, 0.038956, 0.039055, 0.065499, 0.066116, 0.079338, 0.108516, 0.113169])
y = np.array([1.310047, 1.063014, 1.126745, 3.047921, 3.076297, 2.995635])
# plt.gca().xaxis.set_major_formatter(x_update_scale_value)
plt.xlabel('K')
plt.ylabel('Time(s)')
plt.plot(x, y, 'o-')

plt.show()
import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Сравнение времени выполнения операции поэлементного перемножения стандартных списков и массивов NumPy
list1 = [np.random.rand() for i in range(1000000)]
list2 = [np.random.rand() for i in range(1000000)]

start = time.perf_counter()
result_list = [list1[i] * list2[i] for i in range(len(list1))]
end = time.perf_counter()
print("Время выполнения перемножения списков: ", end - start)

array1 = np.array(list1)
array2 = np.array(list2)

start = time.perf_counter()
result_array = np.multiply(array1, array2)
end = time.perf_counter()
print("Время выполнения перемножения массивов: ", end - start)

# График из файла data1.csv
data = np.genfromtxt('data1.csv', delimiter=',', skip_header=1, usecols=(0, 3, 4))
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]

fig, ax = plt.subplots()
ax.plot(x, y1, label='Столбец 4')
ax.plot(x, y2, label='Столбец 5')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('График данных из файла data1.csv')
ax.legend()

# График корреляции
corr_coef = np.corrcoef(y1, y2)[0, 1]
fig, ax = plt.subplots()
ax.scatter(y1, y2)
ax.set_xlabel('Столбец 4')
ax.set_ylabel('Столбец 5')
ax.set_title(f'График корреляции (коэффициент: {corr_coef:.2f})')

# Трёхмерный график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-np.pi, np.pi, 100)
y = x
z = np.tan(x)

ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Трёхмерный график')

plt.show()

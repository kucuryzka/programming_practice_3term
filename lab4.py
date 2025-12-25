import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(2 * x) / np.cos(x)


def L(x):
    return (x[0] - 3) ** 2 + (x[1] - 8) ** 2


def create_plot_2d(ax, x_data, y_data):
    ax.plot(x_data, y_data)
    ax.set_xlabel("ось Х")
    ax.set_ylabel("ось Y")
    ax.set_title("График f(x)")
    ax.legend(["y(x)"])
    ax.set_facecolor('#f0f0f0')


def create_scatter_plot(ax, x_data, y_data):
    ax.scatter(x_data, y_data, marker='v', color=(1, 0, 0), label='Точки функции')
    ax.set_title('Точечный график функции', fontsize=16)
    ax.set_xlabel('Ось X', fontsize=12)
    ax.set_ylabel('Ось Y', fontsize=12)
    ax.grid(True, color=(0, 0, 0), alpha=0)
    ax.legend()


def create_histograms(ax, uniform_data, normal_data):
    ax.hist(normal_data, bins=10, color='red', alpha=0.7, label='Нормальное распределение')
    ax.hist(uniform_data, bins=1, color='blue', alpha=0.7, label='Равномерное распределение')
    ax.hist(normal_data, bins=10, color='red', alpha=0.7, label='Нормальное распределение')
    ax.set_title('Гистограммы распределений')
    ax.set_xlabel('Значения')
    ax.set_ylabel('Частота')
    ax.legend()
    ax.grid(True, alpha=0.3)


def create_pie_chart(ax, unique, counts):
    colors_pie = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    ax.pie(counts, labels=unique, colors=colors_pie, autopct='%1.1f%%')
    ax.set_title('Круговая диаграмма распределения')


def create_bar_chart(ax, unique, counts):
    colors_bar = ['#FF9999', '#66B2FF', '#99FF99', '#FFD700']
    ax.bar(unique, counts, color=colors_bar)
    ax.set_title('Столбчатая диаграмма распределения')
    ax.set_xlabel('Числа')
    ax.set_ylabel('Частота')
    for i, count in enumerate(counts):
        ax.text(unique[i], count + 0.1, str(count), ha='center')


def create_3d_plot(ax):
    x_vals = np.linspace(0, 10, 50)
    y_vals = np.linspace(0, 10, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = L([X, Y])

    surf = ax.plot_surface(X, Y, Z, color='blue', alpha=0.7, linewidth=0.5, antialiased=True)
    ax.set_xlabel('X ось', fontsize=12)
    ax.set_ylabel('Y ось', fontsize=12)
    ax.set_zlabel('Z = L(x,y)', fontsize=12)
    ax.set_title('3D график функции L(x,y)', fontsize=14)
    return surf


n = 1000
a = 2
b = 3

print("step 1")
x_value = np.linspace(a, b, n)
y_value = f(x_value)

print("step 2")
plt.figure()
create_plot_2d(plt.gca(), x_value, y_value)
plt.show()

print("step 3")
plt.figure()
create_scatter_plot(plt.gca(), x_value, y_value)
plt.show()

print("step 4")
uniform_sample = np.random.randint(0, 101, size=n)
normal_sample = np.random.normal(loc=50, scale=15, size=n)
normal_sample = np.clip(normal_sample, 0, 101)

plt.figure()
create_histograms(plt.gca(), uniform_sample, normal_sample)
plt.show()

print("step 5")
sample = np.random.randint(1, 5, 50)
unique, counts = np.unique(sample, return_counts=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
create_pie_chart(ax2, unique, counts)
create_bar_chart(ax1, unique, counts)
plt.tight_layout()
plt.show()

print("step 6")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = create_3d_plot(ax)
plt.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

print("step 7-8")
def create_subplot_grid(style_name):
    with plt.style.context(style_name):
        fig = plt.figure(figsize=(20, 16))
        fig.suptitle(f'Стиль: {style_name}', fontsize=20)

        ax1 = fig.add_subplot(2, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 3)
        ax4 = fig.add_subplot(2, 2, 4, projection='3d')

        create_plot_2d(ax1, x_value, y_value)
        create_scatter_plot(ax2, x_value, y_value)
        create_pie_chart(ax3, unique, counts)
        create_3d_plot(ax4)

        plt.tight_layout()
        plt.show()



styles = ['default', 'ggplot', 'seaborn-v0_8', 'dark_background']
for style in styles:
    create_subplot_grid(style)
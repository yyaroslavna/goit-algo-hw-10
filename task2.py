import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2


a = 0
b = 2
N = 100000


def monte_carlo(a, b, N):
    total = 0
    for i in range(N):
        x = random.uniform(a, b)
        total += f(x)
    return (b - a) * total / N


random.seed(42)
result = monte_carlo(a, b, N)
print("Результат Монте-Карло:", result)

exact_result = (b ** 3 - a ** 3) / 3
print("Аналітичний результат:", exact_result)


difference = abs(result - exact_result)
print("Похибка:", difference)


x = np.linspace(-0.5, 2.5, 400)
y = f(x)
plt.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
plt.fill_between(ix, iy, color='gray', alpha=0.3)
plt.axvline(x=a, color='gray', linestyle='--')
plt.axvline(x=b, color='gray', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Інтеграл функції f(x) = x^2')
plt.grid()
plt.show()

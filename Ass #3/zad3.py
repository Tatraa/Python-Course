import matplotlib.pyplot as plt
import numpy as np

x_min = int(input("Wstaw x_min:"))
x_max = int(input("Wstaw x_max:"))

x_val = np.linspace(x_min, x_max, 200)

x = x_val

y_val = eval(input("Wstaw swoje równanie:"))

print(x_val)
print(y_val)
print(x_min, x_max)

plt.plot(x_val, y_val)
plt.title('Wykres Wielomianu')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid()
plt.show()
plt.savefig('Chart.png')
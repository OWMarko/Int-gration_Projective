import numpy as np
import matplotlib.pyplot as plt

def f(t, x):
    return -4 * x

# Paramètres
x0 = 1
t0 = 0
T = 5
N_values = [10, 50, 100]

def euler_explicite(f, x0, t0, T, N):
    h = (T - t0) / N
    t = np.linspace(t0, T, N+1)
    x = np.zeros(N+1)
    x[0] = x0
    for i in range(N):
        x[i+1] = x[i] + h * f(t[i], x[i])
    return t, x

def euler_implicite(f, x0, t0, T, N):
    h = (T - t0) / N
    t = np.linspace(t0, T, N+1)
    x = np.zeros(N+1)
    x[0] = x0
    for i in range(N):
        x[i+1] = x[i] / (1 + 4 * h) 
    return t, x


fig, axs = plt.subplots(1, len(N_values), figsize=(18, 6))

for idx, N in enumerate(N_values):
    t_e, x_e = euler_explicite(f, x0, t0, T, N)
    t_i, x_i = euler_implicite(f, x0, t0, T, N)

    axs[idx].plot(t_e, x_e, label=f'Euler explicite, N={N}')
    axs[idx].plot(t_i, x_i, '--', label=f'Euler implicite, N={N}')

    t_exact = np.linspace(t0, T, 1000)
    x_exact = x0 * np.exp(-4 * t_exact)
    axs[idx].plot(t_exact, x_exact, 'k', label='Solution exacte')

    axs[idx].set_xlabel('Temps t')
    axs[idx].set_ylabel('Solution x(t)')
    axs[idx].legend()
    axs[idx].set_title(f'N={N}')
    axs[idx].grid()

fig.suptitle('Comparaison des méthodes d\'Euler explicite et implicite')
plt.show()

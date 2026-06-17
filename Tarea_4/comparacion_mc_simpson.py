"""
Integración Monte Carlo vs Simpson
Exploración de la maldición de la dimensionalidad

I_d = ∫_[0,1]^d ∏ sin(pi x_i) dx
Solución analítica: (2/pi)^d
"""

import numpy as np
from scipy.integrate import simpson
import time
import matplotlib.pyplot as plt

# =========================

np.random.seed(42)

dimensiones = [1, 2, 3, 4, 5, 6, 8, 10, 16, 32]

N_MC = 10**5
N_simpson = 10

# FUNCIÓN ANALÍTICA

def integral_analitica(d):
    return (2.0 / np.pi) ** d



# MONTE CARLO


def monte_carlo(d, N):
    
    x = np.random.uniform(0, 1, size=(N, d))
    f = np.prod(np.sin(np.pi * x), axis=1)
    return np.mean(f)



# SIMPSON MULTIDIMENSIONAL


def simpson_nd(d, N):
    x_1d = np.linspace(0, 1, N)
    malla = np.meshgrid(*[x_1d] * d, indexing="ij")

    Z = np.prod([np.sin(np.pi * m) for m in malla], axis=0)

    for _ in range(d):
        Z = simpson(Z, x=x_1d, axis=0)

    return Z


# =========================

resultados_mc = []
resultados_simpson = []

print("\n==============================")
print("INICIO EXPERIMENTO MC vs SIMPSON")
print("==============================\n")

for d in dimensiones:

    I_exacta = integral_analitica(d)

    print(f"\n--- Dimensión d = {d} ---")
    print(f"Exacto: {I_exacta:.6e}")

    # MONTE CARLO
    t0 = time.time()

    integral_mc = monte_carlo(d, N_MC)

    t1 = time.time()

    error_mc = abs(integral_mc - I_exacta)
    tiempo_mc = t1 - t0

    resultados_mc.append((d, integral_mc, error_mc, tiempo_mc))

    print(f"MC      : {integral_mc:.6e} | error={error_mc:.2e} | t={tiempo_mc:.4f}s")

    # SIMPSON
    if d <= 8:   # límite razonable

        t0 = time.time()

        integral_simpson = simpson_nd(d, N_simpson)

        t1 = time.time()

        error_simpson = abs(integral_simpson - I_exacta)
        tiempo_simpson = t1 - t0

        resultados_simpson.append((d, integral_simpson, error_simpson, tiempo_simpson))

        print(f"Simpson : {integral_simpson:.6e} | error={error_simpson:.2e} | t={tiempo_simpson:.4f}s")

    else:
        resultados_simpson.append((d, np.nan, np.nan, np.nan))
        print("Simpson : NO COMPUTABLE (explosión de memoria / maldición de dimensionalidad)")
    

# Tablas


print("\n==============================")
print("RESUMEN FINAL")
print("==============================\n")

print("Monte Carlo:")
for r in resultados_mc:
    print(f"d={r[0]:2d} | error={r[2]:.2e} | tiempo={r[3]:.4f}s")

print("\nSimpson:")
for r in resultados_simpson:
    print(f"d={r[0]:2d} | error={r[2]} | tiempo={r[3]}")



# GRÁFICAS


d_mc, _, err_mc, t_mc = zip(*resultados_mc)
d_s, _, err_s, t_s = zip(*resultados_simpson)

plt.figure()
plt.plot(d_mc, err_mc, marker="o", label="Monte Carlo")
plt.plot(d_s, err_s, marker="o", label="Simpson")
plt.yscale("log")
plt.xlabel("Dimensión d")
plt.ylabel("Error absoluto")
plt.title("Error vs Dimensión")
plt.grid()
plt.legend()

plt.figure()
plt.plot(d_mc, t_mc, marker="o", label="Monte Carlo")
plt.plot(d_s, t_s, marker="o", label="Simpson")
plt.yscale("log")
plt.xlabel("Dimensión d")
plt.ylabel("Tiempo (s)")
plt.title("Tiempo vs Dimensión")
plt.grid()
plt.legend()

plt.show()

print("\n==============================")
print("FIN DEL EXPERIMENTO")
print("==============================")
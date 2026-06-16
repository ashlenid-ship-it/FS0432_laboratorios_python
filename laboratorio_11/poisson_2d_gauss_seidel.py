import numpy as np
import matplotlib.pyplot as plt


def fuente(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)


def solucion_exacta(x, y):
    return -np.sin(np.pi * x) * np.sin(np.pi * y) / (2.0 * np.pi**2)


def error_maximo(u, u_exacta):
    return np.max(np.abs(u - u_exacta))


def graficar_mapa(u, titulo, nombre_archivo):
    plt.figure(figsize=(6, 5))
    plt.imshow(u.T, origin="lower", extent=[0, 1, 0, 1], cmap="viridis")
    plt.colorbar()
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=200)


def graficar_error_convergencia(errores, nombre_archivo):
    plt.figure()
    plt.plot(errores)
    plt.title("Error de convergencia")
    plt.savefig(nombre_archivo, dpi=200)


def main():

    N = 50
    h = 1.0 / N
    tol = 1e-8
    max_iter = 200000

    x = np.linspace(0, 1, N+1)
    y = np.linspace(0, 1, N+1)

    X, Y = np.meshgrid(x, y, indexing="ij")

    f = fuente(X, Y)
    u_exacta = solucion_exacta(X, Y)

    u = np.zeros((N+1, N+1))

    errores_convergencia = []

    iteracion = 0
    error_conv = 1.0
#_______________
    while error_conv > tol and iteracion < max_iter:

        error_conv = 0.0

        for i in range(1, N):
            for j in range(1, N):

                old = u[i, j]

                u[i, j] = 0.25 * (
                    u[i+1, j] + u[i-1, j] +
                    u[i, j+1] + u[i, j-1] -
                    h**2 * f[i, j])

                error_conv = max(error_conv, abs(u[i, j] - old))

        errores_convergencia.append(error_conv)

        iteracion += 1
#_______________
    error_exacto = error_maximo(u, u_exacta)

    print("Metodo: Gauss-Seidel 2D")
    print("Iteraciones =", iteracion)
    print("Error convergencia =", error_conv)
    print("Error maximo =", error_exacto)

    error_absoluto = np.abs(u - u_exacta)

    graficar_mapa(u, "Gauss-Seidel", "solucion_gs.png")
    graficar_mapa(u_exacta, "Exacta", "exacta_gs.png")
    graficar_mapa(error_absoluto, "Error", "error_gs.png")

    graficar_error_convergencia(errores_convergencia, "conv_gs.png")

    plt.show()


if __name__ == "__main__":
    main()
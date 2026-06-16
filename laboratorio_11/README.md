# Laboratorio 11 - Física Computacional

## Información del estudiante
- Nombre: Ashley Ureña Fonseca
- Carné: C27948
- Curso: Física Informática
- Laboratorio: 11

---

## Descripción

Seresuelve numéricamente la ecuación de Poisson en dos dimensiones utilizando el método de diferencias finitas.

Se implementan dos métodos iterativos:

- Método de Jacobi
- Método de Gauss-Seidel

## Ecuación resuelta

∂²u/∂x² + ∂²u/∂y² = sin(πx)sin(πy)

Solución analítica:
u(x,y) = -sin(πx)sin(πy) / (2π²)

---

## Archivos incluidos

- poisson_2d_jacobi.py → implementación del método de Jacobi
- poisson_2d_gauss_seidel.py → implementación del método de Gauss-Seidel
- output_jacobi.txt → salida del programa Jacobi
- output_gauss_seidel.txt → salida del programa Gauss-Seidel
- comparacion.txt → comparación de ambos métodos

---

## Resultados

Se observa que el método de Gauss-Seidel converge en menos iteraciones que el método de Jacobi

---

## Ejecución

Para ejecutar Jacobi y gauss seidel:

```bash
python poisson_2d_jacobi.py
python poisson_2d_gauss_seidel.py
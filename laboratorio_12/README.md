# Laboratorio 12 - Ecuación de Calor 2D
Ashley Ureña Fonseca        C27978
## Curso

FS0432 - Física Computacional

## Descripción

Este programa resuelve numéricamente la ecuación de calor en dos dimensiones utilizando el método explícito de diferencias finitas.

Las condiciones de frontera utilizadas son:

* Bordes izquierdo y derecho: temperatura = 10
* Bordes superior e inferior: temperatura = 5

El programa almacena snapshots de la distribución de temperatura y genera una animación de la evolución temporal en formato GIF.

## Archivos incluidos

* `heat_2d.py` : código fuente.
* `calor_2d.gif` : animación generada.
* `output.txt` : ejemplo de ejecución.
* `README.md` : instrucciones de uso.


## Instalación

```bash
pip install numpy matplotlib pillow
```

## Ejecución

```bash
python heat_2d.py
```

El programa generará automáticamente el archivo:

```text
calor_2d.gif
```

# Sistema de Gestión de Biblioteca (Grafo Dirigido No Ponderado)

Este proyecto implementa un sistema interactivo de gestión de biblioteca utilizando estructuras de datos no lineales, específicamente un **Grafo Dirigido No Ponderado**. Está diseñado para modelar y gestionar de manera eficiente las relaciones de préstamos entre usuarios y libros de una biblioteca.

El proyecto forma parte de la asignatura de **Estructura de Datos** de la Corporación Universitaria Iberoamericana (IberoU).

---

## Concepto del Modelo de Grafo

El sistema modela los elementos de la biblioteca utilizando la teoría de grafos:

- **Nodos (Vértices):** Representan dos tipos de entidades:
  - **Usuarios:** Identificados con el prefijo `U` seguido de su ID (ej. `U101`).
  - **Libros:** Identificados con el prefijo `L` seguido de su ID (ej. `L202`).
- **Aristas (Arcos Dirigidos):** Representan un préstamo activo desde un usuario hacia un libro (`Usuario → Libro`).
  - El grafo es **dirigido** porque el préstamo tiene un sentido claro (de usuario a libro).
  - Es **no ponderado** porque no existe un valor o costo asociado a la relación de préstamo.

---

## Características Principales

1.  **Gestión de Inventario (Libros):**
    - Agregar libros con título, autor, editorial y género.
    - Eliminar libros del sistema (solo si no están prestados actualmente).
    - Visualizar el inventario completo y el estado de cada libro (_Disponible_ o _Prestado_).
2.  **Gestión de Usuarios:**
    - Registrar usuarios con un nombre e ID único.
    - Eliminar usuarios (solo si no tienen libros pendientes por devolver).
    - Visualizar la lista de usuarios y los títulos de los libros que tienen prestados.
3.  **Sistema de Préstamos y Devoluciones:**
    - **Prestar Libro:** Crea una arista dirigida entre el usuario y el libro.
      - _Restricción:_ Un libro solo puede ser prestado a un usuario a la vez.
      - _Restricción:_ Cada usuario puede tener un máximo de **3 libros** prestados simultáneamente.
    - **Devolver Libro:** Elimina la arista dirigida del préstamo actual, dejando el libro disponible de inmediato.
4.  **Visualización del Grafo:**
    - Permite ver la estructura interna del grafo mediante la representación de su **Lista de Adyacencia**, mostrando de forma transparente cómo se conectan los usuarios con los libros prestados en memoria.

## Ejecución y Uso

Para ejecutar el programa, simplemente ejecuta el archivo principal en tu consola o terminal:

```bash
py biblioteca.py
```

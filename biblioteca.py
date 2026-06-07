# SISTEMA DE GESTIÓN DE BIBLIOTECA
# Estructuras de Datos No Lineales: Grafo Dirigido No Ponderado


class GrafoBiblioteca:
    """
    Grafo dirigido no ponderado que modela las relaciones entre
    usuarios y libros en el sistema de la biblioteca.

    Nodos  : usuarios (prefijo 'U') y libros (prefijo 'L')
    Aristas: usuario → libro  (representa un préstamo activo)
    """

    def __init__(self):
        self.adyacencia = {}
        self.nodos = {}

    def agregar_nodo(self, id_nodo, datos):
        if id_nodo in self.nodos:
            return False   
        self.nodos[id_nodo] = datos
        self.adyacencia[id_nodo] = set()
        return True

    def agregar_arista(self, id_origen, id_destino):
        """Agrega arista dirigida origen → destino (préstamo)."""
        if id_origen not in self.nodos or id_destino not in self.nodos:
            return False
        self.adyacencia[id_origen].add(id_destino)
        return True

    def eliminar_nodo(self, id_nodo):
        if id_nodo not in self.nodos:
            return False
        del self.adyacencia[id_nodo]
        del self.nodos[id_nodo]
        for vecinos in self.adyacencia.values():
            vecinos.discard(id_nodo)
        return True

    def eliminar_arista(self, id_origen, id_destino):
        if id_origen not in self.adyacencia:
            return False
        self.adyacencia[id_origen].discard(id_destino)
        return True

    def buscar_nodo(self, id_nodo):
        return self.nodos.get(id_nodo)

    def libros_de_usuario(self, id_usuario):
        return list(self.adyacencia.get(id_usuario, []))

    def usuario_de_libro(self, id_libro):
        for id_u, vecinos in self.adyacencia.items():
            if id_libro in vecinos and self.nodos[id_u]["tipo"] == "usuario":
                return id_u
        return None

    def libro_esta_prestado(self, id_libro):
        return self.usuario_de_libro(id_libro) is not None

    def mostrar_grafo(self):
        print("\n─ Estructura del Grafo (Lista de Adyacencia) ─")
        for nodo, vecinos in self.adyacencia.items():
            tipo = self.nodos[nodo]["tipo"]
            nombre = self.nodos[nodo].get("nombre") or self.nodos[nodo].get("titulo", "")
            destinos = ", ".join(vecinos) if vecinos else "∅"
            print(f"  [{tipo.upper()}] {nodo} ({nombre})  →  {destinos}")
        print()

#  GRAFO GLOBAL DEL SISTEMA

grafo = GrafoBiblioteca()

#  OPERACIONES DEL SISTEMA

def agregar_libro():
    print("\n─ Agregar Nuevo Libro ─")
    id_libro = input("Ingrese el ID del libro: ").strip()
    if not id_libro:
        print("[ERROR] El ID no puede estar vacío.")
        return

    id_nodo = "L" + id_libro
    if grafo.buscar_nodo(id_nodo):
        print(f"[ERROR] El ID '{id_libro}' ya existe.")
        return

    titulo    = input("Título del libro: ").strip()
    autor     = input("Autor: ").strip()
    editorial = input("Editorial: ").strip()
    genero    = input("Género: ").strip()

    if not titulo:
        print("[ERROR] El título no puede estar vacío.")
        return

    datos = {
        "tipo"      : "libro",
        "id"        : id_libro,
        "titulo"    : titulo,
        "autor"     : autor,
        "editorial" : editorial,
        "genero"    : genero,
    }
    grafo.agregar_nodo(id_nodo, datos)
    print(f"\nLibro '{titulo}' agregado exitosamente.\n")


def agregar_usuario():
    print("\n─ Agregar Nuevo Usuario ─")
    id_usuario = input("Ingrese el ID del usuario: ").strip()
    if not id_usuario:
        print("[ERROR] El ID no puede estar vacío.")
        return

    id_nodo = "U" + id_usuario
    if grafo.buscar_nodo(id_nodo):
        print(f"[ERROR] El ID de usuario '{id_usuario}' ya existe.")
        return

    nombre = input("Nombre del usuario: ").strip()
    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return

    datos = {"tipo": "usuario", "id": id_usuario, "nombre": nombre}
    grafo.agregar_nodo(id_nodo, datos)
    print(f"\nUsuario '{nombre}' agregado exitosamente.\n")


def prestar_libro():
    print("\n─ Prestar Libro ─")
    uid = input("ID del usuario: ").strip()
    bid = input("ID del libro  : ").strip()

    id_u = "U" + uid
    id_l = "L" + bid

    user = grafo.buscar_nodo(id_u)
    book = grafo.buscar_nodo(id_l)

    if not user:
        print("Usuario no encontrado.")
        return
    if not book:
        print("Libro no encontrado.")
        return
    if grafo.libro_esta_prestado(id_l):
        print("El libro ya está prestado.")
        return
    if len(grafo.libros_de_usuario(id_u)) >= 3:
        print(f"[ERROR] {user['nombre']} ya tiene el máximo de 3 libros permitidos.")
        return

    grafo.agregar_arista(id_u, id_l)
    print(f"\nPréstamo exitoso: '{book['titulo']}' → {user['nombre']}\n")


def devolver_libro():
    print("\n─ Devolver Libro ─")
    bid = input("ID del libro a devolver: ").strip()
    id_l = "L" + bid

    book = grafo.buscar_nodo(id_l)
    if not book:
        print("Libro no encontrado.")
        return

    id_u = grafo.usuario_de_libro(id_l)
    if not id_u:
        print("El libro no estaba prestado.")
        return

    grafo.eliminar_arista(id_u, id_l)
    user = grafo.buscar_nodo(id_u)
    print(f"\nLibro '{book['titulo']}' devuelto por {user['nombre']}.\n")


def mostrar_libros():
    print("\n─ Inventario de Libros ─")
    libros = [d for d in grafo.nodos.values() if d["tipo"] == "libro"]
    if not libros:
        print("La biblioteca está vacía.")
    else:
        for l in libros:
            id_l    = "L" + l["id"]
            estado  = "Prestado" if grafo.libro_esta_prestado(id_l) else "Disponible"
            print(f"ID: {l['id']} | Título: {l['titulo']} | Autor: {l['autor']} "
                  f"| Editorial: {l['editorial']} | Género: {l['genero']} | Estado: {estado}")
    print()


def mostrar_usuarios():
    print("\n─ Usuarios Registrados ─")
    usuarios = [d for d in grafo.nodos.values() if d["tipo"] == "usuario"]
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for u in usuarios:
            id_u    = "U" + u["id"]
            libros  = [grafo.nodos[l]["titulo"] for l in grafo.libros_de_usuario(id_u)]
            print(f"ID: {u['id']} | Nombre: {u['nombre']} | Libros prestados: {libros}")
    print()


def eliminar_libro():
    print("\n─ Eliminar Libro ─")
    bid  = input("ID del libro a eliminar: ").strip()
    id_l = "L" + bid
    book = grafo.buscar_nodo(id_l)
    if not book:
        print("Libro no encontrado.")
        return
    if grafo.libro_esta_prestado(id_l):
        print("[ERROR] No se puede eliminar un libro que está prestado.")
        return
    grafo.eliminar_nodo(id_l)
    print(f"Libro '{book['titulo']}' eliminado del sistema.\n")


def eliminar_usuario():
    print("\n─ Eliminar Usuario ─")
    uid  = input("ID del usuario a eliminar: ").strip()
    id_u = "U" + uid
    user = grafo.buscar_nodo(id_u)
    if not user:
        print("Usuario no encontrado.")
        return
    if grafo.libros_de_usuario(id_u):
        print("[ERROR] No se puede eliminar un usuario con préstamos activos.")
        return
    grafo.eliminar_nodo(id_u)
    print(f"Usuario '{user['nombre']}' eliminado del sistema.\n")


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

while True:
    print("-" * 35)
    print("    SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("         Grafo Dirigido No Ponderado")
    print("-" * 35)
    print("1. Agregar libro")
    print("2. Agregar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros")
    print("6. Mostrar usuarios")
    print("7. Mostrar grafo (lista de adyacencia)")
    print("8. Eliminar libro")
    print("9. Eliminar usuario")
    print("10. Salir")

    opcion_input = input("\nSeleccione una opción: ").strip()

    if not opcion_input.isdigit():
        print("Error: ingrese un número del 1 al 10.")
        continue

    opcion = int(opcion_input)

    if   opcion == 1:  agregar_libro()
    elif opcion == 2:  agregar_usuario()
    elif opcion == 3:  prestar_libro()
    elif opcion == 4:  devolver_libro()
    elif opcion == 5:  mostrar_libros()
    elif opcion == 6:  mostrar_usuarios()
    elif opcion == 7:  grafo.mostrar_grafo()
    elif opcion == 8:  eliminar_libro()
    elif opcion == 9:  eliminar_usuario()
    elif opcion == 10:
        print("Gracias por visitarnos, hasta luego.")
        break
    else:
        print("Opción no válida, intente de nuevo.")
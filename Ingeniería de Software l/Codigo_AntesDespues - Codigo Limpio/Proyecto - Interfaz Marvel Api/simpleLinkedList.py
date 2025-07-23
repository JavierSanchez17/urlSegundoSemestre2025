from node import Node


class SimplyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    # ------------------ Metodos Para Añadir ------------------
    # Insertar al inicio
    def unshift(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    # Insertar al final
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    # Insertar una posicion en especifico
    def insert_at(self, data, pos):
        new_nodo = Node(data)
        if self.is_empty():
            raise Exception('La lista vacia')
        elif pos == 0:
            self.unshift(data)
        elif pos == self.size:
            self.append(data)
        else:
            previus = self.find_at(pos - 1)
            new_nodo.next = previus.next
            previus.next = new_nodo
            self.size += 1

    # ------------------ Metodos Para Eliminar ------------------
    # Eliminar el inicio
    def shift(self):
        if self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1

        return current.data

    # Eliminar el final
    def pop(self):
        current = self.tail
        if self.is_empty():
            raise Exception("Subdesbordamiento de pila")
        elif self.size == 1:
            current.next = None
            self.head = None
            self.tail = None
            self.size = 0
        else:
            prev = self.find_at(self.size - 2)
            current = self.tail
            self.tail = prev
            prev.next = None
            self.size -= 1

        return current.data

    # Eliminar es una posicion
    def remove_at(self, index):
        if self.is_empty():
            raise Exception("Subdesbordamiento")
        elif index == 0:
            return self.shift()
        elif index == (self.size - 1):
            return self.pop()
        else:
            current = self.find_at(index)
            prev = self.find_at(index - 1)
            prev.next = current.next
            current.next = None
            self.size -= 1

    # Eliminar el valor en especifico
    def remove_by(self, data, event):
        current = self.find_by(data, event)
        pos = self.get_index(current)
        self.remove_at(pos)
        current.next = None
        return current

    # ------------------ Metodos De Busqueda ------------------
    # Hace recorrido para visualizar elementos dentro de la lista
    def transversal(self):
        current = self.head
        result = []

        while current is not None:
            result.append(current)
            current = current.next

        return result

    def transversal_print(self):
        current = self.head
        result = ""

        while current is not None:
            result += current.data
            current = current.next
            if current is not None:
                result += " -> "

        return result

    # Es busca el numero especifico
    def find_at(self, index):
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current
            else:
                current = current.next
                i += 1

        raise Exception("La posicion no existe")

    # Encontrar un elemento dentro de la lista
    def find_by(self, data, event):
        current = self.head
        if event == 1:
            while current is not None:
                if current.data.get_dpi() == data:
                    return current
                else:
                    current = current.next
        elif event == 2:
            while current is not None:
                if current.data.get_name() == data:
                    return current
                else:
                    current = current.next
        elif event == 3:
            while current is not None:
                if current.data.get_mail() == data:
                    return current
                else:
                    current = current.next
        elif event == 4:
            while current is not None:
                if current.data.get_id() == data:
                    return current
                else:
                    current = current.next

        raise Exception("El elemento no existe")

    # buscar la posicion de un nodo por su valor
    def get_index(self, ref):
        current = self.head
        pos = 0

        while current is not None:
            # si comparamos direcciones de memoria usamos is, valores se usa ==
            if current is ref:
                return pos
            else:
                current = current.next
                pos += 1

        raise Exception('No direccion de memoria no existente...')

    # Verificar si la lista está vacia
    def is_empty(self):
        return self.head is None and self.tail is None

    # Extras
    def quantity(self):
        current = self.head
        pos = 0

        while current is not None:
            current = current.next
            pos += 1

        return pos

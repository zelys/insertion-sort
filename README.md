# Algoritmo de ordenamiento

En este ejemplo (Codigó), la función _insertionSort()_ realiza el ordenamiento utilizando el método de "Bubble Sort" el cual además se integra con el uso de listas por comprensión para realizar el intercambio de elementos de manera más compacta.

Aunque este método funciona bien, existen algoritmos de ordenamiento más eficientes, como "Merge Sort" o "Quick Sort", estos permiten un mejor rendimiento al trabajar con listas más grandes.

Sin embargo, Python cuenta con la función _sorted()_ la cual utiliza un algoritmo de ordenamiento híbrido que combina el algoritmo Timsort (una versión mejorada de Merge Sort) y técnicas de adaptación para mejorar el rendimiento en casos comunes.

Esta función toma como argumento la secuencia a ordenar y opcionalmente permite especificar criterios de ordenamiento personalizados mediante el parámetro key.

### Ejemplo básico de cómo usar _sorted()_:

```python
original_list = [75, 35, 20, 2, 1]

# Utilizar sorted() para obtener una nueva lista ordenada
sorted_list = sorted(original_list)

# Mostrar la lista original y la lista ordenada
print("Lista original:", original_list)
print("Lista ordenada:", sorted_list)

# Lista original: [75, 35, 20, 2, 1]
# Lista ordenada: [1, 2, 20, 35, 75]
```

En este caso, _sorted(original_list)_ devuelve una nueva lista ordenada y no modifica la lista original.

La función _sorted()_ además puede recibir un parámetro _key_ que especifica una función para generar un valor clave que se utilizará para ordenar los elementos. Por ejemplo:

```python
# Ordenar una lista de cadenas por longitud
string_list = ["apple", "banana", "kiwi", "orange"]
sorted_string_list = sorted(string_list, key=len)

print("Lista original:", string_list)
print("Lista ordenada por longitud:", sorted_string_list)

# Lista original: ['apple', 'banana', 'kiwi', 'orange']
# Lista ordenada por longitud: ['kiwi', 'apple', 'banana', 'orange']
```

En este ejemplo, la función _len_ se utiliza como clave para ordenar la lista de cadenas por longitud.

import pandas as pd
import time
import matplotlib.pyplot as plt

class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def hash_function(self, key):
        return hash(str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if len(self.table[index]) > 0:
            self.collisions += 1
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def load_factor(self, total_elements):
        return total_elements / self.size


class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def hash_function(self, key):
        return hash(str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            self.collisions += 1
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        start = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start:
                break
        return None

    def load_factor(self, total_elements):
        return total_elements / self.size


class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def hash1(self, key):
        return hash(str(key)) % self.size

    def hash2(self, key):
        # Garantiza que el paso nunca sea 0
        return 1 + (hash(str(key)) % (self.size - 1))

    def insert(self, key, value):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        while self.table[index] is not None:
            self.collisions += 1
            i += 1
            index = (self.hash1(key) + i * step) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        start = index
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (self.hash1(key) + i * step) % self.size
            if index == start:
                break
        return None

    def load_factor(self, total_elements):
        return total_elements / self.size


# Cargar dataset
df = pd.read_csv("D:/Metodos Numericos/tablas_hash/online_retail_II.csv")
df = df.dropna()
keys = df["Invoice"].astype(str).head(10000).tolist()

table_size = 20011

# ---- Encadenamiento separado ----
hash_chain = HashTableChaining(table_size)

start_time = time.time()
for key in keys:
    hash_chain.insert(key, {"Invoice": key})
insert_time_chain = time.time() - start_time

start_time = time.time()
for key in keys[:1000]:
    hash_chain.search(key)
search_time_chain = time.time() - start_time

# ---- Sondeo lineal ----
hash_linear = HashTableLinearProbing(table_size)

start_time = time.time()
for key in keys:
    hash_linear.insert(key, {"Invoice": key})
insert_time_linear = time.time() - start_time

start_time = time.time()
for key in keys[:1000]:
    hash_linear.search(key)
search_time_linear = time.time() - start_time

# ---- Doble hashing ----
hash_double = HashTableDoubleHashing(table_size)

start_time = time.time()
for key in keys:
    hash_double.insert(key, {"Invoice": key})
insert_time_double = time.time() - start_time

start_time = time.time()
for key in keys[:1000]:
    hash_double.search(key)
search_time_double = time.time() - start_time

# ---- Tabla comparativa ----
results = pd.DataFrame({
    "Metodo": ["Encadenamiento", "Sondeo lineal", "Doble hashing"],
    "Tiempo insercion": [insert_time_chain, insert_time_linear, insert_time_double],
    "Tiempo busqueda":  [search_time_chain, search_time_linear, search_time_double],
    "Colisiones":       [hash_chain.collisions, hash_linear.collisions, hash_double.collisions],
    "Factor de carga":  [
        hash_chain.load_factor(len(keys)),
        hash_linear.load_factor(len(keys)),
        hash_double.load_factor(len(keys))
    ]
})

print(results.to_string(index=False))

colores = ["#4C72B0", "#DD8452", "#55A868"]

# ---- Gráfico de tiempo de inserción ----
plt.figure(figsize=(8, 5))
plt.bar(results["Metodo"], results["Tiempo insercion"], color=colores)
plt.title("Comparación de tiempo de inserción")
plt.xlabel("Método")
plt.ylabel("Tiempo en segundos")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ---- Gráfico de tiempo de búsqueda ----
plt.figure(figsize=(8, 5))
plt.bar(results["Metodo"], results["Tiempo busqueda"], color=colores)
plt.title("Comparación de tiempo de búsqueda")
plt.xlabel("Método")
plt.ylabel("Tiempo en segundos")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# ---- Gráfico de colisiones ----
plt.figure(figsize=(8, 5))
plt.bar(results["Metodo"], results["Colisiones"], color=colores)
plt.title("Comparación de colisiones")
plt.xlabel("Método")
plt.ylabel("Número de colisiones")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
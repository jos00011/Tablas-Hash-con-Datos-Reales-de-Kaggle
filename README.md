# Tablas Hash con Datos Reales (Kaggle)

# Presentado por: Coaguila Alave Jose Enrique

## Descripción
Este proyecto implementa y compara diferentes métodos de resolución de colisiones en tablas hash:
- Encadenamiento separado
- Sondeo lineal

Se analiza su rendimiento utilizando un dataset real, evaluando tiempos de inserción, búsqueda, número de colisiones y factor de carga. Además, se incluye una comparación con el diccionario nativo de Python.

---

## Objetivos

- Implementar estructuras de tablas hash desde cero.
- Comparar métodos de resolución de colisiones.
- Evaluar rendimiento con datos reales.
- Analizar eficiencia en función del factor de carga.

---

## Tecnologías utilizadas

- Python 3
- C++
- pandas
- matplotlib

## Estructura del proyecto

-tablas_hash/

│── tablas_hash.py # Implementación principal en Python

│── tablas_hash.cpp # Implementación opcional en C++

│── .gitignore

│── README.md

---

## Metodología

1. Se carga un dataset real (Online Retail II).
2. Se seleccionan claves (`user_id` u otro identificador).
3. Se insertan los datos en:
   - Tabla hash con encadenamiento
   - Tabla hash con sondeo lineal
   - Diccionario nativo de Python
4. Se mide:
   - Tiempo de inserción
   - Tiempo de búsqueda
   - Número de colisiones
   - Factor de carga

---

## Resultados esperados

- El diccionario de Python presenta mejor rendimiento debido a optimizaciones internas.
- El encadenamiento separado es más eficiente con factores de carga altos.
- El sondeo lineal puede degradarse por clustering.

---

## Imagenes de los Resultados En Python 

<img width="801" height="577" alt="Screenshot 2026-05-03 153025" src="https://github.com/user-attachments/assets/b97b70fa-4eb6-4936-a6a2-95401cb8a1ac" />

---

<img width="806" height="582" alt="Screenshot 2026-05-03 153035" src="https://github.com/user-attachments/assets/a401b865-7bff-4d9e-8176-a12de7c04c04" />

---

<img width="799" height="569" alt="Screenshot 2026-05-03 153015" src="https://github.com/user-attachments/assets/4011816d-3856-42e7-a9a6-4d7c3e1404ae" />

---

- Resultados de la terminal

<img width="560" height="92" alt="Screenshot 2026-05-03 161527" src="https://github.com/user-attachments/assets/265133e2-5422-4b39-b844-989384a9f268" />

---

## Imagenes de los Resultados En C++ (Terminal)
<img width="317" height="340" alt="Screenshot 2026-05-03 161646" src="https://github.com/user-attachments/assets/b635d80f-d188-42c0-a5f7-6e13b217941e" />

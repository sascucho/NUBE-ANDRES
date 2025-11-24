# ☁ NUBE-ANDRES | Solución de Procesamiento de Inscripciones 2025

Este proyecto implementa una solución de automatización en Python para el procesamiento, clasificación y visualización de datos de formularios de inscripción (Form.xlsx).

---

## 🎯 Objetivo del Proyecto

El objetivo principal es transformar un archivo de registro plano (Excel) en dos entregables analíticos clave:

1.  Un *Reporte Consolidado* que clasifica las inscripciones, separando los datos en hojas de cálculo según el semestre correspondiente.
2.  Una *Visualización de Datos* que cuantifica la distribución de proyectos por semestre.

---

## 🛠 Arquitectura y Estructura de Archivos

El proyecto sigue una estructura modular para separar claramente las entradas, el código y las salidas.

---

## ⚙ Requisitos y Dependencias

Para ejecutar el script **formulario.py**, es necesario tener instalado [Python 3.x](https://www.python.org/downloads/) y las siguientes librerías, las cuales se pueden instalar mediante pip:

```bash
pip install pandas openpyxl matplotlib

| Columna Clave | Propósito en el Script |
| :--- | :--- |
| Semestre del Proyecto | *Columna de Clasificación:* Usada para agrupar y nombrar las hojas de Excel. |
| Nombre del Proyecto | *Columna de Conteo:* Usada para cuantificar el número de registros por semestre. |
| Otras columnas... | Incluidas en el reporte, pero no usadas para la lógica de clasificación. |


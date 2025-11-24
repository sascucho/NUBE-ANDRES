import pandas as pd
import matplotlib.pyplot as plt
import os

# --- CONFIGURACIÓN ---
# Las variables han sido corregidas con base en tu lista de columnas
NOMBRE_ARCHIVO = 'Form.xlsx'
COLUMNA_SEMESTRE = 'Semestre del Proyecto'  # Nombre de la columna que indica el semestre
COLUMNA_PROYECTO = 'Nombre del Proyecto'    # Nombre de la columna que usaremos para contar
NOMBRE_REPORTE = 'Proyectos_Separados_2025.xlsx'
NOMBRE_GRAFICO = 'grafico_semestres.png'

# Rutas de carpetas (automáticas)
# --- RUTAS CORREGIDAS ---
# Usamos una ruta relativa para evitar NameError: _file_
carpeta_actual = os.getcwd() # Obtiene la ruta actual donde se ejecuta el comando
ruta_datos = os.path.join(carpeta_actual, 'datos')
ruta_resultados = os.path.join(carpeta_actual, 'resultados')
archivo_entrada = os.path.join(ruta_datos, NOMBRE_ARCHIVO)

def procesar_datos():
    print("1. Iniciando procesamiento de inscripciones...")
    
    # --- Verificación de Archivo y Carga ---
    if not os.path.exists(archivo_entrada):
        print(f"❌ ERROR: No se encuentra el archivo '{NOMBRE_ARCHIVO}' en la carpeta 'datos'.")
        print("Asegúrate de haberlo descargado y colocado allí.")
        return

    try:
        df = pd.read_excel(archivo_entrada)
        print("   ✅ Archivo cargado correctamente.")
    except Exception as e:
        print(f"❌ ERROR al leer el Excel: {e}")
        return

    # --- TAREA 1: REPORTE EXCEL (Separar por hojas) ---
    print("\n2. Generando reporte Excel separado por semestres...")
    nombre_salida = os.path.join(ruta_datos, NOMBRE_REPORTE)
    
    try:
        with pd.ExcelWriter(nombre_salida, engine='openpyxl') as writer:
            # Eliminar filas con valores nulos en la columna clave
            df_limpio = df.dropna(subset=[COLUMNA_SEMESTRE])
            
            # Obtener lista de semestres únicos
            semestres = df_limpio[COLUMNA_SEMESTRE].unique()
            
            for sem in semestres:
                # Filtrar datos de ese semestre
                df_semestre = df_limpio[df_limpio[COLUMNA_SEMESTRE] == sem]
                
                # Nombre de la hoja (limitado a 30 caracteres, si aplica)
                nombre_hoja = str(sem).replace('/', '-').replace(':', '')[:30] 
                
                # Guardar en una hoja
                df_semestre.to_excel(writer, sheet_name=nombre_hoja, index=False)
                
        print(f"   ✅ Reporte Excel guardado en: {nombre_salida}")
    except KeyError:
        print(f"❌ ERROR: Las columnas no coinciden. Revisa que '{COLUMNA_SEMESTRE}' sea correcta.")
        return

# --- TAREA 2: VISUALIZACIÓN (Gráfico de barras) ---
    print("\n3. Generando gráfico de visualización con precisión de 1 en 1...")
    
    try:
        # Contar proyectos por semestre (usa la columna de semestre)
        conteo = df[COLUMNA_SEMESTRE].value_counts().sort_index()

        # Crear gráfico
        plt.figure(figsize=(10, 6))
        conteo.plot(kind='bar', color='#1f77b4') # Color azul de ejemplo
        
        plt.title('Cantidad de Proyectos por Semestre 2025', fontsize=14)
        plt.xlabel('Semestre', fontsize=12)
        plt.ylabel('Número de Proyectos', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # --- CAMBIOS PARA PRECISION 1 EN 1 (LÍNEAS 80 y 81) ---
        # 1. Obtener el valor máximo en el conteo
        y_max = conteo.max() 
        # 2. Generar marcas (ticks) desde 0 hasta el máximo, de 1 en 1
        plt.yticks(range(0, y_max + 1, 1)) 
        # --------------------------------------------------------

        plt.tight_layout()

        # Guardar imagen
        ruta_imagen = os.path.join(ruta_resultados, NOMBRE_GRAFICO)
        plt.savefig(ruta_imagen)
        print(f"   ✅ Gráfico guardado en: {ruta_imagen}")
        
    except Exception as e:
        print(f"❌ ERROR al crear el gráfico: {e}")

    print("\n--- ✅ PROCESO FINALIZADO CON ÉXITO: ¡Revisa tus carpetas! ---")

if __name__ == "__main__":
    procesar_datos()
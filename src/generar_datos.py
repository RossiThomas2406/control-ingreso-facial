import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os
from pathlib import Path

# --- Configuración de rutas ABSOLUTAS ---
# 1. Obtenemos la ruta del directorio del script (src/)
script_dir = Path(__file__).parent.absolute()

# 2. Subimos un nivel para llegar a la raíz del proyecto
project_root = script_dir.parent

# 3. Definimos la carpeta data DENTRO del proyecto
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)  # Solo crea si no existe

# 4. Ruta completa del archivo de salida
output_path = data_dir / "produccion_simulada.csv"

# --- Generación de datos (igual que antes) ---
np.random.seed(42)
fechas = [datetime.now() - timedelta(days=i) for i in range(30)]
productos = ["Pan", "Facturas", "Tortas", "Galletas"]
turnos = ["Mañana", "Tarde"]
empleados = ["Juan", "Ana", "Luis", "María"]

data = {
    "fecha": fechas * len(productos),
    "producto": [p for p in productos for _ in range(30)],
    "turno": np.random.choice(turnos, size=120),
    "cantidad_producida": np.random.randint(50, 300, size=120),
    "cantidad_defectuosa": np.random.randint(0, 15, size=120),
    "empleado": np.random.choice(empleados, size=120)
}

df = pd.DataFrame(data)
df["eficiencia"] = round((1 - df["cantidad_defectuosa"] / df["cantidad_producida"]) * 100, 2)

# --- Guardado del archivo ---
df.to_csv(output_path, index=False)
print(f"✅ Dataset guardado EXCLUSIVAMENTE en: {output_path}")
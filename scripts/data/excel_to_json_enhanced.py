import pandas as pd
import json
import os
import numpy as np

# Función personalizada para manejar tipos no serializables en JSON
def json_serial(obj):
    """Función para serializar tipos que no son nativamente soportados por JSON"""
    if isinstance(obj, (np.integer)):
        return int(obj)
    if isinstance(obj, (np.floating)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, pd.Timestamp):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def excel_to_json_enhanced(excel_file):
    """
    Convierte un archivo Excel a JSON con mejoras:
    - Corrige valores NaN a null para compatibilidad JSON
    - Añade estadísticas y metadatos para cada hoja
    - Formatea valores float para mejorar legibilidad
    """
    if not os.path.exists(excel_file):
        print(f"❌ El archivo no existe: {excel_file}")
        return
    
    print(f"✅ Procesando archivo Excel: {excel_file}")
    
    try:
        # Leer el archivo Excel
        excel = pd.ExcelFile(excel_file)
        sheet_names = excel.sheet_names
        
        # Estructura para almacenar los datos mejorados
        enhanced_result = {
            "metadata": {
                "source_file": excel_file,
                "creation_date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_sheets": len(sheet_names),
                "sheet_names": sheet_names
            },
            "data": {}
        }
        
        # Procesar cada hoja
        for sheet_name in sheet_names:
            print(f"  - Procesando hoja: {sheet_name}")
            
            # Leer la hoja actual
            df = pd.read_excel(excel, sheet_name=sheet_name)
            
            # Calcular estadísticas básicas para columnas numéricas
            stats = {}
            for col in df.select_dtypes(include=[np.number]).columns:
                stats[col] = {
                    "min": df[col].min() if not pd.isna(df[col].min()) else None,
                    "max": df[col].max() if not pd.isna(df[col].max()) else None,
                    "avg": round(df[col].mean(), 2) if not pd.isna(df[col].mean()) else None,
                    "null_count": int(df[col].isna().sum())
                }
            
            # Convertir a lista de diccionarios con manejo especial para NaN/None
            records = df.replace({np.nan: None}).to_dict(orient='records')
            
            # Para valores float, redondear a 2 decimales para mejorar legibilidad
            for record in records:
                for key, value in record.items():
                    if isinstance(value, float):
                        record[key] = round(value, 2)
            
            # Almacenar en el diccionario de resultados con metadatos
            enhanced_result["data"][sheet_name] = {
                "records": records,
                "record_count": len(records),
                "column_count": len(df.columns),
                "columns": list(df.columns),
                "statistics": stats
            }
        
        # Crear el nombre del archivo JSON mejorado
        json_file = os.path.splitext(excel_file)[0] + '_enhanced.json'
        
        # Guardar el resultado en un archivo JSON con formato legible
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(enhanced_result, f, ensure_ascii=False, indent=2, default=json_serial)
        
        print(f"\n✅ Archivo JSON mejorado creado: {json_file}")
        print(f"   - Tamaño del archivo: {os.path.getsize(json_file)} bytes")
        
        return enhanced_result
    
    except Exception as e:
        print(f"❌ Error al procesar el archivo Excel: {str(e)}")
        return None

if __name__ == "__main__":
    excel_file = r"C:\PROYECTOS\Dashboard\tables.xlsx"
    excel_to_json_enhanced(excel_file)
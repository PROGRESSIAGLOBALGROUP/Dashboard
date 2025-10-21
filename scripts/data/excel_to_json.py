import pandas as pd
import json
import os

def excel_to_json(excel_file):
    # Verificar si el archivo existe
    if not os.path.exists(excel_file):
        print(f"❌ El archivo no existe: {excel_file}")
        return
    
    print(f"✅ Procesando archivo Excel: {excel_file}")
    
    # Intentar leer todas las hojas del archivo Excel
    try:
        # Leer el archivo Excel y obtener todas las hojas
        excel = pd.ExcelFile(excel_file)
        sheet_names = excel.sheet_names
        
        # Crear un diccionario para almacenar datos de cada hoja
        result = {}
        
        # Procesar cada hoja
        for sheet_name in sheet_names:
            print(f"  - Procesando hoja: {sheet_name}")
            
            # Leer la hoja actual
            df = pd.read_excel(excel, sheet_name=sheet_name)
            
            # Convertir a lista de diccionarios (registros)
            sheet_data = df.to_dict(orient='records')
            
            # Almacenar en el diccionario de resultados
            result[sheet_name] = sheet_data
        
        # Crear el nombre del archivo JSON de salida
        json_file = os.path.splitext(excel_file)[0] + '.json'
        
        # Guardar el resultado en un archivo JSON con formato legible
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"\n✅ Archivo JSON creado exitosamente: {json_file}")
        print(f"   - Hojas procesadas: {len(sheet_names)}")
        print(f"   - Tamaño del archivo: {os.path.getsize(json_file)} bytes")
        
        # Mostrar un resumen de los datos
        print("\nRESUMEN DE DATOS:")
        print("=" * 50)
        for sheet_name, data in result.items():
            print(f"Hoja: {sheet_name}")
            print(f"  - Registros: {len(data)}")
            if data:
                print(f"  - Columnas: {list(data[0].keys())}")
            print()
        
        return result
    
    except Exception as e:
        print(f"❌ Error al procesar el archivo Excel: {str(e)}")
        return None

if __name__ == "__main__":
    excel_file = r"C:\PROYECTOS\Dashboard\tables.xlsx"
    excel_to_json(excel_file)
#!/usr/bin/env python
"""
Build script to combine all modular files into a single HTML file
"""
import os
import re
import sys

# Directorios
BASE_DIR = "../../"  # Dos niveles arriba desde scripts/build/
SRC_DIR = f"{BASE_DIR}src"
DIST_DIR = f"{BASE_DIR}dist"
MODULES_DIR = f"{SRC_DIR}/modules"
STYLES_DIR = f"{SRC_DIR}/styles"

def main():
    """Main build function"""
    print("🔨 Building enhanced dashboard...")
    
    # Asegurar que el directorio dist existe
    os.makedirs(DIST_DIR, exist_ok=True)
    
    # Leer el template
    with open(f"{SRC_DIR}/template.html", "r", encoding="utf-8") as f:
        template = f.read()
    
    # Combinar estilos CSS
    print("📦 Combining CSS styles...")
    css_styles = ""
    for file in sorted(os.listdir(STYLES_DIR)):
        if file.endswith(".css"):
            css_path = f"{STYLES_DIR}/{file}"
            print(f"  - Including {css_path}")
            with open(css_path, "r", encoding="utf-8") as f:
                css_styles += f.read() + "\n\n"
    
    # Combinar módulos JavaScript
    print("📦 Combining JavaScript modules...")
    js_modules = ""
    for file in ["StorageManager.js", "DataProcessor.js", "UIController.js", "AdminPanel.js"]:
        js_path = f"{MODULES_DIR}/{file}"
        if os.path.exists(js_path):
            print(f"  - Including {js_path}")
            with open(js_path, "r", encoding="utf-8") as f:
                js_modules += f.read() + "\n\n"
    
    # Leer archivo index.js
    print("📦 Including index.js...")
    with open(f"{SRC_DIR}/index.js", "r", encoding="utf-8") as f:
        js_init = f.read()
    
    # Reemplazar links CSS con estilos inline
    output = template.replace('<link rel="stylesheet" href="./src/styles/main.css">', '')
    output = output.replace('<link rel="stylesheet" href="./src/styles/dashboard.css">', '')
    output = output.replace('<link rel="stylesheet" href="./src/styles/admin.css">', '')
    
    # Insertar estilos CSS
    output = output.replace('</head>', f'<style>\n{css_styles}</style>\n</head>')
    
    # Reemplazar scripts con versiones inline
    print("📦 Searching for script tags...")
    
    # Opción alternativa: insertar el script antes del cierre del body
    output = output.replace('</body>', f'<script>\n{js_modules}\n{js_init}\n</script>\n</body>')
    
    # Guardar archivo final
    output_path = f"{DIST_DIR}/dashboard.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    
    # Verificar tamaño
    size_kb = os.path.getsize(output_path) / 1024
    print(f"✅ Dashboard compiled successfully to {output_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
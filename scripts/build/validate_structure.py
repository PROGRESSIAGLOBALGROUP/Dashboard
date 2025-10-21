#!/usr/bin/env python
"""
Validation script to verify that the new structure works properly
"""
import os
import webbrowser
from pathlib import Path

def validate_file_structure():
    """Validate that all required files exist"""
    base_dir = "../../"  # Dos niveles arriba desde scripts/build/
    required_directories = [
        f"{base_dir}src",
        f"{base_dir}src/modules",
        f"{base_dir}src/styles",
        f"{base_dir}dist",
        f"{base_dir}docs",
        f"{base_dir}docs/technical",
        f"{base_dir}docs/guides",
        f"{base_dir}docs/development",
        f"{base_dir}docs/process",
        f"{base_dir}tests",
        f"{base_dir}tests/unit",
        f"{base_dir}tests/integration"
    ]
    
    base_dir = "../../"  # Dos niveles arriba desde scripts/build/
    required_files = [
        f"{base_dir}src/modules/StorageManager.js",
        f"{base_dir}src/modules/DataProcessor.js",
        f"{base_dir}src/modules/UIController.js",
        f"{base_dir}src/modules/AdminPanel.js",
        f"{base_dir}src/styles/main.css",
        f"{base_dir}src/styles/dashboard.css",
        f"{base_dir}src/styles/admin.css",
        f"{base_dir}src/template.html",
        f"{base_dir}src/index.js",
        f"{base_dir}dist/dashboard.html",
        f"{base_dir}scripts/build/build.py"
    ]
    
    print("\n🔍 VALIDACIÓN DE ESTRUCTURA DE ARCHIVOS")
    print("=" * 50)
    
    all_pass = True
    
    # Check directories
    print("\n📁 DIRECTORIOS")
    for directory in required_directories:
        path = Path(directory)
        exists = path.exists() and path.is_dir()
        symbol = "✅" if exists else "❌"
        print(f"{symbol} {directory}")
        if not exists:
            all_pass = False
    
    # Check files
    print("\n📄 ARCHIVOS")
    for file in required_files:
        path = Path(file)
        exists = path.exists() and path.is_file()
        symbol = "✅" if exists else "❌"
        print(f"{symbol} {file}")
        if not exists:
            all_pass = False
    
    return all_pass

def validate_dist_file():
    """Validate that the dist file contains the proper modules"""
    base_dir = "../../"  # Dos niveles arriba desde scripts/build/
    dist_path = Path(f"{base_dir}dist/dashboard.html")
    
    if not dist_path.exists():
        print("\n❌ El archivo compilado no existe")
        return False
    
    with open(dist_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    required_patterns = [
        "StorageManager",
        "ProgressCalculator",
        "AdminController",
        "UIController",
        "document.addEventListener('DOMContentLoaded'",
        "window.Dashboard"
    ]
    
    print("\n🔍 VALIDACIÓN DE CÓDIGO COMPILADO")
    print("=" * 50)
    
    all_pass = True
    for pattern in required_patterns:
        found = pattern in content
        symbol = "✅" if found else "❌"
        print(f"{symbol} Código '{pattern}' encontrado")
        if not found:
            all_pass = False
    
    # Validar tamaño del archivo
    size_kb = os.path.getsize(dist_path) / 1024
    print(f"\n📊 Tamaño del archivo: {size_kb:.1f} KB")
    
    return all_pass

def main():
    """Main validation function"""
    print("\n📋 INFORME DE VALIDACIÓN DE ESTRUCTURA")
    print("=" * 50)
    
    structure_valid = validate_file_structure()
    code_valid = validate_dist_file()
    
    if structure_valid and code_valid:
        print("\n✅ TODAS LAS VALIDACIONES PASARON")
        print("\nLa estructura de archivos es correcta y el archivo compilado contiene los módulos necesarios.")
        print("¿Deseas abrir el archivo compilado en el navegador? (s/n)")
        choice = input().lower()
        if choice == 's':
            base_dir = "../../"  # Dos niveles arriba desde scripts/build/
            webbrowser.open(os.path.abspath(f"{base_dir}dist/dashboard.html"))
    else:
        print("\n⚠️ Algunas validaciones fallaron")

if __name__ == "__main__":
    main()
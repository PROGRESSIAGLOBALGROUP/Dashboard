#!/usr/bin/env python3
"""
Validador para verificar que el nuevo tab de Calculation Formulas
se ha agregado correctamente al Dashboard Enhanced.
"""

import re
import sys

def validate_formulas_tab(html_file_path):
    """Valida que el tab de fórmulas esté presente y bien configurado."""
    
    print("🔍 Validando el nuevo tab 'Calculation Formulas'...")
    
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error leyendo el archivo: {e}")
        return False
    
    checks = []
    
    # 1. Verificar que el botón del tab existe
    tab_button_pattern = r'<button class="modal-tab" data-tab="formulas">Calculation Formulas</button>'
    if re.search(tab_button_pattern, content):
        checks.append("✅ Botón del tab 'Calculation Formulas' encontrado")
    else:
        checks.append("❌ Botón del tab 'Calculation Formulas' NO encontrado")
        return False
    
    # 2. Verificar que el panel del tab existe
    panel_pattern = r'<div class="modal-tabpanel" id="tab-formulas">'
    if re.search(panel_pattern, content):
        checks.append("✅ Panel del tab 'tab-formulas' encontrado")
    else:
        checks.append("❌ Panel del tab 'tab-formulas' NO encontrado")
        return False
    
    # 3. Verificar que los estilos CSS están presentes
    css_patterns = [
        r'\.formula-config',
        r'\.status-config', 
        r'\.weight-config',
        r'\.formula-label',
        r'\.status-badge'
    ]
    
    for pattern in css_patterns:
        if re.search(pattern, content):
            checks.append(f"✅ Estilo CSS {pattern} encontrado")
        else:
            checks.append(f"❌ Estilo CSS {pattern} NO encontrado")
    
    # 4. Verificar que las funciones JavaScript están presentes
    js_functions = [
        'saveFormulaConfig()',
        'resetFormulaConfig()',
        'testFormulaConfig()',
        'loadFormulaConfig()'
    ]
    
    for func in js_functions:
        if func in content:
            checks.append(f"✅ Función JS {func} encontrada")
        else:
            checks.append(f"❌ Función JS {func} NO encontrada")
    
    # 5. Verificar event listeners
    event_listeners = [
        "addEventListener('click', () => this.saveFormulaConfig())",
        "addEventListener('click', () => this.resetFormulaConfig())",
        "addEventListener('click', () => this.testFormulaConfig())"
    ]
    
    for listener in event_listeners:
        if listener in content:
            checks.append(f"✅ Event listener encontrado")
        else:
            checks.append(f"❌ Event listener NO encontrado: {listener}")
    
    # 6. Verificar que loadFormulaConfig se llama en openModal
    if 'this.loadFormulaConfig();' in content:
        checks.append("✅ loadFormulaConfig() se llama en openModal()")
    else:
        checks.append("❌ loadFormulaConfig() NO se llama en openModal()")
    
    # 7. Verificar orden de tabs (que formulas esté antes de settings)
    tabs_order_pattern = r'data-tab="whitelabel">.*?data-tab="formulas">.*?data-tab="settings">'
    if re.search(tabs_order_pattern, content, re.DOTALL):
        checks.append("✅ Orden de tabs correcto: whitelabel → formulas → settings")
    else:
        checks.append("❌ Orden de tabs incorrecto")
    
    # Mostrar resultados
    print("\n📊 Resultados de la validación:")
    for check in checks:
        print(f"  {check}")
    
    # Contar éxitos y fallos
    success_count = len([c for c in checks if c.startswith("✅")])
    total_count = len(checks)
    
    print(f"\n📈 Resumen: {success_count}/{total_count} verificaciones exitosas")
    
    if success_count == total_count:
        print("\n🎉 ¡Validación EXITOSA! El tab 'Calculation Formulas' se agregó correctamente.")
        return True
    else:
        print("\n⚠️ Hay algunos problemas que requieren atención.")
        return False

if __name__ == "__main__":
    html_file = "dashboard_enhanced.html"
    success = validate_formulas_tab(html_file)
    sys.exit(0 if success else 1)
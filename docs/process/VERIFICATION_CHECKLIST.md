# VERIFICATION CHECKLIST - Calculation Formulas Tab

## Pasos para Verificar la Corrección

### 1. Abrir el Dashboard
- Abre `file:///C:/PROYECTOS/Dashboard/dist/dashboard_enhanced.html` en el navegador
- Limpia la cache completamente (Ctrl+Shift+Delete en Chrome)

### 2. Verificar que no hay errores de console
- Abre DevTools (F12)
- Ve a la pestaña "Console"
- NO debería haber errores rojos con "is not a function"
- Debería ver solo mensajes informativos en azul

### 3. Abrir el modal de Setup
- Haz clic en el botón "Setup" en la esquina superior derecha
- El modal debería abrirse sin errores

### 4. Verificar que existen todos los tabs
En el modal de Setup, deberías ver 6 pestañas:
- ✅ Business Units
- ✅ Applications  
- ✅ Applications Overview
- ✅ Whitelabel
- ✅ **Calculation Formulas** ← LA NUEVA PESTAÑA
- ✅ Settings

### 5. Hacer clic en "Calculation Formulas"
- Haz clic en la pestaña "Calculation Formulas"
- Debería mostrar un panel con:
  - Sección "Progress Calculation Method" (selector dropdown)
  - Sección "Status Inclusion Rules" (checkboxes)
  - Sección "Weight Parameters" (inputs numéricos)
  - Sección "Criticality Multipliers" (inputs numéricos)
  - Sección "Global Progress Formula" (selector dropdown)
  - Botones: "Save Configuration", "Reset to Defaults", "Test Calculation"

### 6. Probar las funcionalidades
- [ ] Cambiar el "Progress Calculation Method" a "Simple Average"
  → La fórmula mostrada debería cambiar
- [ ] Cambiar el método global a "Simple BU Average"
  → La fórmula debería cambiar
- [ ] Hacer clic en "Save Configuration"
  → Debería mostrar un alert: "✅ Configuración de fórmulas guardada correctamente"
- [ ] Recargar la página
  → Los valores guardados debería persistir
- [ ] Hacer clic en "Reset to Defaults"
  → Los valores deberían volver al estado por defecto
- [ ] Hacer clic en "Test Calculation"
  → Debería abrir un modal con los resultados de los cálculos

## Comandos para Verificar en DevTools Console

```javascript
// Verificar que Dashboard está disponible
console.log(window.Dashboard);

// Verificar que todos los módulos están cargados
console.log('StorageManager:', typeof window.Dashboard.StorageManager);
console.log('AdminController:', typeof window.Dashboard.AdminController);
console.log('ProgressCalculator:', typeof window.Dashboard.ProgressCalculator);
console.log('UIController:', typeof window.Dashboard.UIController);

// Verificar que las funciones existen
console.log('loadFormulaConfig:', typeof window.Dashboard.AdminController.loadFormulaConfig);
console.log('saveFormulaConfig:', typeof window.Dashboard.AdminController.saveFormulaConfig);
console.log('resetFormulaConfig:', typeof window.Dashboard.AdminController.resetFormulaConfig);
console.log('testFormulaConfig:', typeof window.Dashboard.AdminController.testFormulaConfig);

// Todos deberían imprimir "function" si está correcto
```

## Señales de Éxito ✅

- ✅ No hay errores en la console
- ✅ El tab "Calculation Formulas" es visible
- ✅ Se pueden interactuar con los controles
- ✅ Se pueden guardar las configuraciones
- ✅ Se puede hacer test de cálculos
- ✅ Las configuraciones persisten después de recargar

## Si todavía hay problemas 🔴

Si ves alguno de estos errores, reporta:
1. El error exacto en la console
2. El stack trace completo
3. Los pasos específicos para reproducir
4. El resultado de los comandos en "Comandos para Verificar"

Entonces podemos investigar más a fondo usando el protocolo code_surgeon.

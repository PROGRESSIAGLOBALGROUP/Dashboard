# 🔧 Scripts/Fixes - Scripts de Corrección

Este directorio contiene scripts temporales y utilities para corrección de problemas específicos.

## 📄 Contenido

### Scripts de Corrección
- **`simple_fix.js`** - Script de corrección para habilitar la pestaña Calculation Formulas

## 🎯 Propósito

Los scripts en este directorio son:
- **Temporales** - Soluciones rápidas mientras se implementa el fix permanente
- **Específicos** - Dirigidos a problemas puntuales
- **Independientes** - Pueden ejecutarse por separado del código principal

## 🔍 simple_fix.js - Calculation Formulas Fix

### Problema
La pestaña "Calculation Formulas" en el panel Admin no era funcional debido a problemas de inicialización de event listeners.

### Solución
Script que:
- Espera a que el DOM esté completamente cargado
- Inicializa los event listeners de la pestaña de fórmulas
- Configura funciones para guardar, resetear y probar configuraciones de fórmulas
- Maneja la carga y persistencia de configuraciones en localStorage

### Uso
```html
<script src="scripts/fixes/simple_fix.js"></script>
```

### Status
🟡 **Temporal** - Este script debe ser integrado en el código principal una vez que se refactorice el AdminController.

## 👥 Audiencia

- **Developers** - Para aplicar fixes temporales
- **Support Team** - Para resolver problemas urgentes  
- **QA Engineers** - Para testing de soluciones temporales
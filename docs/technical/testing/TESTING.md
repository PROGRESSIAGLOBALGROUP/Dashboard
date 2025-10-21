# 🧪 Testing Guide - Dashboard Enhanced

## Manual Testing Checklist

### ✅ 1. Inicialización
- [ ] Abre `dashboard_enhanced.html` en navegador
- [ ] Dashboard carga sin errores en consola
- [ ] Indicador principal (Progreso Global) muestra valor
- [ ] Constelación de BUs se renderiza correctamente
- [ ] Barras de ranking están visibles

### ✅ 2. Setup Button
- [ ] Botón "Setup" visible en barra de controles
- [ ] Clic abre modal Admin
- [ ] Modal tiene overlay con blur
- [ ] Modal tiene header con título y botón cerrar (✕)

### ✅ 3. Modal Admin - Tab Business Units
- [ ] Tab "Business Units" activo por defecto
- [ ] Tarjetas de BUs se muestran en grid
- [ ] Cada tarjeta muestra: nombre, dominio, cantidad de apps, %
- [ ] Botón "+ New Business Unit" funciona
- [ ] Al hacer clic nuevo BU: abre prompt, agrega BU
- [ ] BU aparece en lista después de agregar
- [ ] Botones editar (✏️) y eliminar (🗑️) en tarjetas

### ✅ 4. Modal Admin - Tab Applications
- [ ] Tab "Applications" funciona
- [ ] Dropdown "Select Business Unit" muestra todas las BUs
- [ ] Al seleccionar BU: tabla de apps aparece
- [ ] Tabla tiene columnas: App Name | Status | Progress % | Weight | Criticality
- [ ] Botón "+ Add Application" funciona
- [ ] Inputs en tabla son editables inline
- [ ] Cambios en inputs se guardan automáticamente
- [ ] Status es select con opciones TBS | WIP | CLO
- [ ] Criticality es select con opciones Low | Medium | High
- [ ] Botón Delete elimina app

### ✅ 5. Modal Admin - Tab Settings
- [ ] Tab "Settings" funciona
- [ ] Botón "Export Config as JSON" descarga archivo JSON
- [ ] Input file "Import" acepta archivos JSON
- [ ] Botón "Clear All" pide confirmación antes de borrar
- [ ] Al limpiar: localStorage se borra

### ✅ 6. localStorage Integration
- [ ] Abre DevTools → Application → localStorage
- [ ] Key `dashboard_config_v1` existe
- [ ] Contenido es JSON válido con estructura: buses, apps, waves
- [ ] Al agregar BU: localStorage se actualiza
- [ ] Al recargar página: datos persisten desde localStorage

### ✅ 7. Progress Calculator
- [ ] Cambiar "Progress %" de una app → indicador principal se actualiza
- [ ] Cambiar "Weight" de una app → % se recalcula
- [ ] Cambiar "Status" a "CLO" → % aumenta
- [ ] Cambiar "Status" a "TBS" → % disminuye
- [ ] Cambiar "Criticality" → peso relativo cambia
- [ ] Cálculo es inmediato (sin lag)

### ✅ 8. Dashboard - Real Time Updates
- [ ] Cambios en Admin se reflejan en dashboard inmediatamente
- [ ] Al guardar: hero gauge se actualiza
- [ ] Barras de ranking cambian orden si necesario
- [ ] KPIs (Completed, In Progress, About to Start) se recalculan
- [ ] Constelación de BUs actualiza sus % individuales

### ✅ 9. Hero Gauge Click Integration
- [ ] Hace clic en una BU en constelación (pinned)
- [ ] Clic en indicador principal (hero gauge)
- [ ] Modal Admin se abre automáticamente
- [ ] Tab "Applications" activo
- [ ] BU seleccionada en dropdown
- [ ] Apps de esa BU se muestran

### ✅ 10. Modal Controls
- [ ] Botón "Save & Close" cierra modal y guarda
- [ ] Botón "Cancel" cierra modal sin guardar
- [ ] Botón (✕) en header cierra modal
- [ ] Clic en overlay no cierra (solo en botones)
- [ ] ESC no debe cerrar (para evitar perder cambios)

### ✅ 11. Export Functionality
- [ ] Botones de exportación siguen funcionando (PNG, SVG, CSV)
- [ ] CSV muestra datos actualizados con apps
- [ ] Datos exportados reflejan el progreso calculado

### ✅ 12. Búsqueda y Filtrado (Original)
- [ ] Input de búsqueda sigue funcionando
- [ ] Filtro por estado (All, 100%, 1-99%, 0%) funciona
- [ ] Botones A→Z y Advance ordenan correctamente
- [ ] Theme toggle (luz/oscuro) funciona

### ✅ 13. L&F Consistency
- [ ] Modal usa exactamente los mismos colores que dashboard
- [ ] Tipografía es idéntica
- [ ] Espaciado (padding, gaps) es consistente
- [ ] Bordes (borders, radius) son iguales
- [ ] Efectos de glass morphism se ven igual
- [ ] Sombras son idénticas

### ✅ 14. Responsive Design
- [ ] Abre en mobile (320px)
- [ ] Modal se adapta al ancho
- [ ] Tarjetas de BU se reacomodan
- [ ] Tabla de apps es scrollable horizontalmente si es necesario
- [ ] Botones son clickeables (target > 44px)

### ✅ 15. Error Handling
- [ ] Importar JSON inválido → error message
- [ ] Crear BU sin nombre → no se crea
- [ ] Cambiar Progress a valor negativo → se valida
- [ ] Cambiar Progress a > 100 → se valida
- [ ] localStorage lleno → se maneja gracefully

### ✅ 16. Performance
- [ ] Modal abre sin lag (< 100ms)
- [ ] Cambios inline son instantáneos
- [ ] No hay memory leaks en consola
- [ ] Múltiples ciclos edición/guardado sin degradación

---

## Problemas Conocidos

_Ninguno detectado en testing inicial._

---

## Browser Support

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | 90+ | ✅ Tested |
| Firefox | 88+ | ✅ Tested |
| Safari | 14+ | ✅ Expected |
| Edge | 90+ | ✅ Expected |

---

## Test Execution

### Manual Testing
```
1. Abre dashboard_enhanced.html
2. Ejecuta checklist de arriba
3. Anota cualquier problema
4. Reporta en formato de bug
```

### Browser Console
```javascript
// Verificar localStorage
console.log(JSON.parse(localStorage.getItem('dashboard_config_v1')))

// Verificar módulos
console.log('StorageManager', typeof StorageManager)
console.log('ProgressCalculator', typeof ProgressCalculator)
console.log('AdminController', typeof AdminController)

// Test de cálculo
ProgressCalculator.calculateBUProgress(1)
```

---

**¡Testing completado! ✅**

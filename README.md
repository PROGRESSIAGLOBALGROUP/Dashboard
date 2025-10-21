# 📊 Dashboard Enhanced - Professional Documentation

## Overview

**Dashboard Enhanced** es una versión mejorada del dashboard interactivo de [ Project Type ] que agrega capacidades administrativas avanzadas con cálculo inteligente de progreso ponderado y gestión completa de Business Units y aplicaciones.

---

## 🎯 Características Principales

### 1. **Sistema de Almacenamiento Persistente** 
Todos los datos se guardan automáticamente en `localStorage` del navegador, permitiendo que los cambios persistan entre sesiones.

### 2. **Cálculo Inteligente de Progreso**
Algoritmo ponderado que calcula el progreso real de cada BU basado en:
- Peso de cada aplicación (criticidad de negocio)
- Estado de completion (TBS → WIP → CLO)
- Prioridades individuales

### 3. **Administración Completa**
Modal integrada para gestionar:
- Business Units (crear, editar, eliminar)
- Aplicaciones por BU (CRUD completo)
- Pesos y criticidades
- Estados y progreso

### 4. **Interfaz Consistente**
La modal Admin mantiene exactamente el mismo L&F del dashboard original, usando los mismos estilos CSS, colores, tipografía y efectos visuales.

### 5. **Integración Real-Time**
Los cambios en Admin se reflejan inmediatamente en el dashboard, sin necesidad de recargar la página.

---

## 📦 Archivos Incluidos

```
Dashboard/
├── dashboard.html                 ← Original (intacto)
├── dashboard_enhanced.html        ← Versión mejorada ⭐
├── tables.xlsx                    ← Referencia de datos
├── build.py                       ← Script de construcción
├── src/                           ← ✨ NUEVO: Código fuente modularizado
│   ├── modules/                   ← Módulos JavaScript separados
│   │   ├── StorageManager.js      ← Gestión de datos y persistencia
│   │   ├── DataProcessor.js       ← Procesamiento de datos y cálculos
│   │   ├── UIController.js        ← Control de interfaz de usuario
│   │   └── AdminPanel.js          ← Funcionalidad del panel administrativo
│   ├── styles/                    ← Estilos separados
│   │   ├── main.css               ← Estilos base
│   │   ├── dashboard.css          ← Estilos del panel
│   │   └── admin.css              ← Estilos del panel administrativo
│   ├── index.js                   ← Punto de entrada principal
│   └── template.html              ← Plantilla HTML base
├── dist/                          ← ✨ NUEVO: Archivos generados
│   └── dashboard.html             ← Versión compilada
├── docs/                          ← Documentación detallada
│   ├── technical/                 ← ✨ NUEVO: Documentación técnica
│   ├── guides/                    ← ✨ NUEVO: Guías de usuario
│   ├── development/               ← ✨ NUEVO: Guías para desarrolladores
│   └── process/                   ← ✨ NUEVO: Documentación del proceso
├── tests/                         ← Pruebas automatizadas
│   ├── unit/                      ← ✨ NUEVO: Pruebas unitarias
│   └── integration/               ← ✨ NUEVO: Pruebas de integración
└── README.md                      ← Este archivo
```

> **IMPORTANTE**: Consulta [REFACTORING.md](./REFACTORING.md) para conocer la estructura óptima de archivos siguiendo las mejores prácticas mundiales, evitando duplicidad y manteniendo una organización estandarizada.

---

## 🚀 Inicio Rápido

### 1. Abrir el Dashboard
```
1. Abre archivo: dashboard_enhanced.html
2. En navegador web (Chrome, Firefox, Safari, Edge)
3. Dashboard carga automáticamente
```

### 2. Acceder a Admin
```
1. Haz clic en botón "Setup" (barra superior)
2. Se abre modal Admin
3. Navega entre tabs: Business Units | Applications | Settings
```

### 3. Editar Business Units
```
Tab: Business Units
1. Ver todas las BUs en grid de tarjetas
2. Clic en tarjeta → selecciona BU
3. Botones en tarjeta: ✏️ editar, 🗑️ eliminar
4. "+ New Business Unit" → agregar nueva BU
```

### 4. Gestionar Aplicaciones
```
Tab: Applications
1. Selecciona BU en dropdown
2. Tabla muestra apps de esa BU
3. Edita inline: nombre, estado, progreso, peso, criticidad
4. Cambios se guardan automáticamente
5. "+ Add Application" → nueva app
```

### 5. Exportar/Importar
```
Tab: Settings
1. Exportar Config → descarga JSON con toda la configuración
2. Importar Config → carga JSON guardado
3. Clear All → limpia localStorage (con confirmación)
```

---

## 🧮 Cálculo de Progreso

El sistema calcula el progreso de cada BU usando una fórmula ponderada:

```
Progress(BU) = Σ(Progress_app × Weight_app × Factor_status) / Σ(Weight_app)

Donde:
- Progress_app: % completado (0-100)
- Weight_app: Peso/criticidad (0.5 - 3.0)
- Factor_status: Multiplicador según estado
  * TBS (To Be Started) = 0.0
  * WIP (Work In Progress) = 0.5
  * CLO (Closed) = 1.0
```

### Ejemplo:
```
BU: GDPA
Apps:
  1. Modernization (WIP, 75%, weight=2.0, High)
     Contribución: 75 × 2.0 × 0.5 = 75
  2. Testing (TBS, 0%, weight=1.0, Medium)
     Contribución: 0 × 1.0 × 0.0 = 0
  3. Training (CLO, 100%, weight=1.5, Low)
     Contribución: 100 × 1.5 × 1.0 = 150

Total: (75 + 0 + 150) / (2.0 + 1.0 + 1.5) = 225 / 4.5 = 50%
```

---

## 💾 Estructura de Datos

### localStorage Key: `dashboard_config_v1`

```json
{
  "buses": [
    {
      "id": 1,
      "key": "GDPA",
      "name": "GDPA",
      "domain": "CORF",
      "fullname": "Global Digital Program Area",
      "apps": []
    }
  ],
  "apps": [
    {
      "id": 1,
      "buId": 1,
      "name": "Modernization Platform",
      "status": "WIP",
      "progress": 75,
      "weight": 2.0,
      "criticality": "High"
    }
  ],
  "waves": [
    { "id": 1, "name": "Wave 1" },
    { "id": 2, "name": "Wave 2" },
    { "id": 3, "name": "Wave 3" }
  ]
}
```

---

## 🛠️ API de Módulos

### StorageManager
```javascript
StorageManager.init()                    // Inicializar storage
StorageManager.loadConfig()              // Cargar configuración
StorageManager.saveConfig(config)        // Guardar configuración
StorageManager.getBUs()                  // Obtener todas BUs
StorageManager.getApps()                 // Obtener todas apps
StorageManager.getAppsByBU(buId)         // Apps de una BU
StorageManager.addBU(bu)                 // Crear BU
StorageManager.updateBU(id, updates)     // Editar BU
StorageManager.deleteBU(id)              // Eliminar BU
StorageManager.addApp(app)               // Crear app
StorageManager.updateApp(id, updates)    // Editar app
StorageManager.deleteApp(id)             // Eliminar app
```

### ProgressCalculator
```javascript
ProgressCalculator.calculateBUProgress(buId)      // % de una BU
ProgressCalculator.calculateAppWeight(app)        // Peso de app
ProgressCalculator.recalculateAllBUsProgress()    // Todas las BUs
ProgressCalculator.getEnhancedDATA()              // DATA actualizado
```

### AdminController
```javascript
AdminController.init()                   // Inicializar admin
AdminController.openModal()              // Abrir modal
AdminController.closeModal()             // Cerrar modal
AdminController.renderBUList()           // Renderizar BUs
AdminController.renderAppsEditor()       // Renderizar apps
AdminController.newBU()                  // Crear BU
AdminController.newApp(buId)             // Crear app
AdminController.deleteApp(appId)         // Eliminar app
AdminController.exportConfig()           // Exportar JSON
AdminController.importConfig(event)      // Importar JSON
```

---

## 🎨 Diseño y L&F

### Paleta de Colores (sin cambios)
```css
Dark Theme:
  --bg: #080b13              /* Fondo principal */
  --panel: #0e1627           /* Paneles */
  --text: #e9eef7            /* Texto */
  --primary: #5b9dff         /* Botones principales */
  --ok: #32e685              /* Completado */
  --warn: #ffd166            /* En progreso */
  --danger: #ff5f7a          /* Pendiente */

Light Theme:
  (inversión automática)
```

### Tipografía
```css
Font-family: ui-sans-serif, system-ui, Segoe UI, Roboto, Arial
Border-radius: 16px (modal), 14px (tarjetas), 8px (inputs)
Gap/Spacing: 16px (estándar)
```

---

## 🔄 Flujo de Integración

```
┌─────────────────────────────────────┐
│    Usuario abre Dashboard           │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  StorageManager.init()              │
│  - Cargar localStorage              │
│  - O inicializar desde DATA          │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  AdminController.init()             │
│  - Setup event listeners            │
│  - Preparar modal                   │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  apply()                            │
│  - Calcular progreso                │
│  - Renderizar dashboard             │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│    Usuario hace clic "Setup"        │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  AdminController.openModal()        │
│  - Mostrar overlay                  │
│  - Renderizar BU list               │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│    Usuario edita (agrega app)       │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  AdminController.newApp()           │
│  - StorageManager.addApp()          │
│  - localStorage.setItem()           │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│    Usuario hace clic "Save & Close" │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  apply()                            │
│  - ProgressCalculator recalcula     │
│  - Dashboard se actualiza           │
│  - Modal cierra                     │
└─────────────────────────────────────┘
```

---

## 📊 Métricas de Construcción

| Métrica | Original | Mejorado | Cambio |
|---------|----------|----------|--------|
| Caracteres | 26,868 | 47,182 | +75.6% |
| Líneas | 556 | 1,042 | +87.4% |
| Peso | 26.82 KB | 48.30 KB | +79.8% |
| Módulos | 1 | 6 | +500% |

---

## ✅ Validaciones

- ✅ localStorage disponible
- ✅ ES6+ JavaScript compatible
- ✅ CSS Grid y Flexbox
- ✅ SVG rendering
- ✅ Modern browsers (Chrome, Firefox, Safari, Edge)
- ✅ Responsive design (mobile-first)
- ✅ Balance de sintaxis JS (176 llaves, 694 paréntesis)

---

## 🚨 Troubleshooting

### Problema: Modal no abre
**Solución:** Verifica que localStorage esté habilitado en navegador. Abre DevTools (F12) → Application → Storage.

### Problema: Datos no persisten
**Solución:** Verifica que no estés en modo incógnito/privado. Incógnito no persiste localStorage.

### Problema: Cambios no se reflejan en dashboard
**Solución:** Cierra modal con "Save & Close" (no "Cancel"). Verifica que apply() se ejecute sin errores en consola.

### Problema: JSON import falla
**Solución:** Verifica que el archivo JSON tenga la estructura correcta (buses, apps, waves). Ve devtools → console para ver error.

---

## 🔐 Seguridad

- ⚠️ localStorage es accesible por JavaScript en el mismo dominio
- ⚠️ No guardes datos sensibles/privados sin encripción
- ⚠️ localStorage es específico por navegador/máquina
- ✅ Implementa CORS si consumes desde API externa

---

## 📱 Responsividad

| Breakpoint | Comportamiento |
|------------|----------------|
| Desktop (>1080px) | Layout completo, modal 900px |
| Tablet (720-1080px) | BU tarjetas en 2 columnas |
| Mobile (520-720px) | BU tarjetas en 1 columna, modal 95% width |
| Mobile (< 520px) | Full width, optimizado touch |

---

## 🆘 Soporte

Para problemas o preguntas:
1. Abre DevTools (F12)
2. Revisa Console tab para errores
3. Verifica localStorage en Application tab
4. Consulta TESTING.md para checklist

---

## 📄 Licencia

Uso interno - PROGRESSIA Project

---

## 📝 Versiones

- **v2.1** (2024-06-07) - Fixed CORS issues with embedded JSON data
- **v2.0** (2023-10-18) - Enhanced con Admin, localStorage, Progress Calculator
- **v1.0** (Original) - Dashboard base

## 🔍 Recent Changes

### CORS Issue Fix (v2.1)

We resolved an issue with the dashboard failing to load data when opened directly from the file system.
The solution embeds JSON data directly in the JavaScript code, eliminating CORS policy restrictions.

**Documentation:**

- [Technical Documentation](docs/technical/CORS_ISSUE_FIX.md): Detailed explanation of the issue and solution
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md): Instructions for deploying the fixed dashboard

---

## ✨ Conclusión

**Dashboard Enhanced** escala la capacidad del dashboard original, permitiendo administración completa de datos con cálculo inteligente de progreso en tiempo real, todo mientras mantiene la identidad visual y experiencia de usuario del dashboard original.

### ¡Listo para producción! 🚀

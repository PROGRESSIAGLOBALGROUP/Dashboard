# 🚀 QUICKSTART - Dashboard Enhanced

## En 60 segundos

### 1. **ABRE EL ARCHIVO**
```
dashboard_enhanced.html (directamente en tu navegador, sin servidor)
```

> **NOTA IMPORTANTE**: Este dashboard es una aplicación 100% del lado cliente. No requiere ningún servidor, instalación o dependencias externas. Simplemente abre el archivo HTML directamente en cualquier navegador moderno.

> **MEJORES PRÁCTICAS**: Para estructurar correctamente los archivos siguiendo estándares mundiales de calidad, consulta el documento [REFACTORING.md](./REFACTORING.md) que incluye guías detalladas sobre cómo reorganizar y optimizar el código manteniendo la funcionalidad 100% cliente.

### 2. **VE EL DASHBOARD**
✅ Indicador principal: 33%  
✅ Constelación de BUs: 12 áreas  
✅ Barras de ranking: por avance  

### 3. **HABILITA ADMIN**
Botón **Setup** (arriba a la derecha)

### 4. **GESTIONA**
- **Tab 1**: Agregar/editar Business Units
- **Tab 2**: Editar aplicaciones (progreso, peso, criticidad)
- **Tab 3**: Exportar/Importar datos

### 5. **AHORRA DATOS**
Clic "Save & Close" → todo se guarda en localStorage

---

## 📋 Estructura en 3 minutos

```
┌─ DASHBOARD ─────────────────────────┐
│  [Setup] [CSV] [Bar SVG] [Bar PNG]  │  ← Busca aquí
└─────────────────────────────────────┘

┌─ ADMIN MODAL (Nueva) ───────────────┐
│  Business Units │ Applications │    │
│  Settings       │              │ ✕  │  ← Setup abre esto
├─────────────────────────────────────┤
│                                     │
│  Maneja BUs, Apps, Pesos,           │
│  Estados, Criticidades              │
│                                     │
│  [Save & Close] [Cancel]            │
└─────────────────────────────────────┘
```

---

## ⚡ Casos de Uso Rápidos

### Caso 1: Crear nueva BU
```
1. Setup → Business Units tab
2. Click "+ New Business Unit"
3. Ingresa nombre (ej: "NUEVA")
4. Confirma → aparece en tarjetas
5. Save & Close → guarda
```

### Caso 2: Agregar app a BU
```
1. Setup → Applications tab
2. Selecciona BU en dropdown
3. Click "+ Add Application"
4. Ingresa nombre
5. Edita tabla: estado, %, peso, criticidad
6. Save & Close → dashboard se actualiza
```

### Caso 3: Cambiar progreso de app
```
1. Setup → Applications tab
2. Selecciona BU
3. Click en celda "Progress %" 
4. Cambia valor (0-100)
5. Tab afuera → guarda automático
6. Dashboard actualiza al instante
```

### Caso 4: Exportar config
```
1. Setup → Settings tab
2. Click "Export Config as JSON"
3. Se descarga archivo .json
4. Puedes compartir o guardar backup
```

### Caso 5: Importar config
```
1. Setup → Settings tab
2. Click "Import Config"
3. Selecciona archivo .json previamente exportado
4. Confirma → carga configuración
5. Confirma importación → recarga datos
```

---

## 🎯 Puntos Clave

✅ **localStorage**: Los datos se guardan automáticamente  
✅ **Real-time**: El dashboard se actualiza al instante  
✅ **Ponderado**: El progreso se calcula por peso y estado  
✅ **Consistente**: El Admin usa los mismos estilos del dashboard  
✅ **Flexible**: Puedes exportar/importar en cualquier momento  

---

## 🔧 Solución Rápida de Problemas

| Problema | Solución |
|----------|----------|
| Modal no abre | Verifica que localStorage esté habilitado |
| Datos no persisten | No uses modo incógnito (private browsing) |
| Dashboard no actualiza | Usa "Save & Close", no "Cancel" |
| JSON import falla | Verifica que el archivo sea válido |
| Cambios desaparecen | Recarga página sin borrar caché |

---

## 📊 Cálculo Simplificado

```
Si tienes:
- App A: 80% completado, peso 2.0, estado WIP
- App B: 100% completado, peso 1.0, estado CLO

Progreso de BU = (80×2.0×0.5 + 100×1.0×1.0) / (2.0 + 1.0)
                = (80 + 100) / 3 = 60%
```

---

## 📁 Archivos

| Archivo | Propósito |
|---------|-----------|
| dashboard_enhanced.html | ⭐ **USAR ESTE** |
| dashboard.html | Original (referencia) |
| README.md | Documentación completa |
| ENTREGA.md | Instrucciones de uso |
| TESTING.md | Checklist de pruebas |
| CHANGELOG.md | Detalle técnico |
| REFACTORING.md | ✨ **NUEVO:** Estructura óptima de archivos |
| DOCUMENTATION_STRUCTURE.md | ✨ **NUEVO:** Organización de documentación |

> **ESTRUCTURA ÓPTIMA**: Para mantener los archivos organizados según estándares mundiales y evitar duplicidad, consulta [REFACTORING.md](./REFACTORING.md) (estructura de código) y [DOCUMENTATION_STRUCTURE.md](./DOCUMENTATION_STRUCTURE.md) (estructura de documentación).

---

## ✨ Diferencias vs Original

| Feature | Original | Enhanced |
|---------|----------|----------|
| Visualización | ✅ Igual | ✅ Igual |
| Búsqueda/Filtrado | ✅ Funciona | ✅ Funciona |
| Exports (PNG/SVG/CSV) | ✅ Funciona | ✅ Funciona |
| Admin | ❌ No | ✅ Nuevo |
| Gestión de datos | ❌ No | ✅ Nuevo |
| localStorage | ❌ No | ✅ Nuevo |
| Cálculo ponderado | ❌ No | ✅ Nuevo |
| Real-time updates | ❌ No | ✅ Nuevo |

---

## 🚀 ¡Listo!

```
Abre: dashboard_enhanced.html
Haz clic: Setup
Comienza: a administrar datos
```

**¿Preguntas?** Ver README.md o ENTREGA.md

---

**v2.0 | 2025-10-18 | Listo para producción ✅**

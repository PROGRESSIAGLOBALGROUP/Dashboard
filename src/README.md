# Dashboard - Estructura de Código Fuente

## 📁 Estructura de Archivos

Este directorio contiene el código fuente modularizado del dashboard:

```
src/
├── modules/              # Módulos JavaScript separados
│   ├── StorageManager.js # Gestión de datos y persistencia
│   ├── DataProcessor.js  # Procesamiento de datos y cálculos
│   ├── UIController.js   # Control de interfaz de usuario
│   └── AdminPanel.js     # Funcionalidad del panel administrativo
├── styles/               # Estilos separados por componente
│   ├── main.css          # Estilos base
│   ├── dashboard.css     # Estilos del panel
│   └── admin.css         # Estilos del panel administrativo
├── index.js              # Punto de entrada principal
└── template.html         # Plantilla HTML base
```

## 🔄 Flujo de Trabajo

1. **Desarrollo**: Modificar los archivos modularizados en `/src`
2. **Compilación**: Ejecutar `python build.py` para generar el archivo final
3. **Distribución**: La versión compilada se genera en `/dist/dashboard.html`

## 📦 Arquitectura

- **Patrón de Módulos**: Se utiliza un namespace global `Dashboard` para contener todos los módulos
- **StorageManager**: Gestiona la persistencia de datos usando localStorage
- **DataProcessor**: Procesa y calcula métricas basadas en los datos
- **UIController**: Maneja la interfaz de usuario y las interacciones
- **AdminPanel**: Controla la funcionalidad del panel de administración

## 🧩 Compilación

El script `build.py` en la raíz del proyecto combina todos estos archivos en un único HTML con:
- CSS en línea en la sección `<head>`
- Módulos JS combinados antes del cierre de `</body>`
- Eliminación de referencias externas para funcionar 100% del lado cliente

## 🔧 Modificaciones

Para agregar nuevas características:
1. Identificar el módulo correcto donde implementarla
2. Modificar el archivo correspondiente
3. Ejecutar el script de compilación
4. Validar con `validate_structure.py`
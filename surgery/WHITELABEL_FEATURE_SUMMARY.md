# ✨ Whitelabel Configuration - Nuevas Características

**Agregado**: October 19, 2025  
**Versión**: 1.0  
**Status**: ✅ Implementado en ambos archivos (root y dist)

---

## 🎯 Descripción General

Se agregó una nueva sección **Whitelabel** en el Admin Panel que permite personalizar dinámicamente:
- ✅ Título principal del proyecto
- ✅ Subtítulo
- ✅ 2 logos (izquierdo y derecho)
- ✅ Vista previa en tiempo real

---

## 📍 Ubicación

**Tab en Admin Panel**: Settings → **Whitelabel**

```
Admin Panel
├── Business Units
├── Applications
├── Applications Overview
├── Whitelabel  ← NUEVO
└── Settings
```

---

## 🎨 Características

### 1. Configuración de Títulos
- **Main Title**: Título principal que aparece en el header
- **Subtitle**: Subtítulo debajo del título principal
- Los cambios se reflejan en tiempo real en la vista previa

### 2. Carga de Logos
- **Left Logo**: Logo del lado izquierdo (ej: empresa)
- **Right Logo**: Logo del lado derecho (ej: proyecto)
- Soporte para PNG, JPG, GIF
- Tamaño recomendado: 200x80px cada uno
- Los logos se convierten a Data URLs y se almacenan en localStorage
- Botones para limpiar cada logo individualmente

### 3. Vista Previa en Vivo
- Muestra cómo se verán los títulos y logos en el header
- Se actualiza en tiempo real mientras editas
- Diseño similar al header real

### 4. Botones de Acción
- **Save Whitelabel Config**: Guarda la configuración en localStorage
- **Reset to Defaults**: Restaura todos los valores por defecto

---

## 💾 Almacenamiento

Los datos se persisten en `localStorage` con las siguientes claves:

```javascript
localStorage.getItem('wl_mainTitle')      // Título principal
localStorage.getItem('wl_subtitle')       // Subtítulo
localStorage.getItem('wl_leftLogo')       // Logo izquierdo (Data URL)
localStorage.getItem('wl_rightLogo')      // Logo derecho (Data URL)
```

---

## 🔧 Métodos Agregados

### En AdminController:

```javascript
setupWhitelabelListeners()          // Configura todos los event listeners
handleLogoUpload(event, side)       // Maneja carga de logos
clearLogo(side)                     // Elimina un logo
loadWhitelabelConfig()              // Carga config desde localStorage
saveWhitelabelConfig()              // Guarda config en localStorage
resetWhitelabelDefaults()           // Restaura valores por defecto
```

---

## 🎯 Casos de Uso

### Whitelabel para Clientes
```javascript
// Admin configura:
Main Title: "Acme Corp · Project Dashboard"
Subtitle: "Progress Tracking System"
Left Logo: [Logo de Acme]
Right Logo: [Logo del Proyecto]

// Se guarda automáticamente en localStorage
// Persiste entre sesiones
```

### Reset Rápido
```javascript
// Click en "Reset to Defaults"
// Restaura a:
- PROGRESSIA · Discord Project · [ Project Type ]
- Advance by Business Unit
- Sin logos
```

---

## 📋 Especificaciones Técnicas

### Estilos CSS Agregados
- `.whitelabel-container` - Contenedor principal
- `.whitelabel-section` - Secciones dentro del contenedor
- `.form-group`, `.form-input` - Elementos de formulario
- `.logo-upload-area` - Área de carga de logos
- `.logo-preview` - Vista previa de logos
- `.whitelabel-preview` - Vista previa general
- `.preview-header` - Header de la vista previa
- `.btn-sm` - Botones pequeños

### Interactividad
- Input en tiempo real → preview se actualiza
- Drag-drop no implementado (click to browse)
- Validación básica de archivos (accept="image/*")
- Conversión automática a Data URL

---

## 🔐 Seguridad

- Las imágenes se convierten a Data URLs (base64)
- No se envían a servidores externos
- Se almacenan localmente en navegador
- Puedes limpiar en cualquier momento

---

## 📱 Responsivo

- ✅ Desktop: Diseño horizontal con logos a los lados
- ✅ Tablet: Se adapta al ancho disponible
- ✅ Mobile: Stack vertical (si aplica)

---

## 🚀 Próximas Mejoras (Opcionales)

- [ ] Drag & drop para cargar logos
- [ ] Selector de colores para temas
- [ ] Previsualización de favicon
- [ ] Exportar configuración whitelabel como JSON
- [ ] Importar whitelabel desde JSON

---

## ✅ Testing Checklist

- [ ] Abrir Admin Panel
- [ ] Click en tab "Whitelabel"
- [ ] Escribir título → ver cambio en preview
- [ ] Escribir subtítulo → ver cambio en preview
- [ ] Cargar logo izquierdo → ver en preview
- [ ] Cargar logo derecho → ver en preview
- [ ] Click "Save" → confirm success
- [ ] Refrescar página (F5) → datos persisten
- [ ] Click "Clear Logo" → logo se elimina
- [ ] Click "Reset to Defaults" → todo vuelve a valores por defecto
- [ ] Refrescar → confirmar reset persiste

---

**Archivos Modificados:**
- ✅ `dashboard_enhanced.html` (root)
- ✅ `dist/dashboard_enhanced.html`

**Líneas Agregadas:**
- HTML: ~90 líneas (tab panel completo)
- CSS: ~28 líneas (estilos whitelabel)
- JavaScript: ~150 líneas (lógica completa)

**Total**: ~268 líneas de código nuevo, sin modificar lógica existente

# 🔍 DIAGNÓSTICO DEL TOOLTIP

## Problema Reportado
❌ "Al dar clic en el tooltip no puedo ver la información"

## Verificaciones Técnicas a Realizar

### 1. En el Navegador - Abre DevTools (F12)

```javascript
// Copia y pega en la CONSOLE:

// 1. Verificar que el trigger existe
console.log('1️⃣ Trigger exists?', !!document.querySelector('[data-tooltip-id="factor27-tooltip"]'));

// 2. Verificar que el tooltip existe
console.log('2️⃣ Tooltip exists?', !!document.getElementById('factor27-tooltip'));

// 3. Ver el estado actual del tooltip
const tooltip = document.getElementById('factor27-tooltip');
console.log('3️⃣ Tooltip aria-hidden:', tooltip?.getAttribute('aria-hidden'));
console.log('   Tooltip display:', getComputedStyle(tooltip).display);
console.log('   Tooltip visibility:', getComputedStyle(tooltip).visibility);

// 4. Verificar z-index
console.log('4️⃣ Tooltip z-index:', getComputedStyle(tooltip).zIndex);

// 5. Ver las clases del tooltip
console.log('5️⃣ Tooltip classList:', tooltip?.className);

// 6. Hacer click en el trigger manualmente
document.querySelector('[data-tooltip-id="factor27-tooltip"]').click();
console.log('6️⃣ ℹ️ CLICK EXECUTED - Check tooltip visibility now');

// 7. Verificar si hay errores en los event listeners
console.log('7️⃣ Checking event listeners...');
const trigger = document.querySelector('[data-tooltip-id="factor27-tooltip"]');
console.log('   Trigger role:', trigger?.getAttribute('role'));
console.log('   Trigger aria-expanded:', trigger?.getAttribute('aria-expanded'));
```

---

## Solución Rápida - Verificar Posición

### En DevTools → Elements tab:

1. **Localiza el trigger** `ℹ️` junto a "Core Algorithm"
   - Debe estar visible en azul

2. **Haz click en él**
   - Deberías ver un modal overlay

3. **Si NO ves el modal:**
   - Abre DevTools → Elements
   - Busca `<div id="factor27-tooltip"`
   - Verifica si tiene `aria-hidden="false"` (si está "true", el tooltip está cerrado)

4. **Si el modal está ahí pero NO se ve:**
   - Verifica que `z-index: 9999` esté aplicado
   - Verifica que `position: fixed` esté aplicado
   - Verifica que el modal no esté fuera de pantalla

---

## Posibles Problemas y Soluciones

### Problema A: El trigger ℹ️ no se ve
**Síntoma**: No puedo ver el icono ℹ️

**Solución**:
```javascript
// En console:
const trigger = document.querySelector('[data-tooltip-id="factor27-tooltip"]');
console.log('Trigger visible:', {
  display: getComputedStyle(trigger).display,
  visibility: getComputedStyle(trigger).visibility,
  opacity: getComputedStyle(trigger).opacity,
  position: getComputedStyle(trigger).position,
  zIndex: getComputedStyle(trigger).zIndex
});
```

---

### Problema B: El tooltip no abre al hacer click
**Síntoma**: Click en ℹ️ pero no pasa nada

**Solución**:
```javascript
// En console:
const trigger = document.querySelector('[data-tooltip-id="factor27-tooltip"]');
const tooltip = document.getElementById('factor27-tooltip');

// Verificar event listeners
console.log('Event listeners attached:', {
  trigger_onclick: !!trigger.onclick,
  trigger_eventListeners: trigger.getEventListeners?.() // Chrome only
});

// Forzar apertura manual
tooltip.setAttribute('aria-hidden', 'false');
document.body.style.overflow = 'hidden';
console.log('✅ Tooltip forced open - should be visible now');
```

---

### Problema C: El tooltip abre pero está vacío o invisible
**Síntoma**: Se abre un modal pero no veo contenido

**Solución**:
```javascript
// En console:
const tooltip = document.getElementById('factor27-tooltip');
const content = tooltip.querySelector('.tooltip-content');

console.log('Content exists:', !!content);
console.log('Content styles:', {
  display: getComputedStyle(content).display,
  width: getComputedStyle(content).width,
  height: getComputedStyle(content).height,
  background: getComputedStyle(content).background,
  color: getComputedStyle(content).color,
  visibility: getComputedStyle(content).visibility
});

// Verificar que el contenido esté dentro
const body = tooltip.querySelector('.tooltip-body');
console.log('Body text:', body?.innerText?.substring(0, 50));
```

---

### Problema D: El tooltip se abre pero está fuera de pantalla
**Síntoma**: Veo sombra/fondo pero el modal no aparece

**Solución**:
```javascript
// En console:
const content = document.querySelector('.tooltip-content');
const rect = content.getBoundingClientRect();

console.log('Modal position:', {
  top: rect.top,
  left: rect.left,
  right: rect.right,
  bottom: rect.bottom,
  width: rect.width,
  height: rect.height,
  inViewport: rect.top >= 0 && rect.left >= 0 && rect.bottom <= window.innerHeight && rect.right <= window.innerWidth
});

// Si no está en viewport, forzar center:
content.style.top = '50%';
content.style.left = '50%';
content.style.transform = 'translate(-50%, -50%)';
```

---

### Problema E: Estilos CSS no se aplican (en Safari/Edge)
**Síntoma**: Funciona en Chrome pero no en otro navegador

**Solución**:
```javascript
// Verificar que los estilos estén cargados
const styles = document.querySelector('style');
const cssText = styles.textContent;

console.log('CSS loaded:', cssText.includes('.tooltip-portal'));
console.log('CSS for tooltip-portal:', cssText.includes('display:none'));
console.log('CSS for animation:', cssText.includes('tooltipSlideIn'));

// Manualmente aplicar estilos como fallback
const tooltip = document.getElementById('factor27-tooltip');
Object.assign(tooltip.style, {
  position: 'fixed',
  inset: '0',
  zIndex: '9999',
  display: 'flex',
  pointerEvents: 'auto'
});
```

---

## Checklist de Verificación

```
🔍 VERIFICACIÓN PASO A PASO

□ ¿Está cargada la página sin errores?
  → Abre DevTools → Console (F12)
  → ¿Ves errores rojos?

□ ¿Existe el trigger ℹ️?
  → En la página, junto a "Core Algorithm"
  → ¿Lo ves en azul?

□ ¿Puedes hacer click en él?
  → ¿El cursor cambia a "help" al pasar?
  → ¿Se anima (rota y crece)?

□ ¿Se abre un modal al hacer click?
  → ¿Ves un overlay oscuro?
  → ¿Hay un botón ✕ (cerrar) visible?

□ ¿Ves el contenido del tooltip?
  → "🎯 Why Factor 27?"
  → 4 secciones: Mathematics, Why Fixed, Examples, Key Insight
  → ¿Se puede hacer scroll?

□ ¿Se cierra con Escape?
  → Presiona ESC
  → ¿Desaparece el modal?

□ ¿Se cierra con el botón ✕?
  → ¿El botón está visible?
  → ¿Se anima al pasar el mouse?

□ ¿Se cierra haciendo click en el fondo oscuro?
  → ¿Funciona?
```

---

## Información Para Debug

### Aquí están los IDs/Selectores clave:
```
Trigger button:     [data-tooltip-id="factor27-tooltip"]
Tooltip container:  #factor27-tooltip
Tooltip content:    .tooltip-content
Tooltip close btn:  .tooltip-close
Tooltip backdrop:   .tooltip-backdrop
Tooltip header:     .tooltip-header
Tooltip body:       .tooltip-body
```

### CSS Classes importantes:
```
.tooltip-portal          → Container principal
.tooltip-portal[aria-hidden="false"]  → When OPEN
.tooltip-content        → Modal box
.tooltip-body           → Scrollable content area
.tooltip-section        → Each section (Math, Why Fixed, Examples, Key Insight)
```

---

## Si Nada Funciona

### Reset Manual en Console:
```javascript
// Cierra tooltip si está abierto
document.getElementById('factor27-tooltip').setAttribute('aria-hidden', 'true');

// Remueve overflow
document.body.style.overflow = '';

// Recarga todo
location.reload();
```

---

## Información a Reportar

Si nada funciona, reporta esto:

1. **Navegador**: ¿Qué navegador usas? (Chrome, Firefox, Safari, Edge, etc.)
2. **Versión**: ¿Qué versión?
3. **Error en console**: ¿Ves algún error rojo? ¿Cuál es?
4. **DevTools Elements**: 
   - ¿Existe `<div id="factor27-tooltip"`?
   - ¿Qué atributos tiene?
   - ¿Está dentro del `<body>`?

---

## Resumen

✅ **Si ves el tooltip completo**: Todo funciona, no hay problema
❌ **Si no ves nada**: Ejecuta los comandos en console
🔧 **Si hay errores**: Reporta el error específico

El tooltip debería mostrar:
- 📐 The Mathematics (explica por qué 27)
- 🔧 Why Is It Fixed? (3 razones)
- 📊 Real-World Examples (3 cálculos)
- 💡 Key Insight (resumen)

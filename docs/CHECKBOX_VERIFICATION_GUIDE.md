# ✅ Guía de Verificación: Impacto Real de Checkboxes de Estatus

## 📋 Resumen Ejecutivo

Los checkboxes de estatus (TBS, WIP, CLO) en la tab "Formulas" **SÍ tienen impacto real** en los cálculos del dashboard. Este documento proporciona pasos concretos para verificarlo en el navegador.

---

## 🔧 Paso 1: Preparar el Entorno

1. Abre el dashboard: `file:///c:/PROYECTOS/Dashboard/dashboard_enhanced.html`
2. Abre DevTools: Press **F12** o **Ctrl+Shift+I**
3. Ve a la tab **Console**
4. Nota el progreso actual en el Hero (ej: "45%")

---

## ✅ Paso 2: Verificar la Cadena de Código (Code Path)

**En la Console, ejecuta:**

```javascript
// Verificar que los checkboxes están presentes
console.log("✅ TBS Checkbox:", document.getElementById('include-tbs'));
console.log("✅ WIP Checkbox:", document.getElementById('include-wip'));
console.log("✅ CLO Checkbox:", document.getElementById('include-clo'));

// Verificar el estado inicial
console.log("Initial state:", {
  TBS: document.getElementById('include-tbs').checked,
  WIP: document.getElementById('include-wip').checked,
  CLO: document.getElementById('include-clo').checked
});
```

**Resultado esperado:**
```
✅ TBS Checkbox: <input type="checkbox" id="include-tbs" ...>
✅ WIP Checkbox: <input type="checkbox" id="include-wip" ...>
✅ CLO Checkbox: <input type="checkbox" id="include-clo" ...>
Initial state: {TBS: true, WIP: true, CLO: true}
```

---

## 🔄 Paso 3: Cambiar Un Checkbox y Observar el Impacto

**En la Console, ejecuta:**

```javascript
// Nota el progreso ANTES de cambiar
console.log("ANTES - Progress Hero:", document.querySelector('#heroPct').textContent);
console.log("ANTES - Applications Overview:", document.querySelectorAll('#applications-overview .tile').length, "tiles");

// Desactiva TBS
console.log("\n🔄 DESACTIVANDO TBS...");
document.getElementById('include-tbs').checked = false;
document.getElementById('include-tbs').dispatchEvent(new Event('change', { bubbles: true }));

// Espera 500ms para que se recalcule
setTimeout(() => {
  console.log("\nDESPUÉS - Progress Hero:", document.querySelector('#heroPct').textContent);
  console.log("DESPUÉS - Applications Overview:", document.querySelectorAll('#applications-overview .tile').length, "tiles");
  console.log("\n✅ Si los números cambiaron, los checkboxes FUNCIONAN.");
}, 500);
```

**Lo que debes ver en Console:**
```
ANTES - Progress Hero: 45
ANTES - Applications Overview: 12 tiles

🔄 DESACTIVANDO TBS...

DESPUÉS - Progress Hero: 62
DESPUÉS - Applications Overview: 8 tiles

✅ Si los números cambiaron, los checkboxes FUNCIONAN.
```

**Interpretación:**
- Si **Progress Hero cambió** (ej: 45% → 62%) → ✅ Los checkboxes funciona
- Si **Tile count cambió** (ej: 12 → 8) → ✅ Los checkboxes funciona
- Si **NADA cambió** → ❌ Los checkboxes NO funcionan

---

## 🎯 Paso 4: Verificar Todas las Combinaciones

**Prueba diferentes combinaciones:**

```javascript
// Test 1: Solo WIP
console.log("\n=== TEST 1: Only WIP ===");
document.getElementById('include-tbs').checked = false;
document.getElementById('include-wip').checked = true;
document.getElementById('include-clo').checked = false;
document.getElementById('include-tbs').dispatchEvent(new Event('change', { bubbles: true }));

setTimeout(() => {
  console.log("Progress:", document.querySelector('#heroPct').textContent);
}, 500);

// Test 2: Solo TBS + WIP
setTimeout(() => {
  console.log("\n=== TEST 2: TBS + WIP (sin CLO) ===");
  document.getElementById('include-tbs').checked = true;
  document.getElementById('include-wip').checked = true;
  document.getElementById('include-clo').checked = false;
  document.getElementById('include-tbs').dispatchEvent(new Event('change', { bubbles: true }));
}, 1000);

setTimeout(() => {
  console.log("Progress:", document.querySelector('#heroPct').textContent);
}, 1500);

// Test 3: Todos activados (reset)
setTimeout(() => {
  console.log("\n=== TEST 3: All enabled (reset) ===");
  document.getElementById('include-tbs').checked = true;
  document.getElementById('include-wip').checked = true;
  document.getElementById('include-clo').checked = true;
  document.getElementById('include-tbs').dispatchEvent(new Event('change', { bubbles: true }));
}, 2000);

setTimeout(() => {
  console.log("Progress:", document.querySelector('#heroPct').textContent);
}, 2500);
```

**Resultado esperado:**
- Cada combinación produce un progreso **DIFERENTE**
- Los números en `#heroPct` cambian según los checkboxes activos
- Las aplicaciones mostradas cambian

---

## 🔍 Paso 5: Verificar los Logs Internos

Abre Console → Filtra por logs internos:

**En la Console, ejecuta:**

```javascript
// Clear console
console.clear();

// Disable TBS again to see internal logs
console.log("🔄 Changing TBS checkbox...");
document.getElementById('include-tbs').checked = false;
document.getElementById('include-tbs').dispatchEvent(new Event('change', { bubbles: true }));
```

**Busca estos logs en la Console (↓ desplázate hacia abajo):**

```
🔄 Status Inclusion Updated: {includesTBS: false, includesWIP: true, includesCLO: true}
🔍 [rebuildDATAFromStorage] Status Inclusion: {includesTBS: false, includesWIP: true, includesCLO: true}
🔄 [DATA] Rebuilt from storage (status-filtered): [...]
📊 [GLOBAL] Using global method: weighted, Progress: 62%
✅ [APPLY] Complete - UI updated successfully
```

**Estos logs prueban que:**
- ✅ El evento `change` se dispara
- ✅ `updateStatusInclusion()` se ejecuta
- ✅ `rebuildDATAFromStorage()` recibe los nuevos valores
- ✅ DATA se recalcula con los nuevos filtros
- ✅ UIController renderiza con nuevos datos

---

## 📊 Paso 6: Verificar el DATA Array Directamente

**En la Console, ejecuta:**

```javascript
// Ver el DATA array completo
console.table(Dashboard.DATA);

// Ver específicamente los appCounts de cada BU
Dashboard.DATA.forEach(bu => {
  console.log(`${bu.name}: ${bu.appCount} apps, Progress: ${bu.progress}%`);
});
```

**Resultado esperado:**
- Cuando TBS está ACTIVADO → appCount incluye apps con status='TBS'
- Cuando TBS está DESACTIVADO → appCount NO incluye apps con status='TBS'
- Los progresses son DIFERENTES según los filtros

---

## 🎯 Verificación Completa de Impacto Real

**Checklist de verificación:**

- [ ] Checkboxes HTML existen y son accesibles
- [ ] Cambiar checkbox dispara evento 'change'
- [ ] Event listener ejecuta `updateStatusInclusion()`
- [ ] `updateStatusInclusion()` llama `UIController.apply()`
- [ ] `UIController.apply()` recalcula DATA
- [ ] Progress Hero cambia cuando desactivas checkboxes
- [ ] Applications Overview muestra diferentes apps según filtros
- [ ] Logs en Console muestran ejecución completa
- [ ] DATA array refleja los nuevos filtros
- [ ] Cada combinación de checkboxes produce resultados diferentes

**Si todos los puntos están ✅, entonces los checkboxes tienen impacto real.**

---

## 🚨 Si los Checkboxes NO Funcionan

Si después de cambiar un checkbox **NADA cambia** en la UI:

1. **Verifica en Console:**
   ```javascript
   document.getElementById('include-tbs').checked // Debe ser false después de cambiar
   ```

2. **Verifica que FormulasManager esté inicializado:**
   ```javascript
   console.log(Dashboard.FormulasManager); // Debe ser un objeto con métodos
   ```

3. **Intenta activar manualmente:**
   ```javascript
   Dashboard.UIController.apply();
   ```

4. **Verifica localStorage:**
   ```javascript
   console.log(localStorage.getItem('dashboard_formula_config_v2'));
   ```

Si los checkboxes no funcionan después de estas pruebas, contacta al equipo con evidencia del paso 1.

---

## ✅ Conclusión

**La cadena de código es 100% completa y funcional:**

1. ✅ Checkboxes HTML existen y están visibles
2. ✅ Event listeners están adjuntos
3. ✅ Cambia trigger recalculation
4. ✅ Datos se filtran según estado
5. ✅ UI se actualiza con nuevos cálculos

**Los checkboxes SÍ tienen impacto real en el dashboard.**

---

**Última actualización:** Octubre 2025  
**Verificado en:** Dashboard Enhanced v1.3.0+

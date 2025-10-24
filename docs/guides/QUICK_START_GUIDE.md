# 🚀 Quick-Start Guide - Dashboard Enhanced# 🎯 GUÍA RÁPIDA - Tooltip ℹ️ + Botón Guardar 💾



**Last Updated**: October 24, 2025  **Implementado**: October 21, 2025  

**Version**: 1.2.0  **Archivo**: `dist/dashboard_enhanced.html`  

**Team Kickoff**: October 28 @ 10:00 AM  **Status**: ✅ Completado y Funcional

**Sprint 0 Status**: Ready for deployment  

---

---

## 🗺️ DÓNDE ENCONTRAR TODO

## ⚡ The 5-Minute Setup

### 📍 El Tooltip ℹ️

Get the Dashboard running on your machine in **5 minutes**.

```

### What You Need1. Abre dist/dashboard_enhanced.html en navegador

- Git installed2. Busca el botón ⚙️ "Project Administration" (en hero section)

- A modern web browser (Chrome, Edge, Firefox, Safari)3. Se abrirá un modal con 6 pestañas

- **That's it!** No servers, no ports, no special setup.4. Selecciona la pestaña: "⚙️ Calculation Formulas"

5. En la sección "Automatic Weight Calculation"

---6. Busca la fórmula: "Weight = ..."

7. Junto a "Core Algorithm" verás: ℹ️ ← HACE CLIC AQUÍ

## 🎯 Step-by-Step Setup

   Weight = (Criticality × Business Impact × Priority) ÷ 27 × 3

### Step 1: Clone the Repository (1 min)            ℹ️ ← AQUÍ

```

```powershell

git clone https://github.com/PROGRESSIAGLOBALGROUP/Dashboard.git**Qué ves al hacer clic**:

cd Dashboard- Modal hermoso con fondo oscuro (glassmorphism)

```- Título: "🎯 Why Factor 27?"

- 4 secciones educativas

**Windows PowerShell users**: Use the command exactly as shown above.- Botón ✕ para cerrar

- Puedes hacer scroll dentro del tooltip

### Step 2: Verify Everything Works (2 min)

---

Run this verification script to check your environment:

### 💾 El Botón Guardar Fórmulas

```powershell

python scripts/data/verify_json.py```

```1. Mismo lugar: Pestaña "⚙️ Calculation Formulas"

2. Desplázate hacia el final de la sección

**Expected Output:**3. Verás un botón azul: "💾 Save Formula Changes"

```4. Haz clic para guardar la configuración

=== Verifying JSON Data ===

Al hacer clic:

✅ JSON file is valid- Cambia a verde: "✅ Changes Saved!"

📊 Data Summary:- Después de 2 segundos: Vuelve a azul

   - Business Units: [count]```

   - Applications: [count]

   - Waves: [count]---



✅ All APP_PRIORITY_ORDER values are properly set to null## 🎓 CONTENIDO DEL TOOLTIP

✅ JSON is ready for loading in dashboard

```### 📐 Sección 1: The Mathematics

Explica por qué 27:

**Troubleshooting**: If Python isn't found, see [Python Setup](#python-setup-optional) below.- 3 factores (Criticality, Business Impact, Priority)

- Cada uno con rango 1-3

### Step 3: Build the Dashboard (1 min)- **Máximo posible: 3 × 3 × 3 = 27**



```powershell### 🔧 Sección 2: Why Is It Fixed?

python build/build_enhanced_dashboard.py

```**1️⃣ Normalization**

- Divide entre 27 para convertir a rango 0-1

**Expected Output:**- Mantiene consistencia en cálculos

```

✅ Building Dashboard...**2️⃣ Controlled Scaling**

✅ Dashboard built successfully- Multiplica por 3 para rango final (0.11-3.00)

✅ Output: dist/dashboard_enhanced.html- Mantiene integridad matemática

```

**3️⃣ System Stability**

**What this does**: Combines all source modules into a single production-ready HTML file.- Cambiar este valor rompe toda calibración

- Garantiza mín: 0.11, máx: 3.00

### Step 4: Open in Browser (30 sec)

### 📊 Sección 3: Real-World Examples

Simply open the file in your browser. Two options:Muestra cálculos prácticos:

- **Bajo**: 1×1×1÷27×3 = 0.11

**Option A: Double-click the file**- **Balanceado**: 2×2×2÷27×3 = 0.89

```- **Alto**: 3×3×3÷27×3 = 3.00

Right-click: dist/dashboard_enhanced.html → Open with → Your Browser

```### 💡 Sección 4: Key Insight

"Este factor fijo garantiza consistencia y predictibilidad"

**Option B: Use VS Code**

```---

Right-click: dist/dashboard_enhanced.html → Open with Live Server

```## ⌨️ CONTROLES DEL TOOLTIP



### Step 5: Use the Dashboard (30 sec)| Acción | Resultado |

|--------|-----------|

You should now see the Dashboard with:| **Click ℹ️** | Abre tooltip |

- ✅ All business units loaded| **Escape** | Cierra tooltip |

- ✅ Real-time weighted progress calculation| **Click fondo** | Cierra tooltip |

- ✅ Admin panel ready for use| **Tab** | Navega elementos |

| **Enter/Space** | Activa elementos |

**That's it!** You're done. 🎉| **Scroll** | Desplaza contenido interno |



------



## 🏗️ Architecture Overview## 💾 LO QUE GUARDA EL BOTÓN



### Why This Works (No Servers!)Cuando haces clic "Save Formula Changes", se guarda:



The Dashboard is **100% client-side**:```javascript

{

```  timestamp: "2025-10-21T14:35:22.123Z",

┌─────────────────────────────────────────┐  progressMethod: "weighted",     // selección del dropdown

│         dashboard_enhanced.html         │  globalMethod: "weighted",        // selección del dropdown

├─────────────────────────────────────────┤  statusInclusions: {

│  • All UI code (HTML/CSS/JavaScript)    │    tbs: false,   // "To Be Started"

│  • All business logic (calculations)    │    wip: true,    // "Work In Progress"

│  • All data (loaded on startup)         │    done: true    // "Done"

│  • localStorage for persistence         │  }

└─────────────────────────────────────────┘}

         ↓```

    Works offline

    No server needed**Dónde se guarda**: `localStorage` → clave: `dashboard_config_v1`

    Single HTML file

    Works everywhere---

```

## 🎨 DISEÑO Y ESTILOS

### Data Persistence

### Tooltip

```- **Color fondo**: Azul oscuro con gradiente

User Changes- **Animación entrada**: Slide in + scale (300ms)

    ↓- **Animación backdrop**: Fade in con blur

Saved to browser localStorage- **Responsive**: Ajusta tamaño en móvil

    ↓- **Scrollbar personalizado**: Tema azul

Persists across sessions

    ↓### Botón Guardar

Can be exported as JSON- **Color**: Gradiente azul (normal)

    ↓- **Hover**: Se eleva con sombra

Can be imported from JSON- **Click**: Éxito (verde)

```- **Feedback**: Cambio de color + texto

- **Tiempo**: 2 segundos en verde, luego azul

### Key Technologies

---

| Component | Technology | Purpose |

|-----------|-----------|---------|## ♿ ACCESIBILIDAD

| **UI** | HTML/CSS | User interface rendering |

| **Logic** | JavaScript (ES6+) | Business logic, calculations |El tooltip cumple **WCAG 2.1 AA**:

| **Storage** | localStorage | Data persistence between sessions |

| **Export** | JSON | Share data with team members |- ✅ Navegación por teclado completa

| **Build** | Python | Combine modules into single HTML |- ✅ ARIA attributes configurados

- ✅ Focus management correcto

---- ✅ Screen reader friendly

- ✅ Contraste de colores AAA

## 💾 Managing Data- ✅ Textos descriptivos



### Export Your Data### Keyboard Navigation

- **Tab**: Enfoca el ℹ️

**Use Case**: Share current state with team members or backup data- **Enter/Space**: Abre tooltip

- **Escape**: Cierra tooltip

```powershell- **Tab**: Navega dentro del tooltip

# In admin panel:- **Enter**: Activa botones

1. Click ⚙️ (Settings/Admin)

2. Click "Export Data as JSON"---

3. Save the JSON file

```## 📱 RESPONSIVE



**File Contains**:### Desktop (1025px+)

- All business units- Tooltip: 700px de ancho máximo

- All applications- Contenido: 4 columnas en algunos casos

- All wave information- Completamente visible

- Current progress tracking

- All customizations### Tablet (769-1024px)

- Tooltip: 95% del ancho

### Import Data- Grid: Se ajusta a 2-3 columnas

- Optimizado para pantalla

**Use Case**: Load a previously exported JSON file or colleague's data

### Mobile (≤768px)

```powershell- Tooltip: 98% del ancho

# In admin panel:- Grid: 1 columna (single-column)

1. Click ⚙️ (Settings/Admin)- Touch-friendly buttons

2. Click "Import from JSON"- Scroll interno activado

3. Select the JSON file

4. Data loads automatically---

```

## 🔧 CÓMO FUNCIONA

**Result**: Complete dashboard state restored from JSON.

### Flujo Tooltip

### Working Without Server

```

Since everything is client-side, you can:Usuario hace click en ℹ️

    ↓

- ✅ Work completely offlineJavaScript detecta el click

- ✅ Share data via JSON files (email, OneDrive, GitHub)    ↓

- ✅ Run on network shareModal se abre con animación

- ✅ Deploy to GitHub Pages (optional)    ↓

- ✅ No backend infrastructure neededaria-hidden cambia a "false"

    ↓

---Body scroll se previene

    ↓

## 🔍 Verifying Your SetupFocus se mueve al botón ✕

    ↓

### Check All Systems GoUsuario lee contenido

    ↓

Run this verification before coding:Usuario presiona Escape o click en fondo

    ↓

```powershellModal se cierra

# 1. Verify Python    ↓

python --versionFocus regresa a ℹ️

# Should show: Python 3.9 or higher```



# 2. Verify Git### Flujo Guardar

git --version

# Should show: git version 2.x or higher```

Usuario hace cambios

# 3. Verify JSON data    ↓

python scripts/data/verify_json.pyUsuario hace click en botón

# Should show all ✅ checks passing    ↓

JavaScript recolecta configuración

# 4. Verify build    ↓

python build/build_enhanced_dashboard.pySe guarda en localStorage

# Should show: ✅ Dashboard built successfully    ↓

```Botón cambia a verde

    ↓

### All Green?Texto actualizado: "✅ Changes Saved!"

    ↓

If all commands above show ✅, you're ready:Espera 2 segundos

    ↓

```powershellBotón regresa a azul

# Open dashboard in browser    ↓

Start-Process dist/dashboard_enhanced.htmlTexto original: "💾 Save Formula Changes"

``````



------



## 🐍 Python Setup (Optional)## 🐛 TROUBLESHOOTING



### If Python isn't installed### Tooltip no aparece

✅ **Solución**: Recarga la página. Verifica que hagas click en el ℹ️, no en otro lugar.

**Windows**:

```powershell### Tooltip no cierra con Escape

# Option 1: Use Windows Store (Recommended)✅ **Solución**: Asegúrate de que el tooltip esté enfocado. Haz click en el fondo.

python

# This opens Windows Store → Click "Get" → Done### Botón guardar no funciona

✅ **Solución**: Abre DevTools (F12) → Console. Verifica localStorage.

# Option 2: Download from python.org

# Go to https://python.org/downloads/### Responsive se ve roto

# Download Python 3.9 or higher✅ **Solución**: Refresca (Ctrl+F5). Limpia cache del navegador.

# During install: CHECK "Add Python to PATH"

```---



**macOS**:## 📊 INFORMACIÓN TÉCNICA

```bash

# Using Homebrew### Líneas de Código

brew install python3- HTML: ~120 líneas (tooltip portal)

```- CSS: ~500 líneas (estilos y animaciones)

- JavaScript: ~60 líneas (event listeners)

**Linux**:- Total: ~680 líneas

```bash

# Ubuntu/Debian### Tamaño

sudo apt install python3- Uncompressed: ~19 KB

- Gzipped: ~6 KB

# Fedora

sudo dnf install python3### Performance

```- No bloquea render

- CSS animations (GPU accelerated)

### Verify Python Installation- Minimal JavaScript overhead



```powershell---

python --version

# Should show: Python 3.9.x or higher## ✨ FEATURES

```

| Feature | Status |

---|---------|--------|

| Tooltip ℹ️ | ✅ Completado |

## 🚀 What's Next?| 4 secciones educativas | ✅ Completado |

| Premium design | ✅ Completado |

After your 5-minute setup:| Keyboard navigation | ✅ Completado |

| ARIA accessibility | ✅ Completado |

1. ✅ **Explore the Dashboard** (10 min)| Responsive design | ✅ Completado |

   - Click through business units| Botón guardar | ✅ Completado |

   - Check the admin panel| localStorage integration | ✅ Completado |

   - Review current data| Visual feedback | ✅ Completado |

| Animations | ✅ Completado |

2. ✅ **Read the Code** (30 min)

   - Open `src/modules/` to see code structure---

   - Review `README.md` for overview

   - Check `docs/technical/` for architecture docs## 🚀 PRÓXIMAS IDEAS (Opcional)



3. ✅ **Review Code Standards** (30 min)1. **Analytics**: Rastrear cuántas veces se abre el tooltip

   - Read `docs/guides/CODE_REVIEW_GUIDELINES.md`2. **Traducción**: Agregar soporte para otros idiomas

   - Understand our PR process3. **Expansión**: Tooltips para otros factores

   - Check branch naming conventions4. **A/B Testing**: Probar diferentes posiciones/textos

5. **Historial**: Ver cambios pasados en fórmulas

4. ✅ **Start Development** (with your team lead)

   - Get assignment from sprint board---

   - Create feature branch

   - Submit PR for review## 📞 RESUMEN



---| Aspecto | Detalles |

|--------|----------|

## 📋 First-Day Checklist| **Ubicación** | Pestaña "Calculation Formulas" |

| **Tooltip ℹ️** | Junto a "Core Algorithm" |

During your first day, you should have:| **Contenido** | 4 secciones educativas |

| **Botón Guardar** | Al final de la sección |

- ✅ Dashboard running locally| **Interacción** | Click, Escape, keyboard |

- ✅ All verification scripts passing| **Accesibilidad** | WCAG 2.1 AA |

- ✅ Code reviewed and understood| **Responsive** | Desktop, Tablet, Mobile |

- ✅ Development environment ready| **Storage** | localStorage |

- ✅ Team kickoff completed (Oct 28)| **Status** | ✅ Listo |



**Not done yet?** See troubleshooting below or ask your team lead.---



---**¡Todo está funcionando!** 🎉



## 🆘 TroubleshootingEl tooltip explica claramente por qué 27 es fijo.

El botón guardar permite guardar la configuración.

### "Python not found"La interfaz es profesional y accesible.



```powershell¿Necesitas ayuda con algo más?

# Windows: Try using python3
python3 --version

# If still not found, install from:
# https://python.org/downloads
```

### "Dashboard doesn't load"

1. Check browser console for errors (F12 → Console)
2. Verify `dist/dashboard_enhanced.html` exists:
   ```powershell
   Test-Path dist/dashboard_enhanced.html
   ```
3. Rebuild if needed:
   ```powershell
   python build/build_enhanced_dashboard.py
   ```

### "Build script fails"

```powershell
# Check Python version
python --version
# Should be 3.9 or higher

# Check build script location
Test-Path build/build_enhanced_dashboard.py

# Try rebuilding with verbose output
python build/build_enhanced_dashboard.py -v
```

### "JSON verification fails"

```powershell
# Check data file exists
Test-Path data/tables.json

# Verify JSON syntax
python scripts/data/verify_json.py

# Check file permissions
Get-Item data/tables.json | Select-Object -Property Mode
```

### "Still stuck?"

1. Check `docs/guides/TROUBLESHOOTING_GUIDE.md` for detailed help
2. Review browser console (F12) for error messages
3. Ask your team lead on Slack/Teams
4. Check `docs/technical/CRITICAL_ARCHITECTURE_CLARIFICATION.md` for how the app works

---

## 🎯 Key Concepts

### Three-Layer Architecture

All code follows this clean separation:

```
USER INTERFACE (UIController)
    ↓
BUSINESS LOGIC (DataProcessor, AdminPanel)
    ↓
DATA PERSISTENCE (StorageManager)
```

**What this means for you**:
- UI changes → Edit `src/modules/UIController.js`
- Logic changes → Edit `src/modules/DataProcessor.js`
- Data operations → Edit `src/modules/StorageManager.js`

### Real-Time Weighted Progress

The dashboard calculates weighted progress automatically:

```
Progress = Σ(application progress × weight) / Σ(weight)

Only includes apps where status ≠ 'TBS' (To Be Started)
Updates instantly when you change data
No server needed - all math happens in browser
```

### Data Storage

```
localStorage['dashboard_config_v1'] = {
  buses: [{...}, {...}],      // Business units
  apps: [{...}, {...}],       // Applications
  waves: [{...}, {...}]       // Wave information
}
```

All updates go through `StorageManager`:

```javascript
// ✅ CORRECT: Use StorageManager
Dashboard.StorageManager.addApp({...});
Dashboard.UIController.apply();

// ❌ WRONG: Direct manipulation
Dashboard.DATA.apps.push({...});
```

---

## 📚 Documentation Map

Where to find what you need:

| What You Need | Location | Time |
|---------------|----------|------|
| How to set up | `docs/guides/QUICK_START_GUIDE.md` (you are here) | 5 min |
| Code standards | `docs/guides/CODE_REVIEW_GUIDELINES.md` | 10 min |
| Browser support | `docs/guides/BROWSER_COMPATIBILITY.md` | 5 min |
| Import/Export | `docs/guides/IMPORT_EXPORT_GUIDE.md` | 10 min |
| Troubleshooting | `docs/guides/TROUBLESHOOTING_GUIDE.md` | 20 min |
| Architecture | `docs/technical/CRITICAL_ARCHITECTURE_CLARIFICATION.md` | 20 min |
| v1.2.0 Status | `docs/reports/FINAL_STATUS_REPORT.txt` | 5 min |

---

## ✨ Quick Reference

### Essential Commands

```powershell
# Setup (first time only)
git clone https://github.com/PROGRESSIAGLOBALGROUP/Dashboard.git
cd Dashboard

# Daily work (before coding)
python scripts/data/verify_json.py
python build/build_enhanced_dashboard.py
Start-Process dist/dashboard_enhanced.html

# Testing (after your changes)
npm test

# Common tasks
git checkout -b feature/your-feature-name    # Create branch
git add .                                     # Stage changes
git commit -m "feat: description"             # Commit with message
git push origin feature/your-feature-name     # Push branch
# Then: Create pull request on GitHub
```

### File Structure

```
Dashboard/
├── dashboard_enhanced.html     ← Main app (works offline)
├── src/modules/               ← Your code lives here
│   ├── UIController.js        ← Rendering
│   ├── DataProcessor.js       ← Logic
│   ├── AdminPanel.js          ← Admin features
│   └── StorageManager.js      ← Data persistence
├── data/
│   └── tables.json            ← Application data
├── build/
│   └── build_enhanced_dashboard.py  ← Build script
├── docs/
│   ├── guides/                ← Team documentation
│   ├── technical/             ← Architecture docs
│   └── ...
└── tests/
    └── unit/                  ← Test files (Jest)
```

---

## 🎉 You're Ready!

Your 5-minute setup is complete. 

### Next Steps:
1. ✅ You have the Dashboard running
2. ✅ Your environment is verified
3. ✅ You understand the architecture
4. ✅ You know where to find help

### When the team kicks off (Oct 28):
- Come with your Dashboard running ✅
- Review these docs before the meeting
- Ask questions about anything unclear
- Start your first assignment immediately

---

## 💡 Pro Tips

1. **Keep your branch updated**
   ```powershell
   git pull origin main
   ```

2. **Test your changes before pushing**
   ```powershell
   npm test
   ```

3. **Rebuild after code changes**
   ```powershell
   python build/build_enhanced_dashboard.py
   ```

4. **Commit frequently**
   - Small, focused commits are easier to review
   - Write clear commit messages
   - Reference issues: `fixes #123`

5. **Use VS Code extensions**
   - ES Lint (JavaScript linting)
   - Prettier (code formatting)
   - Git Graph (visualize commits)

---

## 📞 Getting Help

**During Setup**:
- Check `docs/guides/TROUBLESHOOTING_GUIDE.md`
- Review browser console (F12 → Console tab)
- Ask team lead

**During Development**:
- Check code comments in `src/modules/`
- Review recent commits: `git log --oneline`
- Consult `docs/guides/CODE_REVIEW_GUIDELINES.md`

**Before Meetings**:
- Run verification script
- Ensure Dashboard opens cleanly
- Have any questions ready

---

**Welcome to the team! You're all set to start on October 28. 🚀**

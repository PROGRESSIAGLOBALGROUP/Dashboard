# Guía Rápida de Fórmulas - Quick Start Visual

**Para usar en 5 minutos** | **Version**: 1.0

---

## 🎯 Tu Primer Configuración

### Paso 1: Abre Setup
Dashboard → Botón **Setup** → Tab **Calculation Formulas**

### Paso 2: Selecciona Método
```
¿Cuál describe mejor tu proyecto?

[A] Algunas apps son más importantes que otras
    └─ Elige: Weighted Average ⭐ RECOMENDADO

[B] Todas las apps tienen igual importancia  
    └─ Elige: Simple Average

[C] TODAS deben estar completas para tener éxito
    └─ Elige: Minimum Progress
```

### Paso 3: Define Estados a Incluir
```
¿Quieres contar apps sin iniciar?

[A] No, solo trabajo activo y completado
    └─ Unchecked: To Be Started
       ✓ Work in Progress
       ✓ Closed

[B] Sí, todo incluyendo lo no iniciado
    └─ ✓ To Be Started
       ✓ Work in Progress
       ✓ Closed

[C] Solo trabajo completado (auditoría)
    └─ Unchecked: To Be Started
       Unchecked: Work in Progress
       ✓ Closed
```

### Paso 4: Configura Pesos (si Weighted)
```
Minimum Weight:  0.5  (por defecto: apps menos importantes)
Maximum Weight:  3.0  (por defecto: apps muy importantes)
Default Weight:  1.0  (por defecto: apps normales)

¿Cómo asignar a cada app?
- 0.5 = NO es importante comparada con otras
- 1.0 = Importancia normal/estándar
- 2.0 = MÁS importante que normal
- 3.0 = MUY CRÍTICA, falla detiene todo
```

### Paso 5: Boosting por Criticidad
```
¿Qué apps son estratégicamente críticas?

Multiplicadores (default):
- Low Criticality:   1.0  (sin boost)
- Medium Criticality: 1.0  (sin boost)  
- High Criticality:   1.2  (20% boost)

Aumentar si tienes apps que si fallan, falla todo:
- Cambiar High a: 1.5 o 2.0
```

### Paso 6: Fórmula Global
```
¿Cómo combinar BUs en reporte general?

[A] BUs grandes influyen más
    └─ Elige: Weighted by BU Size

[B] Todas las BUs cuentan igual
    └─ Elige: Simple Average
```

### Paso 7: Guarda y Prueba
```
[Botón] Save Configuration  → Guarda cambios
[Botón] Test Calculation    → Ve resultado en tiempo real
[Botón] Reset to Defaults   → Vuelve a valores por defecto
```

---

## 📊 Entender tu Progreso

### Fórmula = Promedio Inteligente

```
Imagine tienes 3 apps:

APP 1          APP 2          APP 3
70% done       100% done      30% done
Peso: 1        Peso: 3        Peso: 0.5

┌─────────────────────────────────────────┐
│ Cálculo:                                │
│                                         │
│ (70×1) + (100×3) + (30×0.5)             │
│ ─────────────────────────────────      │
│         1 + 3 + 0.5                     │
│                                         │
│ = 70 + 300 + 15 = 385                   │
│   ───────────────   ──                  │
│       4.5            4.5                │
│                                         │
│ = 85.6% ✓                               │
│                                         │
│ APP 2 (peso 3) influye MUCHO            │
│ APP 1 (peso 1) influye NORMAL           │
│ APP 3 (peso 0.5) influye POCO           │
└─────────────────────────────────────────┘
```

### Por Qué Pesa Más

```
Aplicación importante         Aplicación normal
(peso 3.0)                    (peso 1.0)

A 100% progreso              A 100% progreso
Contribuye: 300 puntos       Contribuye: 100 puntos

¿Resultado? 3 veces más importante
```

### Con Criticidad

```
App Normal                    App Crítica
Peso: 2.0                     Peso: 2.0
Criticidad: Medium (1.0)      Criticidad: High (1.2)

Contribución: 2.0 × 1.0       Contribución: 2.0 × 1.2
           = 2.0                           = 2.4

La app crítica cuenta 20% más
```

---

## 🎨 Presets Listos para Usar

### Preset 1: Startup/Pequeño Equipo

```json
{
  "progressMethod": "weighted",
  "globalMethod": "simple",
  "statusInclusion": {
    "TBS": true,
    "WIP": true,
    "CLO": true
  },
  "weights": {
    "min": 0.5,
    "max": 2.0,
    "default": 1.0
  },
  "criticalityMultipliers": {
    "low": 1.0,
    "medium": 1.1,
    "high": 1.3
  }
}
```

**Cuándo usar**: Equipo pequeño, pocas apps.

---

### Preset 2: Empresa Grande/Portafolio

```json
{
  "progressMethod": "weighted",
  "globalMethod": "weighted",
  "statusInclusion": {
    "TBS": false,
    "WIP": true,
    "CLO": true
  },
  "weights": {
    "min": 0.3,
    "max": 5.0,
    "default": 1.0
  },
  "criticalityMultipliers": {
    "low": 0.9,
    "medium": 1.0,
    "high": 1.5
  }
}
```

**Cuándo usar**: Portafolio grande, apps con distinta importancia.

---

### Preset 3: Solo Completado (Auditoría)

```json
{
  "progressMethod": "minimum",
  "globalMethod": "simple",
  "statusInclusion": {
    "TBS": false,
    "WIP": false,
    "CLO": true
  },
  "weights": {
    "min": 1.0,
    "max": 1.0,
    "default": 1.0
  },
  "criticalityMultipliers": {
    "low": 1.0,
    "medium": 1.0,
    "high": 1.0
  }
}
```

**Cuándo usar**: Solo importa lo completado (compliance, auditoría).

---

### Preset 4: Agile/Iterativo

```json
{
  "progressMethod": "weighted",
  "globalMethod": "weighted",
  "statusInclusion": {
    "TBS": false,
    "WIP": true,
    "CLO": true
  },
  "weights": {
    "min": 0.5,
    "max": 3.0,
    "default": 1.0
  },
  "criticalityMultipliers": {
    "low": 1.0,
    "medium": 1.1,
    "high": 1.2
  }
}
```

**Cuándo usar**: Metodología iterativa, énfasis en WIP.

---

## ⚡ Cambios Comunes

### "Quiero que apps críticas impacten MÁS"

```
Actual:  High Criticality = 1.2
Cambiar: High Criticality = 1.5  (25% más)
         o incluso      = 2.0   (100% más)
```

### "No quiero contar apps sin iniciar"

```
Actual:  To Be Started ✓ (checked)
Cambiar: To Be Started ☐ (unchecked)
```

### "Quiero que todas las apps importen igual"

```
Cambiar a: Simple Average
O configura todos los pesos = 1.0
           todos multiplicadores = 1.0
```

### "Quiero ser más conservador"

```
Cambiar a: Minimum Progress
(progreso = la app con menos avance)
```

---

## ✅ Validación

### Cómo saber si está bien

```
1. Haz clic: Test Calculation
   ↓
2. Ve: fórmulas aplicadas paso a paso
   ↓
3. Pregúntate: ¿Tiene sentido este número?
   ↓
4. Si NO: Ajusta parámetros y repite
   ↓
5. Si SÍ: Haz clic Save Configuration ✓
```

### Indicadores de Problema

```
❌ Progreso muy bajo
   → Aumenta Max Weight
   → Aumenta Criticality Multipliers
   → Excluye TBS

❌ Progreso muy alto
   → Disminuye Max Weight
   → Disminuye Criticality Multipliers
   → Incluye TBS

❌ Una app domina todo
   → Disminuye su Weight
   → Disminuye su Criticality Multiplier
```

---

## 📌 Recordar

1. **Pesos**: Qué tan importante es cada app
2. **Criticidad**: Qué tan estratégica es
3. **Estados**: Qué trabajo contar (TBS/WIP/CLO)
4. **Método**: Cómo agregar (weighted/simple/minimum)
5. **Global**: Cómo combinar BUs

---

## 🔄 Exportar/Importar

```
Guardar configuración:
Setup → Calculation Formulas → Save Configuration
  ↓
Settings → Export Configuration
  ↓
Archivo JSON con TODOS los parámetros

Restaurar:
Settings → Import Configuration
  ↓
Selecciona archivo JSON
  ↓
Automáticamente restaura TODO
```

---

## 🆘 SOS Rápido

| Problema | Solución |
|----------|----------|
| No aparece progreso | Incluye al menos un estado (WIP o CLO) |
| Progreso = 0% | Apps en TBS, cambia status o excluye TBS |
| Una app domina | Reduce su peso o criticidad |
| Resultado NO tiene sentido | Haz Test Calculation, ve paso a paso |
| Quiero volver a defaults | Botón Reset to Defaults |

---

**Versión**: 1.0 | **Quick Start**: 5 minutos | **Última actualización**: Octubre 2025

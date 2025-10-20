# 📊 Manual de Configuración de Fórmulas - Dashboard Enhanced

**Última actualización**: Octubre 2025  
**Versión**: 1.0  
**Audiencia**: Administradores de proyectos y analistas de datos

---

## 📖 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Acceso al Panel de Fórmulas](#acceso-al-panel-de-fórmulas)
3. [Parámetros Principales](#parámetros-principales)
4. [Cálculo de Progreso Ponderado](#cálculo-de-progreso-ponderado)
5. [Ejemplos Prácticos](#ejemplos-prácticos)
6. [Exportar e Importar Configuración](#exportar-e-importar-configuración)
7. [Preguntas Frecuentes](#preguntas-frecuentes)

---

## Introducción

### ¿Qué son las Fórmulas de Cálculo?

Las fórmulas de cálculo permiten personalizar cómo el dashboard calcula el progreso general de cada unidad de negocio (BU). Puedes ajustar:

- **Métodos de cálculo** para progreso individual y global
- **Inclusión de estados** (qué estados contar o ignorar)
- **Pesos de aplicaciones** (aplicaciones más importantes cuentan más)
- **Multiplicadores de criticidad** (boost para aplicaciones críticas)

### ¿Por Qué Personalizar las Fórmulas?

Diferentes organizaciones tienen diferentes necesidades:

- **Equipos ágiles**: Pueden querer dar más peso a aplicaciones en progreso
- **Proyectos críticos**: Pueden requerir multiplicadores altos para apps críticas
- **Auditoría**: Pueden necesitar incluir/excluir estados específicos
- **Reporting**: Pueden necesitar métodos de cálculo más simples o complejos

### Conceptos Clave

| Término | Significado |
|---------|------------|
| **BU (Business Unit)** | Unidad de negocio (departamento, producto o línea de negocio) |
| **Aplicación** | Sistema de software bajo el control del proyecto |
| **Estado** | Situación actual (To Be Started, Work in Progress, Closed) |
| **Peso (Weight)** | Importancia relativa de una aplicación (0.5 = menos importante, 3.0 = muy importante) |
| **Criticidad** | Nivel de importancia estratégica (Low, Medium, High) |
| **Multiplicador** | Factor que amplifica el impacto de la criticidad |
| **Progreso Ponderado** | Promedio ponderado que considera pesos y criticidad |

---

## Acceso al Panel de Fórmulas

### Paso 1: Abrir Setup

1. En el dashboard principal, haz clic en el botón **Setup** (arriba a la derecha)
2. Se abrirá el modal de "Project Administration"

### Paso 2: Navegar a "Calculation Formulas"

1. Verás 6 pestañas en el modal:
   - Business Units
   - Applications
   - Applications Overview
   - Whitelabel
   - **Calculation Formulas** ← Aquí
   - Settings

2. Haz clic en la pestaña **"Calculation Formulas"**

### Paso 3: Ver el Panel

El panel se divide en 5 secciones:

```text
┌─────────────────────────────────────────────────────────────────────┐
│  📊 PANEL DE FÓRMULAS DE CÁLCULO                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ☐ Progress Calculation   ☑ Status Inclusion   ◈ Weight Parameters │
│  Method (BU Progress)     Rules                                     │
│                                                                     │
│  ◈ Criticality Multipliers ◈ Global Progress Formula               │
│  Per Level                 Overall Progress Method                 │
│                                                                     │
│  [Save Configuration] [Reset to Defaults] [Test Calculation]      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Parámetros Principales

### 1. Progress Calculation Method (Método de Cálculo de Progreso BU)

**Ubicación**: Primera sección izquierda

**Descripción**: Define cómo se calcula el progreso de cada Business Unit basado en sus aplicaciones.

#### Opciones Disponibles:

##### 📊 **Weighted Average (Promedio Ponderado)** - RECOMENDADO
- **Fórmula**:
  ```
  BU Progress = Σ(App Progress × Weight) / Σ(Weight)
  ```
- **Ejemplo**:
  - App A: 50% progress, weight 1.0
  - App B: 100% progress, weight 2.0
  - Cálculo: (50×1.0 + 100×2.0) / (1.0 + 2.0) = 250/3 = 83.33%

- **Cuándo usar**: Cuando necesitas que aplicaciones más importantes influyan más en el progreso total
- **Ventaja**: Flexible y realista
- **Desventaja**: Más complejo de entender

##### 🔢 **Simple Average (Promedio Simple)**
- **Fórmula**:
  ```
  BU Progress = Σ(App Progress) / Count(Apps)
  ```
- **Ejemplo**:
  - App A: 50%
  - App B: 100%
  - Cálculo: (50 + 100) / 2 = 75%

- **Cuándo usar**: Cuando todas las aplicaciones tienen igual importancia
- **Ventaja**: Fácil de entender y comunicar
- **Desventaja**: No considera prioridades

##### ⏱️ **Minimum Progress (Mínimo Progreso)**
- **Fórmula**:
  ```
  BU Progress = MIN(App1 Progress, App2 Progress, ...)
  ```
- **Ejemplo**:
  - App A: 50%
  - App B: 100%
  - Cálculo: MIN(50, 100) = 50%

- **Cuándo usar**: Para proyectos donde TODAS las aplicaciones deben completarse
- **Ventaja**: Refleja realidad de proyectos de portafolio
- **Desventaja**: Conservador, puede desmoralizar

---

### 2. Status Inclusion Rules (Reglas de Inclusión de Estados)

**Ubicación**: Segunda sección (Status Inclusion)

**Descripción**: Define qué estados incluir en los cálculos de progreso.

#### Estados Disponibles:

| Estado | Código | Significado | Por defecto |
|--------|--------|-------------|------------|
| **To Be Started** | TBS | No ha comenzado | ❌ NO incluir |
| **Work in Progress** | WIP | En progreso | ✅ Incluir |
| **Closed** | CLO | Completado | ✅ Incluir |

#### Comportamiento:

- **Si INCLUYES TBS**: Aplicaciones no iniciadas cuentan como 0% en cálculos
- **Si EXCLUYES TBS**: Aplicaciones no iniciadas se ignoran completamente
- **Si INCLUYES WIP**: Aplicaciones en progreso contribuyen al cálculo
- **Si EXCLUYES WIP**: Solo aplicaciones completas cuentan

#### Ejemplos de Escenarios:

**Escenario 1**: Proyecto con muchas aplicaciones pendientes
```
✅ To Be Started (incluir)
✅ Work in Progress (incluir)
✅ Closed (incluir)
Resultado: Muestra el progreso real incluyendo lo no iniciado
```

**Escenario 2**: Reportes ejecutivos (solo trabajo actual)
```
❌ To Be Started (excluir)
✅ Work in Progress (incluir)
✅ Closed (incluir)
Resultado: Muestra progreso de trabajo activo, ignora lo pendiente
```

**Escenario 3**: Auditoría (solo completado)
```
❌ To Be Started (excluir)
❌ Work in Progress (excluir)
✅ Closed (incluir)
Resultado: Muestra solo aplicaciones completadas (más conservador)
```

---

### 3. Weight Parameters (Parámetros de Peso)

**Ubicación**: Tercera sección (Weight Parameters)

**Descripción**: Define el rango de pesos que pueden asignarse a aplicaciones.

#### Parámetros:

| Parámetro | Rango | Por Defecto | Significado |
|-----------|-------|------------|------------|
| **Minimum Weight** | 0.1 - 2.0 | 0.5 | Peso más bajo permitido para aplicación |
| **Maximum Weight** | 1.0 - 10.0 | 3.0 | Peso máximo permitido para aplicación |
| **Default Weight** | Min - Max | 1.0 | Peso asignado automáticamente a nuevas apps |

#### Cómo se Usan:

Cuando creas o editas una aplicación, puedes asignarle un peso:

```
Peso 0.5 = Aplicación menos importante
Peso 1.0 = Aplicación estándar/normalizada
Peso 3.0 = Aplicación muy importante (crítica)
```

#### Fórmula de Aplicación:

En el cálculo ponderado:
```
App Contribution = App Progress × App Weight
```

#### Ejemplo Práctico:

**Configuración de Pesos**: Min=0.5, Max=3.0, Default=1.0

| Aplicación | Peso | Progreso | Contribución |
|------------|------|----------|--------------|
| CRM Sistema | 0.5 | 100% | 50% |
| Payment Gateway | 3.0 | 75% | 225% |
| Dashboard | 1.0 | 90% | 90% |
| **Total Ponderado** | 4.5 | - | **365/450 = 81%** |

---

### 4. Criticality Multipliers (Multiplicadores de Criticidad)

**Ubicación**: Cuarta sección (Criticality Multipliers)

**Descripción**: Define cómo la criticidad de una aplicación amplifica su impacto.

#### Niveles de Criticidad:

| Nivel | Multiplicador Defecto | Significado |
|------|---------------------|------------|
| **Low** | 1.0 | Impacto normal, no amplificado |
| **Medium** | 1.0 | Impacto normal, no amplificado |
| **High** | 1.2 | 20% de aumento de impacto |

#### Cómo se Usan:

Los multiplicadores amplian el peso de una aplicación basado en su criticidad:

```
Weighted Contribution = App Progress × App Weight × Criticality Multiplier
```

#### Ejemplo Práctico:

**Configuración**: Low=1.0, Medium=1.0, High=1.2

| Aplicación | Peso | Criticidad | Mult. | Progreso | Contribución |
|------------|------|-----------|-------|----------|--------------|
| Reporting | 1.0 | Low | 1.0 | 85% | 85% |
| Analytics | 2.0 | Medium | 1.0 | 90% | 180% |
| Auth System | 2.0 | High | 1.2 | 70% | **168%** |
| **Total** | 5.0 | - | - | - | **433/600 = 72.2%** |

#### Cuándo Aumentar Multiplicadores:

- **Aumento a 1.2 - 1.5**: Apps críticas que impactan directamente al negocio
- **Aumento a 1.5 - 2.0**: Apps que si fallan detienen toda operación
- **Sin cambios (1.0)**: Apps estándares o no críticas

---

### 5. Global Progress Formula (Fórmula de Progreso Global)

**Ubicación**: Quinta sección (Global Progress Formula)

**Descripción**: Define cómo se calcula el progreso general del portafolio combinando todas las BUs.

#### Opciones:

##### 📊 **Weighted by BU Size**
- **Fórmula**:
  ```
  Global Progress = Σ(BU Progress × BU App Count) / Σ(BU App Count)
  ```
- **Significado**: Las BUs con más aplicaciones influyen más
- **Ejemplo**:
  - BU A: 80% (5 apps) → 400
  - BU B: 60% (2 apps) → 120
  - Total: 520/7 = 74.3%
- **Cuándo usar**: Para reportes de portafolio donde tamaño importa

##### 🔢 **Simple Average**
- **Fórmula**:
  ```
  Global Progress = Σ(BU Progress) / Count(BUs)
  ```
- **Significado**: Todas las BUs cuentan igual
- **Ejemplo**:
  - BU A: 80%
  - BU B: 60%
  - Total: 140/2 = 70%
- **Cuándo usar**: Para equipos con BUs similares en tamaño

---

## Cálculo de Progreso Ponderado

### Fórmula Completa (Weighted Average)

```
┌─────────────────────────────────────────────────────────────┐
│ FÓRMULA DE PROGRESO PONDERADO COMPLETA                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BU Progress = Σ(App[i] Progress × App[i] Weight           │
│                  × Criticality Multiplier[App[i]])          │
│                ─────────────────────────────────────        │
│                Σ(App[i] Weight                              │
│                  × Criticality Multiplier[App[i]])          │
│                                                             │
│  Donde:                                                     │
│  • App[i] Progress    = Progreso de la aplicación (0-100%) │
│  • App[i] Weight      = Peso asignado (0.5-3.0)            │
│  • Criticality Mult.  = Multiplicador de criticidad         │
│                        (1.0, 1.2, 1.5, etc.)               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Paso a Paso - Ejemplo Completo

**Configuración**:
- Progress Method: Weighted Average
- Status Inclusion: Incluir TBS, WIP, CLO
- Weights: Min=0.5, Default=1.0, Max=3.0
- Criticality: Low=1.0, Medium=1.0, High=1.2

**Datos de Aplicaciones**:

| App | Estado | Progress | Weight | Criticidad | Mult. |
|-----|--------|----------|--------|-----------|-------|
| CRM | CLO | 100% | 1.0 | Low | 1.0 |
| Portal | WIP | 75% | 2.0 | High | 1.2 |
| API | TBS | 0% | 0.5 | Medium | 1.0 |
| Reports | CLO | 90% | 1.5 | High | 1.2 |

**Cálculo Paso a Paso**:

```
Paso 1: Calcular numerador (suma ponderada)
────────────────────────────────────────────
CRM:     100 × 1.0 × 1.0 = 100
Portal:   75 × 2.0 × 1.2 = 180
API:       0 × 0.5 × 1.0 = 0
Reports:  90 × 1.5 × 1.2 = 162
                           ─────
Numerador Total:            442

Paso 2: Calcular denominador (suma de pesos ponderados)
─────────────────────────────────────────────────────
CRM:     1.0 × 1.0 = 1.0
Portal:  2.0 × 1.2 = 2.4
API:     0.5 × 1.0 = 0.5
Reports: 1.5 × 1.2 = 1.8
                    ─────
Denominador Total:   5.7

Paso 3: Dividir
───────────────
BU Progress = 442 / 5.7 = 77.54%

RESULTADO: La BU tiene 77.54% de progreso
```

### Interpretación de Resultados

| Rango | Interpretación | Acción |
|-------|----------------|--------|
| 0-20% | Proyecto en fase inicial | Monitorear inicio |
| 21-50% | En progreso activo | Seguimiento normal |
| 51-80% | Avance significativo | Acelerar final |
| 81-99% | Casi completado | Cerrar pendientes |
| 100% | Completado | Validar y cerrar |

---

## Ejemplos Prácticos

### Caso 1: Startup Tecnológica

**Contexto**: Equipo pequeño, pocas apps, todas críticas

**Configuración Recomendada**:
```
Progress Method:       Weighted Average
Status Inclusion:      ✅ TBS, ✅ WIP, ✅ CLO
Minimum Weight:        0.5
Default Weight:        1.0
Maximum Weight:        2.0 (menos variabilidad)
Low Multiplier:        1.0
Medium Multiplier:     1.1
High Multiplier:       1.3
Global Formula:        Simple Average
```

**Justificación**: Todas las apps son críticas, no hay mucha diferencia de peso.

---

### Caso 2: Empresa Grande (Múltiples BUs)

**Contexto**: Portafolio grande, aplicaciones con diferentes importancias

**Configuración Recomendada**:
```
Progress Method:       Weighted Average
Status Inclusion:      ❌ TBS, ✅ WIP, ✅ CLO
Minimum Weight:        0.3 (permite peso bajo)
Default Weight:        1.0
Maximum Weight:        5.0 (apps muy críticas)
Low Multiplier:        0.9 (reduce impacto)
Medium Multiplier:     1.0
High Multiplier:       1.5 (aumenta mucho)
Global Formula:        Weighted by BU Size
```

**Justificación**: Muchas variaciones, apps críticas deben impactar más.

---

### Caso 3: Auditoría/Compliance

**Contexto**: Solo interesa lo completado, sin progreso parcial

**Configuración Recomendada**:
```
Progress Method:       Minimum Progress
Status Inclusion:      ❌ TBS, ❌ WIP, ✅ CLO
Minimum Weight:        1.0
Default Weight:        1.0
Maximum Weight:        1.0
Low Multiplier:        1.0
Medium Multiplier:     1.0
High Multiplier:       1.0
Global Formula:        Simple Average
```

**Justificación**: Solo cosas completas cuentan. Sin ponderación.

---

### Caso 4: Agile/Metodología Iterativa

**Contexto**: Énfasis en trabajo en progreso, entregas incrementales

**Configuración Recomendada**:
```
Progress Method:       Weighted Average
Status Inclusion:      ❌ TBS, ✅ WIP, ✅ CLO
Minimum Weight:        0.5
Default Weight:        1.0
Maximum Weight:        3.0
Low Multiplier:        1.0
Medium Multiplier:     1.1
High Multiplier:       1.2
Global Formula:        Weighted by BU Size
```

**Justificación**: Incluye WIP, pero no TBS. Permite variación de pesos.

---

## Exportar e Importar Configuración

### Exportar Configuración de Fórmulas

**¿Por qué?** Para backup, compartir con equipo, o usar en otro proyecto.

**Pasos**:

1. Haz clic en Setup → Calculation Formulas
2. Configura los parámetros deseados
3. Haz clic en **"Save Configuration"**
4. Ve a Settings → Export Configuration
5. Se descargará un archivo JSON con:
   - Estructura de BUs y Apps
   - **Configuración de fórmulas completa**
   - Configuración Whitelabel (si existe)

**Contenido del Export**:
```json
{
  "buses": [...],
  "apps": [...],
  "waves": [...],
  "formulaConfig": {
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
      "medium": 1.0,
      "high": 1.2
    },
    "timestamp": "2025-10-20T14:30:00Z"
  },
  "whitelabel": {...},
  "metadata": {
    "exportedAt": "2025-10-20T14:30:00Z",
    "version": "2.1",
    "schema": "dashboard_config_v1_enriched_with_formulas",
    "includesFormulaConfig": true,
    "includesWhitelabelConfig": true
  }
}
```

---

### Importar Configuración de Fórmulas

**¿Por qué?** Para restaurar una configuración anterior o usar configuración de referencia.

**Pasos**:

1. Ve a Settings → Import Configuration
2. Selecciona el archivo JSON exportado previamente
3. El dashboard automáticamente:
   - ✅ Restaurará estructura de BUs y Apps
   - ✅ **Restaurará configuración de fórmulas**
   - ✅ Restaurará configuración Whitelabel
   - ✅ Recalculará todo progreso
4. Se recargará la página automáticamente

**Notas**:
- ✅ Soporta archivos sin formulaConfig (compatible hacia atrás)
- ✅ Valida estructura antes de importar
- ✅ Muestra confirmación visual de lo importado
- ❌ No se puede importar solo fórmulas (siempre va con proyecto)

---

## Preguntas Frecuentes

### ❓ P1: ¿Qué diferencia hay entre Weighted Average y Simple Average?

**R**: 
- **Weighted**: Aplicaciones más importantes (peso alto) cuentan más
- **Simple**: Todas las apps cuentan igual

**Ejemplo**:
- App Crítica: 50% (peso 3.0)
- App Normal: 100% (peso 1.0)
- **Weighted**: (50×3 + 100×1) / 4 = 62.5%
- **Simple**: (50 + 100) / 2 = 75%

### ❓ P2: ¿Cuándo debo usar Minimum Progress?

**R**: Solo cuando **TODAS** las aplicaciones son críticas y deben completarse antes de dar proyecto por exitoso.

**Ejemplo**: Migración de datos - si una sola tabla no migra, proyecto falla.

### ❓ P3: ¿Puedo cambiar fórmulas en medio del proyecto?

**R**: Sí, pero los números históricos cambiarán. **Recomendación**: Decide fórmulas al inicio y mantenlas estables para comparabilidad.

### ❓ P4: ¿Qué pasa si no incluyo aplicaciones TBS?

**R**: 
- **Si incluyes**: Aplicaciones no iniciadas = 0%, reducen el promedio
- **Si excluyes**: Se ignoran completamente, no afectan cálculo

**Impacto**: Excluir TBS hace que progreso se vea más alto.

### ❓ P5: ¿Cómo sé qué pesos asignar?

**R**: Preguntas clave:
- ¿Cuánto impactaría si esta app falla? → Criticidad
- ¿Comparada con otras, es más importante? → Peso alto
- ¿Es estándar? → Peso 1.0
- ¿Es menor? → Peso 0.5

### ❓ P6: ¿Puedo tener multiplicadores > 1.2?

**R**: Sí, puedes configurar cualquier valor. Recomendaciones:
- **1.0 - 1.2**: Pequeño boost para críticas
- **1.2 - 1.5**: Boost moderado
- **> 1.5**: Reservado para apps de impacto máximo

### ❓ P7: ¿Qué significa "Weighted by BU Size"?

**R**: En progreso global, BUs con más apps influyen más que BUs pequeñas.

**Ejemplo**:
- BU A (5 apps): 80% → cuenta más
- BU B (1 app): 50% → cuenta menos
- Global ponderado diferente de simple average

### ❓ P8: ¿Se pierden fórmulas si limpio datos?

**R**: No. Al hacer "Clear All Data", se eliminan BUs/Apps pero las fórmulas se mantienen en localStorage. Al resetear, vuelven los defaults.

### ❓ P9: ¿Puedo exportar solo la configuración de fórmulas?

**R**: No, se exporta con todo el proyecto. Pero puedes:
1. Exportar proyecto
2. Compartir el JSON
3. Otros importan y obtienen fórmulas automáticamente

### ❓ P10: ¿Cómo valido que mis fórmulas están correctas?

**R**: Usa **"Test Calculation"**:
1. En Calculation Formulas → botón "Test Calculation"
2. Verá simulación con datos actuales
3. Verá fórmulas aplicadas paso a paso
4. Podrá ajustar si no es lo deseado

---

## 🎓 Resumen Rápido

### Proceso de Configuración

```
1. Accede a Setup → Calculation Formulas
2. Elige Progress Method (qué fórmula para BU)
3. Define Status Inclusion (qué estados contar)
4. Configura Weights (rango de importancia)
5. Ajusta Criticality Multipliers (boost para críticas)
6. Elige Global Formula (cómo combinar BUs)
7. Guarda con "Save Configuration"
8. Prueba con "Test Calculation"
```

### Variables a Recordar

| Variable | Rango | Defecto | Impacto |
|----------|-------|---------|--------|
| Progress Method | 3 opciones | Weighted | **Alto** |
| Status Inclusion | TBS/WIP/CLO | Incluir WIP,CLO | **Alto** |
| Min Weight | 0.3 - 2.0 | 0.5 | Bajo |
| Max Weight | 1.0 - 10.0 | 3.0 | **Alto** |
| Default Weight | Min - Max | 1.0 | Medio |
| Low Multiplier | 0.5 - 1.5 | 1.0 | Bajo |
| Medium Multiplier | 0.5 - 1.5 | 1.0 | Bajo |
| High Multiplier | 1.0 - 2.0 | 1.2 | **Alto** |
| Global Formula | 2 opciones | Weighted | Medio |

---

## 📞 Soporte

Si tienes preguntas adicionales:

1. Consulta la documentación técnica en `docs/technical/`
2. Revisa ejemplos de configuración en `docs/guides/`
3. Contacta al equipo de administración

---

**Última actualización**: Octubre 2025  
**Documento**: Formula Configuration Guide v1.0

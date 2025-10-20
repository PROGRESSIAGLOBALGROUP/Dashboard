# Manual de Configuración de Fórmulas de Cálculo

**Última actualización**: Octubre 2025  
**Versión**: 1.0

---

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Acceso al Panel](#acceso-al-panel)
3. [Parámetros Principales](#parámetros-principales)
4. [Cálculo Ponderado](#cálculo-ponderado)
5. [Ejemplos Prácticos](#ejemplos-prácticos)
6. [FAQ](#faq)

---

## Introducción

### ¿Qué son las Fórmulas de Cálculo?

Las fórmulas personalizan cómo el dashboard calcula el progreso de cada Business Unit (BU). Te permite ajustar:

- **Métodos de cálculo**: Diferentes formas de agregar aplicaciones
- **Inclusión de estados**: Qué estados contar o ignorar
- **Pesos de aplicaciones**: Aplicaciones importantes cuentan más
- **Multiplicadores de criticidad**: Boost para aplicaciones críticas

### ¿Por Qué Personalizar?

Diferentes contextos requieren diferentes cálculos:

- **Equipos ágiles**: Dan más peso a trabajo en progreso
- **Proyectos críticos**: Multiplicadores altos para apps críticas
- **Auditoría**: Solo incluyen trabajo completado
- **Reporting**: Usan cálculos simples y entendibles

### Conceptos Clave

| Concepto | Significado |
|----------|------------|
| **BU** | Business Unit (unidad de negocio) |
| **Aplicación** | Sistema de software en el proyecto |
| **Estado** | Situación actual (TBS, WIP, CLO) |
| **Peso** | Importancia relativa (0.5=baja, 3.0=alta) |
| **Criticidad** | Nivel de importancia estratégica |
| **Multiplicador** | Factor de amplificación de criticidad |

---

## Acceso al Panel

### Paso 1: Abrir Setup

Haz clic en el botón **Setup** (arriba a la derecha del dashboard).

### Paso 2: Navegar a Fórmulas

En el modal que se abre, haz clic en la pestaña **"Calculation Formulas"**.

### Paso 3: Ver las Secciones

El panel contiene 5 secciones principales:

- **Progress Calculation Method**: Fórmula para cada BU
- **Status Inclusion Rules**: Qué estados incluir
- **Weight Parameters**: Rango de pesos
- **Criticality Multipliers**: Boost por criticidad
- **Global Progress Formula**: Cómo combinar BUs

---

## Parámetros Principales

### 1. Progress Calculation Method

Define cómo se calcula el progreso de cada BU.

#### Weighted Average (RECOMENDADO)

**Fórmula**: `BU Progress = Σ(App Progress × Weight) / Σ(Weight)`

**Ejemplo**:
- App A: 50% progress, weight 1.0
- App B: 100% progress, weight 2.0
- Resultado: (50×1 + 100×2) / 3 = 83%

**Cuándo usar**: Cuando necesitas que apps importantes influyan más.

**Ventajas**: Flexible, realista.
**Desventajas**: Más complejo de entender.

#### Simple Average

**Fórmula**: `BU Progress = Σ(App Progress) / Count(Apps)`

**Ejemplo**:
- App A: 50%
- App B: 100%
- Resultado: 75%

**Cuándo usar**: Cuando todas las apps tienen igual importancia.

**Ventajas**: Fácil de entender.
**Desventajas**: No considera prioridades.

#### Minimum Progress

**Fórmula**: `BU Progress = MIN(App1, App2, ...)`

**Ejemplo**:
- App A: 50%
- App B: 100%
- Resultado: 50%

**Cuándo usar**: Cuando TODAS las apps deben completarse.

**Ventajas**: Refleja realidad de portafolios.
**Desventajas**: Muy conservador.

---

### 2. Status Inclusion Rules

Define qué estados incluir en cálculos.

| Estado | Código | Significado | Por Defecto |
|--------|--------|-------------|------------|
| To Be Started | TBS | No ha comenzado | NO |
| Work in Progress | WIP | En progreso | SÍ |
| Closed | CLO | Completado | SÍ |

**Comportamiento**:

- **Incluir TBS**: Apps sin iniciar cuentan como 0%
- **Excluir TBS**: Apps sin iniciar se ignoran
- **Incluir WIP**: Apps en progreso contribuyen
- **Excluir WIP**: Solo apps completadas cuentan

**Escenarios comunes**:

1. **Desarrollo normal**: Incluir TBS + WIP + CLO
2. **Reportes ejecutivos**: Excluir TBS, incluir WIP + CLO
3. **Auditoría**: Solo CLO
4. **Agile**: Excluir TBS, incluir WIP + CLO

---

### 3. Weight Parameters

Define el rango de pesos para aplicaciones.

| Parámetro | Rango | Por Defecto |
|-----------|-------|------------|
| Minimum Weight | 0.1 - 2.0 | 0.5 |
| Maximum Weight | 1.0 - 10.0 | 3.0 |
| Default Weight | Min - Max | 1.0 |

**Significado**:

- **Min Weight**: Peso más bajo permitido
- **Max Weight**: Peso máximo permitido
- **Default**: Se asigna automáticamente a nuevas apps

**Uso en cálculos**:

```
App Contribution = App Progress × App Weight
```

**Ejemplo**:

| App | Peso | Progreso | Contribución |
|-----|------|----------|--------------|
| CRM | 0.5 | 100% | 50% |
| Payment | 3.0 | 75% | 225% |
| Dashboard | 1.0 | 90% | 90% |
| Total | 4.5 | - | 365/450 = 81% |

---

### 4. Criticality Multipliers

Define cómo la criticidad amplifica el impacto.

| Nivel | Multiplicador Defecto |
|------|---------------------|
| Low | 1.0 |
| Medium | 1.0 |
| High | 1.2 |

**Cómo funciona**:

```
Contribution = App Progress × App Weight × Criticality Multiplier
```

**Ejemplo**:

| App | Peso | Crit. | Mult. | Progreso | Contrib. |
|-----|------|-------|-------|----------|----------|
| Reporting | 1.0 | Low | 1.0 | 85% | 85% |
| Analytics | 2.0 | Med | 1.0 | 90% | 180% |
| Auth | 2.0 | High | 1.2 | 70% | 168% |
| Total | 5.0 | - | - | - | 433/600 = 72% |

**Cuándo aumentar multiplicadores**:

- **1.2 - 1.5**: Apps críticas del negocio
- **1.5 - 2.0**: Apps cuya falla detiene todo
- **Sin cambios**: Apps estándares

---

### 5. Global Progress Formula

Cómo combinar BUs en progreso global.

#### Weighted by BU Size

**Fórmula**: `Global = Σ(BU Progress × BU App Count) / Σ(BU App Count)`

BUs con más apps influyen más.

**Ejemplo**:
- BU A (5 apps): 80% → 400
- BU B (2 apps): 60% → 120
- Total: 520/7 = 74%

#### Simple Average

**Fórmula**: `Global = Σ(BU Progress) / Count(BUs)`

Todas las BUs cuentan igual.

**Ejemplo**:
- BU A: 80%
- BU B: 60%
- Total: 70%

---

## Cálculo Ponderado

### Fórmula Completa

```
BU Progress = Σ(App[i] Progress × App[i] Weight × Criticality Mult[i])
              ──────────────────────────────────────────────────────
              Σ(App[i] Weight × Criticality Mult[i])
```

### Ejemplo Paso a Paso

**Configuración**:
- Method: Weighted Average
- Status: TBS, WIP, CLO incluidos
- Weights: Min=0.5, Default=1.0, Max=3.0
- Criticality: Low=1.0, Med=1.0, High=1.2

**Datos**:

| App | Estado | Progress | Weight | Crit. | Mult. |
|-----|--------|----------|--------|-------|-------|
| CRM | CLO | 100% | 1.0 | Low | 1.0 |
| Portal | WIP | 75% | 2.0 | High | 1.2 |
| API | TBS | 0% | 0.5 | Med | 1.0 |
| Reports | CLO | 90% | 1.5 | High | 1.2 |

**Cálculo**:

```
Numerador:
CRM:     100 × 1.0 × 1.0 = 100
Portal:   75 × 2.0 × 1.2 = 180
API:       0 × 0.5 × 1.0 = 0
Reports:  90 × 1.5 × 1.2 = 162
                          = 442

Denominador:
CRM:     1.0 × 1.0 = 1.0
Portal:  2.0 × 1.2 = 2.4
API:     0.5 × 1.0 = 0.5
Reports: 1.5 × 1.2 = 1.8
                    = 5.7

Resultado: 442 / 5.7 = 77.54%
```

---

## Ejemplos Prácticos

### Caso 1: Startup Tecnológica

**Contexto**: Equipo pequeño, pocas apps, todas críticas.

**Configuración**:
- Progress Method: Weighted Average
- Status: Incluir TBS, WIP, CLO
- Weights: Min=0.5, Default=1.0, Max=2.0
- Criticality: Low=1.0, Med=1.1, High=1.3
- Global: Simple Average

**Justificación**: Todas las apps son críticas, sin mucha variabilidad.

---

### Caso 2: Empresa Grande

**Contexto**: Portafolio grande, apps con diferente importancia.

**Configuración**:
- Progress Method: Weighted Average
- Status: Excluir TBS, incluir WIP, CLO
- Weights: Min=0.3, Default=1.0, Max=5.0
- Criticality: Low=0.9, Med=1.0, High=1.5
- Global: Weighted by BU Size

**Justificación**: Variaciones importantes, apps críticas impactan más.

---

### Caso 3: Auditoría/Compliance

**Contexto**: Solo interesa lo completado.

**Configuración**:
- Progress Method: Minimum Progress
- Status: Solo CLO
- Weights: Min=1.0, Default=1.0, Max=1.0
- Criticality: Todos=1.0
- Global: Simple Average

**Justificación**: Solo cosas completas, sin ponderación.

---

### Caso 4: Metodología Agile

**Contexto**: Énfasis en trabajo en progreso.

**Configuración**:
- Progress Method: Weighted Average
- Status: Excluir TBS, incluir WIP, CLO
- Weights: Min=0.5, Default=1.0, Max=3.0
- Criticality: Low=1.0, Med=1.1, High=1.2
- Global: Weighted by BU Size

**Justificación**: Incluye WIP pero no TBS, permite variación.

---

## Exportar e Importar

### Exportar

1. Configura los parámetros deseados
2. Haz clic en "Save Configuration"
3. Ve a Settings → Export Configuration
4. Se descarga JSON con todo: BUs, Apps, Waves, **Fórmulas**, Whitelabel

### Importar

1. Ve a Settings → Import Configuration
2. Selecciona archivo JSON exportado
3. Automáticamente:
   - Restaura BUs y Apps
   - **Restaura fórmulas**
   - Restaura Whitelabel
   - Recalcula progreso

**Nota**: Soporta archivos sin formula config (compatible hacia atrás).

---

## FAQ

### P1: ¿Diferencia entre Weighted y Simple Average?

**R**: Weighted da más importancia a apps con mayor peso. Simple trata todas igual.

**Ejemplo**:
- App Crítica: 50% (peso 3.0)
- App Normal: 100% (peso 1.0)
- Weighted: 62.5%
- Simple: 75%

### P2: ¿Cuándo usar Minimum Progress?

**R**: Solo cuando TODAS las apps deben completarse. Ej: migración de datos.

### P3: ¿Puedo cambiar fórmulas en medio del proyecto?

**R**: Sí, pero números históricos cambiarán. **Recomendación**: Decide al inicio.

### P4: ¿Qué pasa si no incluyo TBS?

**R**: Se ignoran, no afectan el cálculo. Hace que progreso se vea más alto.

### P5: ¿Cómo sé qué pesos asignar?

**R**: Preguntas:
- ¿Impacto si falla? → Define criticidad
- ¿Es más importante que otras? → Peso alto
- ¿Es estándar? → Peso 1.0
- ¿Es menor? → Peso 0.5

### P6: ¿Multiplicadores > 1.2?

**R**: Sí. Recomendaciones:
- 1.0 - 1.2: Pequeño boost
- 1.2 - 1.5: Boost moderado
- > 1.5: Máximo impacto

### P7: ¿Qué es "Weighted by BU Size"?

**R**: BUs con más apps influyen más en progreso global.

### P8: ¿Se pierden fórmulas si limpio datos?

**R**: No. Se guardan en localStorage. Reset vuelve a defaults.

### P9: ¿Exportar solo fórmulas?

**R**: No. Se exportan con proyecto completo. Pero otros las importan automáticamente.

### P10: ¿Cómo valido fórmulas?

**R**: Usa botón "Test Calculation" en el panel. Muestra paso a paso.

---

## Resumen Rápido

### Pasos de Configuración

1. Setup → Calculation Formulas
2. Elige Progress Method
3. Define Status Inclusion
4. Configura Weights
5. Ajusta Criticality Multipliers
6. Elige Global Formula
7. Guarda con "Save Configuration"
8. Prueba con "Test Calculation"

### Variables Clave

| Variable | Rango | Defecto | Impacto |
|----------|-------|---------|---------|
| Progress Method | 3 opciones | Weighted | **ALTO** |
| Status Inclusion | TBS/WIP/CLO | WIP,CLO | **ALTO** |
| Min Weight | 0.3-2.0 | 0.5 | Bajo |
| Max Weight | 1.0-10.0 | 3.0 | **ALTO** |
| Default Weight | Min-Max | 1.0 | Medio |
| Low Multiplier | 0.5-1.5 | 1.0 | Bajo |
| Med Multiplier | 0.5-1.5 | 1.0 | Bajo |
| High Multiplier | 1.0-2.0 | 1.2 | **ALTO** |
| Global Formula | 2 opciones | Weighted | Medio |

---

**Versión**: 1.0 | **Última actualización**: Octubre 2025

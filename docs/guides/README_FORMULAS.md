# 📚 Documentación de Fórmulas de Cálculo

Esta sección contiene guías completas para configurar y entender las fórmulas de progreso ponderado en Dashboard Enhanced.

---

## 📖 Guías Disponibles

### 1. **Quick Start** - Empieza Aquí (5 minutos)
**Archivo**: `FORMULA_QUICKSTART.md`

Guía visual y práctica para usuarios que recién comienzan. Incluye:
- 7 pasos para primera configuración
- Ejemplos visuales de cálculos
- 4 presets listos para usar
- Cambios comunes en 30 segundos
- SOS rápido para problemas

**Para quién**: Administradores nuevos, implementadores rápidos.

---

### 2. **Guía Completa** - Referencia Exhaustiva (30 minutos)
**Archivo**: `FORMULA_GUIDE.md`

Documentación técnica completa. Incluye:
- Explicación detallada de cada parámetro
- Fórmulas matemáticas completas
- Ejemplos paso a paso
- Escenarios prácticos (Startup, Empresa Grande, Auditoría, Agile)
- FAQ con 10 preguntas frecuentes
- Tabla de variables clave

**Para quién**: Administradores expertos, analistas, auditores.

---

## 📚 Estructura de Contenido

### Quick Start (`FORMULA_QUICKSTART.md`)

```
🎯 Tu Primer Configuración (7 pasos)
  ├─ Paso 1: Abre Setup
  ├─ Paso 2: Selecciona Método
  ├─ Paso 3: Define Estados
  ├─ Paso 4: Configura Pesos
  ├─ Paso 5: Criticidad
  ├─ Paso 6: Fórmula Global
  └─ Paso 7: Guarda y Prueba

📊 Entender tu Progreso
  ├─ Fórmula = Promedio Inteligente
  ├─ Por Qué Pesa Más
  └─ Con Criticidad

🎨 Presets Listos para Usar (4 opciones)
  ├─ Preset 1: Startup/Pequeño Equipo
  ├─ Preset 2: Empresa Grande/Portafolio
  ├─ Preset 3: Solo Completado (Auditoría)
  └─ Preset 4: Agile/Iterativo

⚡ Cambios Comunes (4 escenarios)
✅ Validación
📌 Recordar (5 conceptos)
🔄 Exportar/Importar
🆘 SOS Rápido (tabla de problemas)
```

### Guía Completa (`FORMULA_GUIDE.md`)

```
Introducción
  ├─ ¿Qué son las Fórmulas?
  ├─ ¿Por Qué Personalizar?
  └─ Conceptos Clave (tabla)

Acceso al Panel (3 pasos)

Parámetros Principales (5 secciones)
  ├─ 1. Progress Calculation Method
  │   ├─ Weighted Average (RECOMENDADO)
  │   ├─ Simple Average
  │   └─ Minimum Progress
  ├─ 2. Status Inclusion Rules
  │   ├─ Tabla de estados
  │   ├─ Comportamiento
  │   └─ Escenarios comunes
  ├─ 3. Weight Parameters
  │   ├─ Tabla de parámetros
  │   ├─ Uso en cálculos
  │   └─ Ejemplo
  ├─ 4. Criticality Multipliers
  │   ├─ Tabla de multiplicadores
  │   ├─ Cómo funciona
  │   ├─ Ejemplo
  │   └─ Cuándo aumentar
  └─ 5. Global Progress Formula
      ├─ Weighted by BU Size
      └─ Simple Average

Cálculo Ponderado
  ├─ Fórmula Completa
  └─ Ejemplo Paso a Paso

Ejemplos Prácticos (4 casos)
  ├─ Caso 1: Startup Tecnológica
  ├─ Caso 2: Empresa Grande
  ├─ Caso 3: Auditoría/Compliance
  └─ Caso 4: Metodología Agile

Exportar e Importar
  ├─ Exportar
  └─ Importar

FAQ (10 preguntas)
  ├─ P1-P10 respondidas
  └─ Resumen Rápido

Resumen Rápido
  ├─ Pasos de Configuración
  └─ Variables Clave (tabla)
```

---

## 🎓 Flujo de Lectura Recomendado

### Para Administrador Nuevo (20 minutos totales)

1. **Quick Start** (5 min)
   - Lee los 7 pasos
   - Mira los ejemplos visuales
   - Prueba uno de los 4 presets

2. **Guía Completa** - Sección "Acceso al Panel" (5 min)
   - Confirma dónde acceder

3. **Guía Completa** - Sección "Parámetros Principales" (10 min)
   - Lee solo la subsección de tu método (Weighted/Simple/Minimum)
   - Entiende los estados que necesitas
   - Listo para configurar

### Para Auditor/Compliance (30 minutos totales)

1. **Guía Completa** - Introducción (5 min)
   - Entiende conceptos clave

2. **Guía Completa** - Parámetros Principales (10 min)
   - Lee todo, enfocándose en "Status Inclusion Rules"

3. **Guía Completa** - Ejemplo Caso 3: Auditoría/Compliance (5 min)
   - Configuración lista para usar

4. **Guía Completa** - Cálculo Ponderado (10 min)
   - Entiende las matemáticas exactas

### Para Analista de Datos (Todos los documentos - 60 minutos)

1. Quick Start - Complete
2. Guía Completa - Complete
3. FAQ - Profundizar en preguntas específicas
4. Cálculo Ponderado - Paso a paso entendimiento

---

## 🔑 Conceptos Clave a Recordar

### 5 Decisiones Principales

| # | Decisión | Impacto | Opciones |
|---|----------|--------|---------|
| 1 | **Método de Cálculo** | **MUY ALTO** | Weighted / Simple / Minimum |
| 2 | **Inclusión de Estados** | **ALTO** | TBS / WIP / CLO (combinables) |
| 3 | **Pesos de Apps** | **ALTO** | 0.3 - 10.0 |
| 4 | **Criticidad de Apps** | **ALTO** | 0.5 - 2.0 (multiplicadores) |
| 5 | **Fórmula Global** | **MEDIO** | Weighted by Size / Simple |

### 3 Niveles de Complejidad

**Nivel 1: Básico**
- Usa defaults
- Métodos recomendados
- No ajusta pesos individualmente
- ⏱️ 5 minutos

**Nivel 2: Intermedio**
- Lee Guía Completa
- Personaliza pesos por app
- Ajusta criticidades
- ⏱️ 30 minutos

**Nivel 3: Avanzado**
- Entiende matemáticas
- Crea presets propios
- Valida con Test Calculation
- ⏱️ 60+ minutos

---

## 🔧 Troubleshooting Rápido

**Progreso se ve muy bajo**
→ Ve a Quick Start → "Cambios Comunes" → Primera opción

**Progreso se ve muy alto**
→ Ve a Quick Start → "Cambios Comunes" → Segunda opción

**Una app domina todo**
→ Ve a Quick Start → "Cambios Comunes" → Tercera opción

**Resultado NO tiene sentido**
→ Ve a Guía Completa → Sección "Cálculo Ponderado" → "Ejemplo Paso a Paso"

**Pregunta sobre un parámetro**
→ Ve a Guía Completa → "Parámetros Principales" → Busca por nombre

---

## 📊 Exemplos de Fórmulas

### Fórmula Weighted Average (Recomendada)

$$BU Progress = \frac{\sum (App Progress \times Weight \times Criticality Multiplier)}{\sum (Weight \times Criticality Multiplier)}$$

**Cuándo usar**: Cuando apps tienen diferente importancia.

### Fórmula Simple Average

$$BU Progress = \frac{\sum App Progress}{Count(Apps)}$$

**Cuándo usar**: Cuando todas las apps importan igual.

### Fórmula Minimum Progress

$$BU Progress = MIN(App1 Progress, App2 Progress, ...)$$

**Cuándo usar**: Cuando TODAS deben estar completas.

---

## ✅ Checklist de Configuración

Usa esto para verificar que tu configuración está lista:

- [ ] Decidí el método (Weighted / Simple / Minimum)
- [ ] Definí estados a incluir (TBS / WIP / CLO)
- [ ] Configuré pesos (min / default / max)
- [ ] Ajusté multiplicadores si necesario
- [ ] Elegí fórmula global (Weighted / Simple)
- [ ] Clickeé "Save Configuration"
- [ ] Clickeé "Test Calculation" y vi resultado
- [ ] El resultado tiene sentido
- [ ] Exporté configuración para backup

---

## 📞 Soporte y Referencias

### Si necesitas saber...

| Necesito... | Archivo | Sección |
|-----------|---------|---------|
| Cómo empezar rápido | FORMULA_QUICKSTART.md | Top |
| Definición de parámetro | FORMULA_GUIDE.md | Parámetros Principales |
| Cómo se calcula | FORMULA_GUIDE.md | Cálculo Ponderado |
| Ejemplo de mi caso | FORMULA_GUIDE.md | Ejemplos Prácticos |
| Respuesta a pregunta | FORMULA_GUIDE.md | FAQ |
| Validar configuración | FORMULA_QUICKSTART.md | Validación |
| Solucionar problema | FORMULA_QUICKSTART.md | SOS Rápido |

---

## 🎯 Objetivos Alcanzables

Con estas guías puedes:

✅ Configurar fórmulas en 5-30 minutos  
✅ Entender impacto de cada parámetro  
✅ Validar tus configuraciones  
✅ Crear presets reutilizables  
✅ Exportar e importar configuraciones  
✅ Troubleshoot problemas comunes  
✅ Compartir configuraciones con equipo  

---

**Última actualización**: Octubre 2025  
**Versión**: 1.0  
**Documentos**: 2 (Quick Start + Guía Completa)
